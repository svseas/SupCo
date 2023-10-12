from odoo import models, fields, api


class Employee(models.Model):
    _inherit = 'res.users'
    # _name = "supreme.court.employee"
    # _description = 'Supreme Court Employee'

    # name = fields.Char(string="Full Name")
    # title_position = fields.Char(string="Title Position")
    dob = fields.Date(string='Date of Birth')
    national_id = fields.Char(string='National ID')
    department = fields.Many2many('supreme.court.department', string='Department')
    introduction_letter = fields.Many2many("supreme.court.letter", string="Supreme Court Letter")
