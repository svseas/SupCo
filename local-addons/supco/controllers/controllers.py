import base64
import string
import requests
import werkzeug
import re

from odoo import http
from odoo.http import request, route, content_disposition, Response
import io
import qrcode
from odoo.addons.web.controllers.main import ReportController
import logging
import os

_logger = logging.getLogger(__name__)


class UserController(http.Controller):
    @http.route("/users/<string:code>", type="http", auth="public", website=True)
    def user_code_info(self, code):
        user = request.env["res.users"].sudo().search([("code", "=", code)], limit=1)

        if user:
            # Get the base URL from system parameters
            base_url = (
                request.env["ir.config_parameter"].sudo().get_param("web.base.url")
            )

            name = user.name
            code = user.code
            dob = user.dob
            email = user.login
            national_id = user.national_id
            department = user.department.name
            introduction_letter = user.introduction_letter
            position = user.position
            avatar = user.image_1920.decode("utf-8") if user.image_1920 else None
            qr_image_url = f"https://api.qrserver.com/v1/create-qr-code/?data=http://{base_url}/users/{code}&amp;size=80x80"

            # Use the base URL to generate QR code dynamically
            qr = qrcode.QRCode()
            qr.add_data(f"{base_url}/users/{code}")
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
                    "code": code,
                    "image_1920": avatar,
                    "qr_image_url": qr_image_url,
                    "qr_code_image": qr_code_image,
                },
            )
        else:
            return "User not found or You have no right to access."

    @http.route("/nhan-vien/<string:code>", type="http", auth="public", website=True)
    def user_info(self, code):
        user = request.env["res.users"].sudo().search([("code", "=", code)], limit=1)

        if user:
            # Get the base URL from system parameters
            base_url = (
                request.env["ir.config_parameter"].sudo().get_param("web.base.url")
            )

            name = user.name
            code = user.code
            dob = user.dob
            email = user.login
            national_id = user.national_id
            department = user.department.name
            introduction_letter = user.introduction_letter
            position = user.position
            avatar = user.image_1920.decode("utf-8") if user.image_1920 else None
            qr_image_url = f"https://api.qrserver.com/v1/create-qr-code/?data=http://{base_url}/users/{code}&amp;size=80x80"

            # Use the base URL to generate QR code dynamically
            qr = qrcode.QRCode()
            qr.add_data(f"{base_url}/users/{code}")
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
                    "code": code,
                    "image_1920": avatar,
                    "qr_image_url": qr_image_url,
                    "qr_code_image": qr_code_image,
                },
            )
        else:
            return "User not found or You have no right to access."


class HttpRenderController(http.Controller):
    @route(["/letters/public/<string:public_id>"], type="http", auth="public")
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

        # Render the report as HTML
        try:
            html_content = request.env["ir.actions.report"]._render_qweb_html(
                "supco.report_supreme_court_letter_main", letter.ids
            )[0]
        except Exception as e:
            _logger.error(
                "Failed to generate report for public_id: %s, Error: %s",
                public_id,
                str(e),
            )
            return http.Response("Internal Server Error", status=500)

        # Return the fetched HTML as a response.
        return http.Response(html_content, content_type="text/html")


