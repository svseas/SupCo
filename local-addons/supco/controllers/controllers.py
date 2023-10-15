import base64
from odoo import http
from odoo.http import request, route, content_disposition
import io
import qrcode
import requests
from datetime import datetime


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


class LetterController(http.Controller):

    @http.route('/letters/qr/<int:letter_id>', type='http', auth="public", website=True)
    def letter_qr(self, letter_id):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        report_url = f'{base_url}/report/pdf/supco.report_supreme_court_letter_main/{letter_id}'

        # Extract the token from the query parameters
        token = request.httprequest.args.get('token')

        # Validate the token
        if not self.is_valid_token(token):
            return "Access denied: Invalid or expired token"

        response = requests.get(report_url, headers={
            'Cookie': 'session_id=%s' % http.request.session.sid,
        })

        if response.status_code != 200:
            return "Failed to fetch report content!"

        encoded_content = base64.b64encode(response.content).decode("utf-8")

        # Generate QR code from the encoded content
        img = qrcode.make(encoded_content)
        buffer = io.BytesIO()
        img.save(buffer, "PNG")
        buffer.seek(0)

        filename = f"letter_{letter_id}.png"

        # Update response headers to force a download prompt
        headers = [
            ('Content-Type', 'image/png'),
            ('Content-Disposition', content_disposition(filename))
        ]

        return http.request.make_response(buffer.getvalue(), headers=headers)

    def is_valid_token(self, token):
        # Validate the token against the access.token model
        access_token = http.request.env['access.token'].sudo().search([('token', '=', token)], limit=1)

        if access_token and access_token.expiration_date >= datetime.now():
            return True  # Token is valid and not expired
        else:
            return False  # Token is invalid or expired

    @http.route('/letters/qr_code/<int:letter_id>', type='http', auth="public", website=True)
    def get_qr_code(self, letter_id):
        # Fetch the letter's QR code from the database
        letter = http.request.env['supreme.court.letter'].sudo().browse(letter_id)
        if not letter:
            return "Letter not found!"

        qr_code_data = base64.b64decode(letter.qr_code) if letter.qr_code else None
        if not qr_code_data:
            return "QR Code not available!"

        return http.request.make_response(qr_code_data, headers=[('Content-Type', 'image/png')])