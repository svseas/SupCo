import base64
from odoo import http
from odoo.http import request, route, content_disposition
import io
import qrcode
import requests


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
        # Fetch the letter
        letter = http.request.env['supreme.court.letter'].sudo().browse(letter_id)
        if not letter:
            return "Letter not found!"

        # Generate QR code from the letter content
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(letter.content)  # Replace with the actual field containing your letter content
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        qr_code_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

        # Save the QR code data in the letter record
        letter.write({'qr_code': qr_code_data})

        # Now you can generate and store the QR code without authentication
        return "QR Code generated and stored successfully!"

    @http.route('/letters/qr_code/<int:letter_id>', type='http', auth="public", website=True, csrf=False)
    def get_qr_code(self, letter_id):
        # Fetch the letter
        letter = http.request.env['supreme.court.letter'].sudo().browse(letter_id)
        if not letter:
            return "Letter not found!"

        qr_code_data = letter.qr_code
        if not qr_code_data:
            return "QR Code not available!"

        return http.request.make_response(qr_code_data, headers=[('Content-Type', 'image/png')])

