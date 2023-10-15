import base64
from odoo import http
from odoo.http import request, route, content_disposition
import io
import qrcode
import requests


class UserController(http.Controller):

    @http.route('/users/<string:national_id>', type='http', auth="user", website=True)
    def user_info(self, national_id):
        user = request.env['res.users'].sudo().search([('national_id', '=', national_id)], limit=1)

        if user:
            name = user.name
            dob = user.dob
            id = user.national_id
            department = user.department.name
            introduction_letter = user.introduction_letter
            position = user.function
            avatar = user.image_1920.decode("utf-8") if user.image_1920 else None
            qr = qrcode.QRCode()
            qr.add_data(f"http://localhost:8060/users/{national_id}")
            f = io.StringIO()
            qr.print_ascii(out=f)
            f.seek(0)
            qr_code = f.read()
            return request.render('supco.template_name',
                                  {'name': name,
                                   'dob': dob,
                                   'national_id': id,
                                   'department': department,
                                   'function': position,
                                   'qr_code': qr_code,
                                   'image_1920': avatar})
        else:
            return "User not found or You have no right to access."


class LetterController(http.Controller):

    @http.route('/letters/pdf/<int:letter_id>', type='http', auth="user", website=True)
    def generate_pdf(self, letter_id):
        # Fetch the letter record
        letter = http.request.env['supreme.court.letter'].browse(letter_id)

        if not letter:
            return "Letter not found!"

        # Get the report object using its complete XML ID
        report = http.request.env.ref('supco.report_supreme_court_letter_main', False)
        if not report:
            return "Report not found!"

        # Render the report to PDF
        pdf_content, content_type = report.render_qweb_pdf(letter.ids)

        # Return the rendered PDF
        return http.request.make_response(pdf_content, headers=[
            ('Content-Type', content_type),
            ('Content-Disposition', f'filename=letter_{letter_id}.pdf;'),
        ])

    @http.route('/letters/qr/<int:letter_id>', type='http', auth="user", website=True)
    def letter_qr(self, letter_id):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        report_url = f'{base_url}/report/pdf/supco.report_supreme_court_letter_main/{letter_id}'

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

        response = http.request.make_response(buffer.getvalue(), headers=[('Content-Type', 'image/png')])
        return response
