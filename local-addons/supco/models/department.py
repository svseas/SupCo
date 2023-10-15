from odoo import models,fields,api

class Department(models.Model):
    _name = 'supreme.court.department'
    _description = "Supreme Court Department"

    name = fields.Char(string='Department', required=True)
    code = fields.Char(string='Code of Department', required=True)
    employee = fields.One2many('res.users','department',string='Employee')

    _sql_constraints = [
        ("code_of_department_uq",
        "UNIQUE (code)",
        "Code of Department must be unique."),
        ("name_of_department_uq",
        "UNIQUE (name)",
        "Name of Department must be unique.")
        ]