class PDFRenderController(http.Controller):
    @route(
        ["/letters/pdf/<string:public_id>"], type="http", auth="public", website=True
    )
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
        try:
            pdf_content, _ = Report._render_qweb_pdf(
                "supco.report_supreme_court_letter_main", res_ids=[letter.id]
            )
        except Exception as e:
            _logger.error(
                "Failed to generate report for public_id: %s, Error: %s",
                public_id,
                str(e),
            )
            return Response("Internal Server Error", status=500)

        # Set filename to something meaningful, e.g., "letter_<public_id>.pdf"
        filename = "{}.pdf".format(public_id)

        # Return the fetched PDF as a response.
        pdfhttpheaders = [
            ("Content-Type", "application/pdf"),
            ("Content-Length", len(pdf_content)),
            ("Content-Disposition", content_disposition(filename)),
        ]
        return request.make_response(pdf_content, headers=pdfhttpheaders)

    @http.route(
        ["/letters/pdf/<string:public_id>/embed"],
        type="http",
        auth="public",
        website=True,
    )
    def public_report_by_public_id_embed(self, public_id, **kw):
        # The code for serving the PDF in embed mode
        letter = (
            request.env["supreme.court.letter"]
            .sudo()
            .search([("public_id", "=", public_id)], limit=1)
        )

        if not letter:
            return Response("Not Found", status=404)

        Report = request.env["ir.actions.report"].sudo().with_context()

        try:
            pdf_content, _ = Report._render_qweb_pdf(
                "supco.report_supreme_court_letter_main", res_ids=[letter.id]
            )
        except Exception as e:
            return Response("Internal Server Error", status=500)

        filename = "{}.pdf".format(public_id)
        pdfhttpheaders = [
            ("Content-Type", "application/pdf"),
            ("Content-Length", len(pdf_content)),
            ("Content-Disposition", "inline; " + content_disposition(filename)),
        ]
        return request.make_response(pdf_content, headers=pdfhttpheaders)

    @http.route(
        ["/letters/pdf/view/<string:public_id>/"],
        type="http",
        auth="public",
        website=True,
    )
    def view_report_embedded(self, public_id, **kw):
        # Serve the HTML page with the PDF embedded
        pdf_url = "/letters/pdf/{}/embed".format(public_id)
        html_content = """
           <!DOCTYPE html>
           <html>
           <head>
               <title> Công Lý - Giấy giới thiệu </title>
           </head>
           <body style="margin:0;">
               <iframe src="{}" style="border: none; width: 100%; height: 100vh;"></iframe>
           </body>
           </html>
           """.format(pdf_url)
        return html_content

    @http.route(
        ["/letters/ggt/<string:public_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def public_report_by_public_id_embed2(self, public_id, **kw):
        # The code for serving the PDF in embed mode
        letter = (
            request.env["supreme.court.letter"]
            .sudo()
            .search([("public_id", "=", public_id)], limit=1)
        )

        if not letter:
            return Response("Not Found", status=404)

        Report = request.env["ir.actions.report"].sudo().with_context()

        try:
            pdf_content, _ = Report._render_qweb_pdf(
                "supco.report_supreme_court_letter_main", res_ids=[letter.id]
            )
            encode = base64.b64encode(pdf_content)

            html_content = (
                """
              <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Giấy giới thiệu - Báo Công Lý</title>
                <style>
                * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                }

                .loading {
                    margin-top: 20px;
                    width: 100%;
                    height: 100%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
              

                svg{
                width: 100px;
                height: 100px;
                margin: 0px;
                display:inline-block;
                }
                .pdf{
                width: 100%;
                height: 100%;
                display:flex;
                flex-direction: row;
                justify-content: center;
                align-items: start;
                overflow: scroll;
                }
               
                </style>
                </head>
                <body>
                
                <div class="body" style="width:100vw; min-height:100vh; display:flex; align-items: center;justify-content:start;background:white;flex-direction:column">
                <div class="loading">
                <svg version="1.1" id="L1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 100" enable-background="new 0 0 100 100" xml:space="preserve">
                <circle fill="none" stroke="#fff" stroke-width="6" stroke-miterlimit="15" stroke-dasharray="14.2472,14.2472" cx="50" cy="50" r="47" >
                <animateTransform 
                    attributeName="transform" 
                    attributeType="XML" 
                    type="rotate"
                    dur="5s" 
                    from="0 50 50"
                    to="360 50 50" 
                    repeatCount="indefinite" />
                </circle>
                <circle fill="none" stroke="red" stroke-width="1" stroke-miterlimit="10" stroke-dasharray="10,10" cx="50" cy="50" r="39">
                    <animateTransform 
                        attributeName="transform" 
                        attributeType="XML" 
                        type="rotate"
                        dur="5s" 
                        from="0 50 50"
                        to="-360 50 50" 
                        repeatCount="indefinite" />
                </circle>
                <g fill="red">
                <rect x="30" y="35" width="5" height="30">
                    <animateTransform 
                    attributeName="transform" 
                    dur="1s" 
                    type="translate" 
                    values="0 5 ; 0 -5; 0 5" 
                    repeatCount="indefinite" 
                    begin="0.1"/>
                </rect>
                <rect x="40" y="35" width="5" height="30" >
                    <animateTransform 
                    attributeName="transform" 
                    dur="1s" 
                    type="translate" 
                    values="0 5 ; 0 -5; 0 5" 
                    repeatCount="indefinite" 
                    begin="0.2"/>
                </rect>
                <rect x="50" y="35" width="5" height="30" >
                    <animateTransform 
                    attributeName="transform" 
                    dur="1s" 
                    type="translate" 
                    values="0 5 ; 0 -5; 0 5" 
                    repeatCount="indefinite" 
                    begin="0.3"/>
                </rect>
                <rect x="60" y="35" width="5" height="30" >
                    <animateTransform 
                    attributeName="transform" 
                    dur="1s" 
                    type="translate" 
                    values="0 5 ; 0 -5; 0 5"  
                    repeatCount="indefinite" 
                    begin="0.4"/>
                </rect>
                <rect x="70" y="35" width="5" height="30" >
                    <animateTransform 
                    attributeName="transform" 
                    dur="1s" 
                    type="translate" 
                    values="0 5 ; 0 -5; 0 5" 
                    repeatCount="indefinite" 
                    begin="0.5"/>
                </rect>
                </g>
                </svg>
                </div>
                <div class="pdf">
                                <canvas id="the-canvas"  style="overflow:scroll;">Đang tải tài liệu...</canvas>
                </div>
                </div>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js" integrity="sha512-q+4liFwdPC/bNdhUpZx6aXDx/h77yEQtn4I1slHydcbZK34nLaR3cAeYSJshoxIOq3mjEf7xJE8YWIUHMn+oCQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

                <script type="module">"""
                + f"""
                var pdfData = atob("{encode.decode("utf-8")}");
                """
                + """
                    var { pdfjsLib } = globalThis;

                    // The workerSrc property shall be specified.
                    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

                    // Using DocumentInitParameters object to load binary data.
                    var loadingTask = pdfjsLib.getDocument({data: pdfData});
                    loadingTask.promise.then(function(pdf) {
                        console.log('PDF loaded');

                        // Fetch the first page
                        var pageNumber = 1;
                        pdf.getPage(pageNumber).then(function(page) {
                        console.log('Page loaded');

                        var scale =  1.5;
                        
                        var viewport = page.getViewport({scale: scale});

                        // Prepare canvas using PDF page dimensions
                        var canvas = document.getElementById('the-canvas');
                        var context = canvas.getContext('2d')
                        canvas.height = viewport.height;
                        canvas.width = viewport.width;
                        canvas.style.display = 'block';

                        // Render PDF page into canvas context
                        var renderContext = {
                            canvasContext: context,
                            viewport: viewport
                        };
                        var renderTask = page.render(renderContext);
                        renderTask.promise.then(function () {
                            console.log('Page rendered');
                        });
                        });
                        var loading = document.querySelector('.loading');
                        loading.style.display = 'none';
                    }, function (reason) {
                        // PDF loading error
                        console.error(reason);
                    });
                </script>
                </body>
                </html>
            """
            )

            return html_content
        except Exception as e:
            return Response("Internal Server Error", status=500)


class SignedPdfLetterController(http.Controller):
    @http.route(
        "/giay-gioi-thieu/<string:public_id>", type="http", auth="public", website=True
    )
    def serve_pdf(self, public_id, **kw):
        # Retrieve the letter record by its ID
        letter = (
            request.env["supreme.court.letter"]
            .sudo()
            .search([("public_id", "=", public_id)], limit=1)
        )
        if not letter or not letter.signed_upload_file:
            return request.not_found()

        # Decode the file content from base64
        pdf_content = base64.b64decode(letter.signed_upload_file)
        pdfhttpheaders = [
            ("Content-Type", "application/pdf"),
            (
                "Content-Disposition",
                f'inline; filename="{letter.signed_upload_file_name}"',
            ),
        ]
        return request.make_response(pdf_content, headers=pdfhttpheaders)
