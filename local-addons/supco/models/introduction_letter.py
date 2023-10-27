import random
import string
import base64
import io
import qrcode
from datetime import datetime, timedelta
from odoo import api, fields, models, exceptions, _
import logging
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class SupremeCourtLetter(models.Model):
    _name = "supreme.court.letter"
    _description = "Supreme Court Letter"
    _rec_name = "display_number"

    number = fields.Integer(
        string="Số",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: self.env["ir.sequence"].next_by_code(
            "supreme.court.letter"
        ),
    )

    @api.model
    def _get_default_user(self):
        return [self.env.user.id]

    user_ids = fields.Many2many(
        "res.users", string="Người gửi", default=_get_default_user
    )

    recipient_name = fields.Char(
        string="Tên các đồng chí", compute="_compute_recipient_name", store=True
    )
    display_number = fields.Char(string="Số", compute="_compute_display_number")

    @api.depends("number")
    def _compute_display_number(self):
        for record in self:
            record.display_number = f"{record.number:05}"

    @api.depends("user_ids")
    def _compute_recipient_name(self):
        """This method is used to compute the recipient names"""
        for letter in self:
            recipient_name = ""
            for user in letter.user_ids:
                if user.name:
                    recipient_name += user.name + ", "
            letter.recipient_name = recipient_name[:-2]

    title_position = fields.Many2many('supreme.court.position', string="Chức vụ")

    organization_unit = fields.Char(string="Tổ chức", default="Báo Công Lý")
    address = fields.Text(string="Nơi đến")
    regarding = fields.Text(string="Về việc")
    validity_duration = fields.Selection(
        string="Thời hạn",
        selection=[
            ("1", "1 tuần"),
            ("2", "2 tuần"),
            ("3", "3 tuần"),
            ("4", "4 tuần"),
        ],
        default="2",
    )
    validity_to_date = fields.Date(string="Hiệu lực đến ngày", compute="_compute_validity_to_date", readonly=True, store=True)
    is_valid = fields.Boolean(string="Còn hiệu lực", compute="_compute_is_valid")

    @api.depends("validity_duration", "approval_status", "approve_date")
    def _compute_validity_to_date(self):
        for letter in self:
            if letter.validity_duration and letter.approval_status == "approved":
                letter.validity_to_date = letter.approve_date + timedelta(weeks=int(letter.validity_duration))
            else:
                letter.validity_to_date = False

    @api.depends("validity_to_date")
    def _compute_is_valid(self):
        for letter in self:
            if letter.validity_to_date and letter.validity_to_date >= datetime.now().date():
                letter.is_valid = True
            else:
                letter.is_valid = False

    created_by = fields.Many2one(
        "res.users", string="Tạo bởi", default=lambda self: self.env.user
    )
    custom_url = fields.Char(string="URL", compute="_compute_custom_url", store=True)
    qr_code = fields.Binary("Mã QR", compute="_compute_qr_code", store=True)
    public_id = fields.Char(
        string="Public ID",
        copy=False,
        readonly=True,
        default=lambda self: "_".join(
            [
                "cl",
                "ggt",
                "".join(random.choices(string.ascii_letters + string.digits, k=16)),
            ]
        ),
    )

    @api.depends("number")
    def _compute_custom_url(self):
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        for letter in self:
            if letter.public_id:
                letter.custom_url = f"{base_url}/letters/ggt/{letter.public_id}"
            else:
                letter.custom_url = False

    @api.depends("number")
    def _compute_qr_code(self):
        for letter in self:
            base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
            if letter.public_id:
                qr_code_link = f"{base_url}/letters/ggt/{letter.public_id}"

                # Generate a QR code from the link
                img = qrcode.make(qr_code_link)
                buffer = io.BytesIO()
                img.save(buffer, format="PNG")
                encoded_image = base64.b64encode(buffer.getvalue())
                letter.qr_code = encoded_image

    def button_print_pdf(self):
        self.ensure_one()  # Ensure this is called for one record only
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        if self.public_id:
            pdf = f"{base_url}/letters/pdf/{self.public_id}"
            return {
                "type": "ir.actions.act_url",
                "url": pdf,
                "target": "new",
            }

    approval_status = fields.Selection(
        [
            ("draft", "Nháp"),
            ("waiting_first_approval", "Chờ duyệt lần 1"),
            ("waiting_second_approval", "Chờ duyệt lần 2"),
            ("approved", "Đã được duyệt"),
            ("rejected", "Bị từ chối"),
        ],
        default="draft",
        string="Trạng thái duyệt",
    )

    first_approval_by = fields.Many2one(
        "res.users", string="Người duyệt lần đầu", readonly=True
    )
    second_approval_by = fields.Many2one(
        "res.users", string="Người duyệt lần hai", readonly=True
    )

    reject_by = fields.Many2one("res.users", string="Người từ chối", readonly=True)
    reject_reason = fields.Text(string="Lý do từ chối")
    reject_reason_user = fields.Text(
        string="Lý do từ chối", readonly=True, compute="_compute_reject_reason_user"
    )
    approve_date = fields.Date(string="Ngày duyệt", readonly=True, store=True)

    @api.depends("reject_reason")
    def _compute_reject_reason_user(self):
        for letter in self:
            letter.reject_reason_user = letter.reject_reason

    def action_request_first_approval(self):
        self.ensure_one()

        # Check if the record already has either first or second approver set
        if self.first_approval_by or self.second_approval_by:
            raise UserError(
                _("Thư này đã có người duyệt. Không thể xin duyệt lần một.")
            )

        # Check if the status has already been changed to waiting_first_approval
        if self.approval_status == "waiting_first_approval":
            raise UserError(_("Thư này đang trong trạng thái 'Xin duyệt lần 1'."))

        self.write(
            {
                "approval_status": "waiting_first_approval",
                "first_approval_by": False,
                "second_approval_by": False,
            }
        )

        return {
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "supreme.court.letter",
        }

    def action_first_approval(self):
        self.ensure_one()  # Ensure that only one record is being processed
        self.write(
            {
                "approval_status": "waiting_second_approval",
                "first_approval_by": self.env.user.id,
            }
        )
        return {
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "supreme.court.letter",
        }

    def action_second_approval(self):
        self.ensure_one()
        self.write(
            {"approval_status": "approved",
             "second_approval_by": self.env.user.id,
             "approve_date": datetime.now().date()}
        )
        return {
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "supreme.court.letter",
        }

    def action_reject(self):
        self.ensure_one()

        # Check if a reject reason is provided
        if not self.reject_reason:
            raise exceptions.UserError(
                _("Xin hãy đưa ra lý do từ chối trước khi tiếp tục.")
            )

        # Check if the status is approved
        if self.approval_status == "approved":
            raise exceptions.UserError(
                _("Không thể từ chối giấy giới thiệu đã được duyệt.")
            )

        # Create log before changing the status

        self.env["letter.rejection.log"].create(
            {
                "letter_id": self.id,
                "reject_by": self.env.user.id,
                "rejection_reason": self.reject_reason,
                "rejection_time": datetime.now(),
            }
        )

        self.write(
            {
                "approval_status": "rejected",
                "second_approval_by": False,
                "first_approval_by": False,
                "reject_by": self.env.user.id,
            }
        )

        # Notify the client about status change
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": "Rejection",  # Notification's title
                "message": _("Giấy giới thiệu đã bị từ chối."),
                "sticky": False,  # True means the notification won't auto-close
            },
        }

    attachment_ids = fields.One2many(
        "ir.attachment",
        "res_id",
        domain=[("res_model", "=", "supreme.court.letter")],
        string="Tệp tin đính kèm",
    )

    date_created = fields.Date(
        string="Ngày tạo", default=datetime.today().date(), readonly=True
    )

    gdrive_url = fields.Char(string="Tài liệu từ Google Drive")

    def reject_show(self):
        return {
            "name": "Lý do từ chối",
            "views": [
                [self.env.ref("supco.view_letter_rejection_log_logview").id, "log"]
            ],
            "type": "ir.actions.act_window",
            "res_model": "letter.rejection.log",
            "target": "new",
            "domain": [("letter_id", "=", self.id)],
        }


class LetterRejectionLog(models.Model):
    _name = "letter.rejection.log"
    _description = "Log of Rejected Letters"

    letter_id = fields.Many2one(
        "supreme.court.letter", string="Giấy giới thiệu số", readonly=True,
        ondelete="cascade"
    )
    reject_by = fields.Many2one("res.users", string="Người từ chối", readonly=True)
    rejection_reason = fields.Text("Lý do từ chối")
    rejection_time = fields.Datetime(
        string="Time Rejected", default=datetime.now(), readonly=True
    )
