# from odoo import http
# from odoo.http import request
# from werkzeug.wrappers import Response
# from datetime import date
# import json
# import io
# import qrcode

# class CustomUserController(http.Controller):

#     @http.route('/users/<string:national_id>', type='http', auth="public")
#     def show_user_info(self, national_id, **kw):

#         user = request.env['res.users'].search([('national_id', '=', national_id)], limit=1)


#         if user:
#             name = user.name
#             dob = user.dob.strftime('%Y-%m-%d')  

#             qr = qrcode.QRCode()
#             qr.add_data(f"http://localhost:8060/users/{national_id}")
#             f = io.StringIO()
#             qr.print_ascii(out=f)
#             f.seek(0)
#             qr_code = f.read()
#             qr_code = qr_code.replace("\n", "                                                                                                                                                                       ")
#             response_data = {
#                 'name': name,
#                 'dob': dob,
#                 'qr_code': qr_code
#             }
#             json_data = json.dumps(response_data,ensure_ascii=False, indent=4)

#             response = Response(json_data, content_type='application/json')

#             return response
#         else:
#             error_data = {
#                 'error': 'User Not Found'
#             }
#             error_json = json.dumps(error_data)
#             error_response = Response(error_json, content_type='application/json')

#             return error_response
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
            return request.render('SupCo.template_name', {'name': name, 'dob': dob, 'qr_code': qr_code})
        else:
            return "User not found or You have no right to access."

