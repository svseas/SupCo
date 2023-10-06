from odoo import api, fields, models


class SupremeCourtLetter(models.Model):
    _name = 'supreme.court.letter'
    _description = 'Supreme Court Letter'

    number = fields.Char(string='Number')
    recipient_name = fields.Char(string='Recipient Name')
    title_position = fields.Char(string='Title/Position')
    organization_unit = fields.Char(string='Organization/Unit')
    address = fields.Char(string='Address')
    regarding = fields.Text(string='Regarding')
    request = fields.Text(string='Request')
    validity_date = fields.Date(string='Validity Date')
