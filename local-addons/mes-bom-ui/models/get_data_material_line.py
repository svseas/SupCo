from odoo import models, fields, api

class DataTable(models.Model):
    _inherit = ['material.line']
    _description = 'Data Table'

    @api.model
    def get_material_line_data(self):
        data = self.env['material.line'].search([])

        result = []
        for record in data:
            record_data = {
                'code': record.code,
                'name': record.name,
                'description': record.description,
                'image': "",
            }
            result.append(record_data)

        # Define custom labels for each key
        table_keys = {
            'code': "MÃ",
            'name': "TÊN CÔNG ĐOẠN",
            'description': "MÔ TẢ",
            'image': "HÌNH ẢNH",
        }

        return result, table_keys