import base64
import string
import requests
from odoo import http
from odoo.http import request, route, content_disposition, Response
import io
import qrcode
from odoo.addons.web.controllers.main import ReportController
import logging

_logger = logging.getLogger(__name__)


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
            position = user.position
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
                                   'position': position,
                                   'qr_code': qr_code,
                                   'image_1920': avatar})
        else:
            return "User not found or You have no right to access."


class YourControllerNameHere(http.Controller):

    @http.route(['/letters/public/<string:public_id>'], type='http', auth="public")
    def public_report_by_public_id(self, public_id, **kw):
        _logger.info("Generating report for public_id: %s", public_id)

        # Find the letter by public_id
        letter = request.env['supreme.court.letter'].sudo().search([('public_id', '=', public_id)], limit=1)

        if not letter:
            _logger.warning("No letter found for public_id: %s", public_id)
            return Response("Not Found", status=404)

        Report = request.env['ir.actions.report'].sudo().with_context()

        # Render the report as PDF
        try:
            pdf_content, _ = Report._render_qweb_pdf('supco.report_supreme_court_letter_main', res_ids=[letter.id])
        except Exception as e:
            _logger.error("Failed to generate report for public_id: %s, Error: %s", public_id, str(e))
            return Response("Internal Server Error", status=500)

        # Set filename to something meaningful, e.g., "letter_<public_id>.pdf"
        filename = "letter_{}.pdf".format(public_id)

        # Return the fetched PDF as a response.
        pdfhttpheaders = [
            ('Content-Type', 'application/pdf'),
            ('Content-Length', len(pdf_content)),
            ('Content-Disposition', content_disposition(filename))
        ]
        return request.make_response(pdf_content, headers=pdfhttpheaders)