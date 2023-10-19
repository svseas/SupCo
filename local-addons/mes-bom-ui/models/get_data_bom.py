from odoo import models, fields, api

class DataTable(models.Model):
    _inherit = ['mrp.bom']
    _description = 'Data Table'

    @api.model
    def get_bom_data(self):
        data = self.env['mrp.bom'].search([])

        result = []
        for record in data:
            product_name = record.product_tmpl_id.name if record.product_tmpl_id else ""
            approve_name = record.approved_by.name if record.approved_by else ""
            ng_percent = record.ng_percent * 100
            record_data = {
                'code': record.code,
                'name': product_name,
                'ng_percent': ng_percent,
                'approved_by': approve_name,
                'id': record.id,
            }
            result.append(record_data)
        table_keys = {
            'code': "MÃ",
            'name': "SẢN PHẨM",
            'ng_percent': "% NG",
            'approved_by': "TRẠNG THÁI",
        }

        return result, table_keys