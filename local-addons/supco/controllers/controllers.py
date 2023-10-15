import base64
import string
from odoo import http
from odoo.http import request, route, content_disposition
import io
import qrcode
import random


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


class ReportDuplicator(http.Controller):
    @http.route('/letters/<int:id>', type='http', auth='public')
    def duplicate_report_and_qr(self, id, **kwargs):
        # Retrieve the original report record
        original_report = request.env['supco.report_supreme_court_letter_main'].browse(id)

        if not original_report:
            return "Original report not found!"

        # Duplicate the content of the report by creating a new record
        duplicated_report = original_report.copy()

        # Render the duplicated report as base64-encoded PDF
        base64_encoded_report = self._render_report(duplicated_report)

        # Generate a unique identifier (token) for the public access
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

        # Generate a URL containing the token
        qr_code_link = f'/my_module/duplicate_report/{duplicated_report.id}/{token}'

        # Generate a QR code from the token
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_code_link)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code as a base64-encoded image
        buffer = io.BytesIO()
        qr_img.save(buffer, format="PNG")
        base64_encoded_qr = base64.b64encode(buffer.getvalue()).decode()

        # Update the duplicated report's QR code field with the base64-encoded image
        duplicated_report.write({'qr_code': base64_encoded_qr})

        # Generate the PDF report using the provided snippet
        pdf, _ = self._render_qweb_pdf('sale.action_report_saleorder', [duplicated_report.id])

        # Return the base64-encoded report as a response for downloading
        pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', u'%s' % len(pdf))]
        response = request.make_response(pdf, headers=pdfhttpheaders)
        response.headers['Content-Disposition'] = f'attachment; filename=duplicated_report.pdf'
        return response

    def _render_report(self, report_record):
        # Retrieve the report template associated with the model
        report_template = report_record.get_report_template()

        # Generate the report content using Odoo's report generation mechanism
        report_service = report_template.report_name
        report_data, format = report_template.render_qweb_pdf([report_record.id])

        # Encode the report content as base64
        base64_encoded_report = base64.b64encode(report_data).decode()

        return base64_encoded_report

    def _render_qweb_pdf(self, report_name, docargs):
        pdf, _ = request.env['ir.actions.report'].sudo()._render_qweb_pdf(report_name, docargs)
        return pdf
