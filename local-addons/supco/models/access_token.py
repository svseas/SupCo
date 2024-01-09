from odoo import models, fields


class AccessToken(models.Model):
    _name = 'access.token'
    _description = 'Access Tokens'

    name = fields.Char('Token Name', required=True)
    token = fields.Char('Token', required=True, index=True)
    expiration_date = fields.Datetime('Expiration Date', required=True)
