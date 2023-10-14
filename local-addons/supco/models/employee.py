from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'res.users'
    # _name = "supreme.court.employee"
    # _description = 'Supreme Court Employee'

    # name = fields.Char(string="Full Name")
    # title_position = fields.Char(string="Title Position")
    dob = fields.Date(string='Date of Birth')
    national_id = fields.Char(string='National ID')
    department = fields.Many2many('supreme.court.department',string='Department')
    introduction_letter = fields.Many2many("supreme.court.letter",string="Supreme Court Letter")
    custom_url = fields.Char(string="URL", compute='_compute_custom_url', store=True)

    @api.depends('national_id')
    def _compute_custom_url(self):
        for user in self:
            if user.national_id:
                user.custom_url = f'http://localhost:8060/users/{user.national_id}'
            else:
                user.custom_url = False
    
    _sql_constraints = [
        ("national_id_uq",
        "UNIQUE (national_id)",
        "National ID must be unique.")
        ]