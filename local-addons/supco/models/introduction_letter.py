import random
import string
import base64
import io
import qrcode
from datetime import datetime
from odoo import api, fields, models, exceptions
import logging
_logger = logging.getLogger(__name__)


class SupremeCourtLetter(models.Model):
    _name = 'supreme.court.letter'
    _description = 'Supreme Court Letter'

    number = fields.Integer(string='Number', required=True, copy=False, readonly=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('supreme.court.letter'))
    user_ids = fields.Many2many('res.users', string='Sender')
    recipient_name = fields.Char(string='Recipient Names', compute='_compute_recipient_name', store=True)
    display_number = fields.Char(string='Display Number', compute='_compute_display_number')

    @api.depends('number')
    def _compute_display_number(self):
        for record in self:
            record.display_number = f'{record.number:05}'

    @api.depends('user_ids')
    def _compute_recipient_name(self):
        """This method is used to compute the recipient names"""
        for letter in self:
            recipient_name = ''
            for user in letter.user_ids:
                if user.name:
                    recipient_name += user.name + ', '
            letter.recipient_name = recipient_name[:-2]

    title_position = fields.Char(string='Title Position')
    organization_unit = fields.Char(string='Organization Unit')
    address = fields.Char(string='Address')
    regarding = fields.Text(string='Regarding')
    validity_date = fields.Date(string='Validity Date')
    created_by = fields.Many2one('res.users', string='Tạo bởi', default=lambda self: self.env.user)
    custom_url = fields.Char(string="URL", compute='_compute_custom_url', store=True)
    qr_code = fields.Binary("QR Code", compute='_compute_qr_code', store=True)
    public_id = fields.Char(string="Public ID", copy=False, readonly=True, default=lambda self: ''.join(random.choices(string.ascii_letters + string.digits, k=16)))

    @api.constrains('validity_date')
    def _check_date(self):
        for record in self:
            if record.validity_date and record.validity_date <= datetime.today().date():
                raise exceptions.ValidationError('Valid Date must be after today!')

    @api.depends('number')
    def _compute_custom_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for letter in self:
            if letter.public_id:
                letter.custom_url = f'{base_url}/letters/public/{letter.public_id}'
            else:
                letter.custom_url = False

    @api.depends('number')
    def _compute_qr_code(self):
        for letter in self:
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            if letter.public_id:
                qr_code_link = f'{base_url}/letters/public/{letter.public_id}'

                # Generate a QR code from the link
                img = qrcode.make(qr_code_link)
                buffer = io.BytesIO()
                img.save(buffer, format="PNG")
                encoded_image = base64.b64encode(buffer.getvalue())
                letter.qr_code = encoded_image

    approval_status = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_first_approval', 'Waiting for First Approval'),
        ('waiting_second_approval', 'Waiting for Second Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='draft', string="Approval Status")

    first_approval_by = fields.Many2one('res.users', string="First Approved By")
    second_approval_by = fields.Many2one('res.users', string="Second Approved By")

    def action_first_approval(self):
        self.write({
            'approval_status': 'waiting_second_approval',
            'first_approval_by': self.env.user.id
        })

    def action_second_approval(self):
        self.write({
            'approval_status': 'approved',
            'second_approval_by': self.env.user.id
        })

