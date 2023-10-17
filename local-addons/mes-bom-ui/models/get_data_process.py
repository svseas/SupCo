from odoo import models, fields, api

class DataTable(models.Model):
    _inherit = ['tech.process']
    _description = 'Data Table'

    @api.model
    def get_process_data(self):
        product_id = 1
        data = self.env['tech.process'].browse(product_id)

        result = []
        for record in data:
            record_data = {
                'code': record.code,
                'name': record.name,
            }
            result.append(record_data)
        table_keys = {
            'code': "MÃ",
            'name': "SẢN PHẨM",
            'ng_percent': "% NG",
            'approved_by': "TRẠNG THÁI",
        }

        return result, table_keys