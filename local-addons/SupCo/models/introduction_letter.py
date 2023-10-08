from odoo import api, fields, models
from odoo import exceptions
from datetime import datetime


class SupremeCourtLetter(models.Model):
    _name = 'supreme.court.letter'
    _description = 'Supreme Court Letter'

    # recipient_name = fields.Char(string='Recipient Name')
    recipient_name = fields.Many2many('supreme.court.employee', string='Recipient Name')
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
