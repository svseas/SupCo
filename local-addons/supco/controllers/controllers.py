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
    @http.route("/users/<string:national_id>", type="http", auth="public", website=True)
    def user_info(self, national_id):
        user = (
            request.env["res.users"]
            .sudo()
            .search([("national_id", "=", national_id)], limit=1)
        )

        if user:
            # Get the base URL from system parameters
            base_url = (
                request.env["ir.config_parameter"].sudo().get_param("web.base.url")
            )

            name = user.name
            dob = user.dob
            email = user.login
            national_id = user.national_id
            department = user.department.name
            introduction_letter = user.introduction_letter
            position = user.position
            avatar = user.image_1920.decode("utf-8") if user.image_1920 else None
            qr_image_url = f"https://api.qrserver.com/v1/create-qr-code/?data=http://{base_url}/users/{national_id}&amp;size=80x80"

            # Use the base URL to generate QR code dynamically
            qr = qrcode.QRCode()
            qr.add_data(f"{base_url}/users/{national_id}")
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="#f9f9f9")
            f = io.StringIO()
            temp = io.BytesIO()
            img.save(temp, format="png")
            qr.print_ascii(out=f)
            f.seek(0)
            qr_code = f.read()
            qr_code_image = base64.b64encode(temp.getvalue()).decode("utf-8")

            return request.render(
                "supco.template_name",
                {
                    "name": name,
                    "dob": dob,
                    "national_id": national_id,
                    "email": email,
                    "department": department,
                    "position": position,
                    "qr_code": qr_code,
                    "image_1920": avatar,
                    "qr_image_url": qr_image_url,
                    "qr_code_image": qr_code_image,
                },
            )
        else:
            return "User not found or You have no right to access."


class YourControllerNameHere(http.Controller):
    @http.route(["/letters/public/<string:public_id>"], type="http", auth="public")
    def public_report_by_public_id(self, public_id, **kw):
        _logger.info("Generating report for public_id: %s", public_id)

        # Find the letter by public_id
        letter = (
            request.env["supreme.court.letter"]
            .sudo()
            .search([("public_id", "=", public_id)], limit=1)
        )

        if not letter:
            _logger.warning("No letter found for public_id: %s", public_id)
            return Response("Not Found", status=404)

        Report = request.env["ir.actions.report"].sudo().with_context()

        # Render the report as PDF
        # try:
        #     pdf_content, _ = Report._render_qweb_pdf(
        #         "supco.report_supreme_court_letter_main", res_ids=[letter.id]
        #     )
        # except Exception as e:
        #     _logger.error(
        #         "Failed to generate report for public_id: %s, Error: %s",
        #         public_id,
        #         str(e),
        #     )
        #     return Response("Internal Server Error", status=500)
        #
        # # Set filename to something meaningful, e.g., "letter_<public_id>.pdf"
        # filename = "letter_{}.pdf".format(public_id)
        #
        # # Return the fetched PDF as a response.
        # pdfhttpheaders = [
        #     ("Content-Type", "application/pdf"),
        #     ("Content-Length", len(pdf_content)),
        #     ("Content-Disposition", content_disposition(filename)),
        # ]
        # return request.make_response(pdf_content, headers=pdfhttpheaders)

        # Render the report as HTML
        try:
            html_content = request.env['ir.actions.report']._render_qweb_html(
                'supco.report_supreme_court_letter_main', letter.ids
            )[0]
        except Exception as e:
            _logger.error(
                "Failed to generate report for public_id: %s, Error: %s",
                public_id,
                str(e),
            )
            return http.Response("Internal Server Error", status=500)

        # Return the fetched HTML as a response.
        return http.Response(html_content, content_type='text/html')
