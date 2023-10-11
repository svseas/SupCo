from odoo import models,fields,api

class Department(models.Model):
    _name = 'supreme.court.department'
    _description = "Supreme Court Department"

    name = fields.Char(string='Department', required=True)
    code = fields.Char(string='Code of Department', required=True)
    employee = fields.Many2many('res.users',string='Employee')