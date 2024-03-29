from odoo import models, fields, api
import datetime


class Employee(models.Model):
    _inherit = "res.users"
    _rec_name = "combined_name"

    code = fields.Char(string="Mã", required=True)
    _sql_constraints = [("code_unique", "UNIQUE(code)", "Mã phải là duy nhất.")]
    combined_name = fields.Char(
        string="Tên", compute="_compute_combined_name", store=True
    )

    @api.depends("name", "code")
    def _compute_combined_name(self):
        for employee in self:
            employee.combined_name = f"{employee.code} - {employee.name}"

    dob = fields.Date(string="Ngày sinh", default=datetime.datetime(1980, 1, 1))
    national_id = fields.Char(string="Số CCCD")
    introduction_letter = fields.Many2many(
        "supreme.court.letter", string="Giấy giới thiệu"
    )
    custom_url = fields.Char(string="URL", compute="_compute_custom_url", store=True)
    position = fields.Many2one("supreme.court.position", string="Vị trí")

    @api.depends("combined_name")
    def _compute_custom_url(self):
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        for user in self:
            if user.code:
                user.custom_url = f"{base_url}/nhan-vien/{user.code}"
            else:
                user.custom_url = False

    _sql_constraints = [
        ("national_id_uq", "UNIQUE (national_id)", "CCCD Phải là duy nhất.")
    ]
    department = fields.Many2many("supreme.court.department", string="Phòng ban")


class Position(models.Model):
    _name = "supreme.court.position"
    _rec_name = "name"

    code = fields.Char(string="Mã")
    name = fields.Char(string="Vị trí", required=True)
    description = fields.Text(string="Mô tả")
