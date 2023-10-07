from odoo import api, fields, models


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
