from odoo import http
from odoo.http import request
import io
import qrcode
class UserController(http.Controller):

    @http.route('/users/<string:national_id>', type='http', auth="user", website=True)
    def user_info(self, national_id):
        user = request.env['res.users'].sudo().search([('national_id', '=', national_id)], limit=1)

        if user:
            name = user.name
            dob = user.dob
            qr = qrcode.QRCode()
            qr.add_data(f"http://localhost:8060/users/{national_id}")
            f = io.StringIO()
            qr.print_ascii(out=f)
            f.seek(0)
            qr_code = f.read()
            return request.render('supco.template_name', {'name': name, 'dob': dob, 'qr_code': qr_code})
        else:
            return "User not found or You have no right to access."
