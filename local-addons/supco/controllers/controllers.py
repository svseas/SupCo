import base64
import string
import requests
from odoo import http
from odoo.http import request, route, content_disposition, Response
import io
import qrcode
from odoo.addons.web.controllers.main import ReportController



class UserController(http.Controller):

    @http.route('/users/<string:national_id>', type='http', auth="public", website=True)
    def user_info(self, national_id):
        user = request.env['res.users'].sudo().search([('national_id', '=', national_id)], limit=1)

        if user:
            # Get the base URL from system parameters
            base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')

            name = user.name
            dob = user.dob
            national_id = user.national_id
            department = user.department.name
            introduction_letter = user.introduction_letter
            position = user.function
            avatar = user.image_1920.decode("utf-8") if user.image_1920 else None

            # Use the base URL to generate QR code dynamically
            qr = qrcode.QRCode()
            qr.add_data(f"{base_url}/users/{national_id}")
            f = io.StringIO()
            qr.print_ascii(out=f)
            f.seek(0)
            qr_code = f.read()

            return request.render('supco.template_name',
                                  {'name': name,
                                   'dob': dob,
                                   'national_id': national_id,
                                   'department': department,
                                   'function': position,
                                   'qr_code': qr_code,
                                   'image_1920': avatar})
        else:
            return "User not found or You have no right to access."


class PublicReportController(http.Controller):

    @http.route(['/letters/public/<string:public_id>'], type='http', auth="public")
    def public_report_by_public_id(self, public_id, **kw):
        # Find the letter by public_id
        letter = request.env['supreme.court.letter'].sudo().search([('public_id', '=', public_id)], limit=1)

        # If not found, return a 404
        if not letter:
            return Response("Not Found", status=404)

        report_name = 'supco.report_supreme_court_letter_main'
        report = request.env['ir.actions.report']._get_report_from_name(report_name)

        # Use the built-in ReportController's method to fetch the report
        return ReportController().report_routes(report_name, docids=str(letter.sudo().id), converter='pdf')


