from odoo import http
from odoo.http import request
import jwt
from werkzeug.utils import redirect
import logging
import time

_logger = logging.getLogger(__name__)

roomName = 'Test'

class Auth(http.Controller):
    @http.route('/api/auth', type='json', auth='public', methods=['POST'])
    def authenticate(self, **kwargs):
        params = request.params
        login = params.get('login')
        password = params.get('password')
        

        # _logger.info(list(request.env.registry.models.keys()))
        _logger.info(f"Login: {login}")
        _logger.info(f"Password: {password}")

        uid = request.session.authenticate('odoo', login, password)

        _logger.info(f"User {login} with {uid} authenticated successfully")
        if uid is not False:
            user = request.env['res.users'].sudo().search([('id', '=', uid)])
            payload = {
                'user_id': user.id,
                'nbf': int(time.time()),
                'exp': int(time.time()) + 3600,  
                'context': {
                    "user": {
                        "name": user.name,
                        "email": user.email,
                        "avatar": user.image_1920,  
                    }
                },
                "aud":"jitsi",
                "iss":"jitsi",
                "sub":"*",
                "room": roomName,
            }
            token = jwt.encode(payload, '123456789', algorithm='HS256')
            print(f"User {user.name} authenticated successfully")
            return {"redirect": f"https://suncat.io/{roomName}?jwt={token}"}
        else:
            return {"redirect": f"https://suncat.io/{roomName}?auth_status=unauthorized"}

class Redirect(http.Controller):
    @http.route('/api/redirect', type='http', auth='public', methods=['GET'])
    def redirect(self, **kwargs):
        roomName = kwargs.get('roomName')
        return redirect(f"https://auth.suncat.io/{roomName}")