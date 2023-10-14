from odoo import api, fields, models

from odoo import exceptions
from datetime import datetime



class SupremeCourtLetter(models.Model):
    _name = 'supreme.court.letter'
    _description = 'Supreme Court Letter'


    # recipient_name = fields.Char(string='Recipient Name')
    recipient_name = fields.Many2many('res.users', string='Recipient Name')
    title_position = fields.Char(string='Title/Position')
    organization_unit = fields.Char(string='Organization/Unit')
    address = fields.Char(string='Address')
    regarding = fields.Text(string='Regarding')
    request = fields.Text(string='Request')
    validity_date = fields.Date(string='Validity Date')
    @api.constrains('validity_date')
    def _check_date(self):
        for record in self:
            if record.validity_date and record.validity_date <= datetime.today().date():
                raise exceptions.ValidationError('Valid Date must be after today!')

    number = fields.Integer(string='Số')
    recipient_name = fields.Char(string='Đồng chí')
    title_position = fields.Char(string='Chức vụ')
    organization_unit = fields.Char(string='Đơn vị')
    address = fields.Char(string='Cử đến')
    regarding = fields.Text(string='Về việc')
    request = fields.Text(string='Yêu cầu (Tên các đồng chí)')
    validity_date = fields.Date(string='Ngày hiệu lực')
    created_by = fields.Many2one('res.users', string='Tạo bởi', default=lambda self: self.env.user)

