import random
import string
import base64
import io
import qrcode
from datetime import datetime
from odoo import api, fields, models, exceptions


class SupremeCourtLetter(models.Model):
    _name = 'supreme.court.letter'
    _description = 'Supreme Court Letter'

    number = fields.Integer(string='Số')
    recipient_name = fields.Char(string='Đồng chí')
    title_position = fields.Char(string='Chức vụ')
    organization_unit = fields.Char(string='Đơn vị')
    address = fields.Char(string='Cử đến')
    regarding = fields.Text(string='Về việc')
    request = fields.Text(string='Yêu cầu (Tên các đồng chí)')
    validity_date = fields.Date(string='Ngày hiệu lực')
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
        report_name = 'supco.report_supreme_court_letter_main'
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


