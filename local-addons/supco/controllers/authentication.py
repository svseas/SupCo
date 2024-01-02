from odoo import http
from odoo.http import request
import jwt
from werkzeug.utils import redirect
import logging

_logger = logging.getLogger(__name__)

roomName = 'Test'

class Auth(http.Controller):
    @http.route('/api/auth', type='json', auth='public', methods=['POST'])
    def authenticate(self, **kwargs):
        params = request.params
        login = params.get('login')
        password = params.get('password')

        uid = request.session.authenticate('postgres', login, password)
        _logger.info(f"User {login} with {uid} authenticated successfully")
        if uid is not False:
            user = request.env['res.users'].sudo().search([('id', '=', uid)])
            token = jwt.encode({'user_id': user.id}, '123456789', algorithm='HS256')
            print(f"User {user.name} authenticated successfully")
            return http.redirect(f"https://suncat.io/{roomName}?jwt={token}")
        else:
            return http.redirect(f"https://suncat.io/{roomName}?auth_status=unauthorized")

class Redirect(http.Controller):
    @http.route('/api/redirect', type='http', auth='public', methods=['GET'])
    def redirect(self, **kwargs):
        roomName = kwargs.get('roomName')
        return redirect(f"https://auth.suncat.io/{roomName}")