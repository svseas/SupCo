from odoo import models, fields, api


class Employee(models.Model):
    _inherit = 'res.users'

    dob = fields.Date(string='Ngày Sinh')
    national_id = fields.Char(string='Số CCCD')
    introduction_letter = fields.Many2many("supreme.court.letter", string="Supreme Court Letter")
    custom_url = fields.Char(string="URL", compute='_compute_custom_url', store=True)

    @api.depends('national_id')
    def _compute_custom_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for user in self:
            if user.national_id:
                user.custom_url = f'{base_url}/users/{user.national_id}'
            else:
                user.custom_url = False

    _sql_constraints = [
        ("national_id_uq",
         "UNIQUE (national_id)",
         "National ID must be unique.")
    ]
    department = fields.Many2many('supreme.court.department', string='Phòng ban')
