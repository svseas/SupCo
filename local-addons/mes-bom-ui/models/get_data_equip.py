from odoo import models, fields, api

class DataTable(models.Model):
    _inherit = ['equipment.template']
    _description = 'Data Table'

    @api.model
    def get_equip_data(self):
        data = self.env['equipment.template'].search([])

        result = []
        for record in data:
            record_data = {
                'code': record.code,
                'name': record.name,
                'position': record.position,
            }
            result.append(record_data)
        table_keys = {
            'code': "MÃ",
            'name': "SẢN PHẨM",
            'position': "VỊ TRÍ",
        }

        return result, table_keys