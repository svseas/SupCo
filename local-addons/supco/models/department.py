from odoo import models, fields, api


class Department(models.Model):
    _name = 'supreme.court.department'
    _description = "Supreme Court Department"

    name = fields.Char(string='Phòng Ban', required=True)
    code = fields.Char(string='Mã Phòng Ban', required=True)

    _sql_constraints = [
        ("code_of_department_uq",
         "UNIQUE (code)",
         "Code of Department must be unique."),
        ("name_of_department_uq",
         "UNIQUE (name)",
         "Name of Department must be unique.")
    ]
    employee = fields.Many2many('res.users', string='Employee')
