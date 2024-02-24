from odoo import http
from odoo.http import request
import jwt
from werkzeug.utils import redirect
import logging
import time

_logger = logging.getLogger(__name__)

class Auth(http.Controller):
    @http.route('/api/auth', type='json', auth='public', methods=['POST'])
    def authenticate(self, **kwargs):

        login = kwargs.get('login')
        password = kwargs.get('password')

        _logger.info(f"Login: {login}")
        _logger.info(f"Password: {password}")

        uid = request.session.authenticate('odoo', login, password)

        if uid is not False:
            user = request.env['res.users'].sudo().search([('id', '=', uid)])
            current_time = int(time.time())
            payload = {
                'context': {
                    "user": {
                        "id": user.login,  
                        "name": user.name,
                        "email": user.email,
                    }
                },
                "aud": "jitsi",
                "iss": "jitsi",
                "nbf": current_time,
                "exp": current_time + 3600,
                "iat": current_time
            }
            jwt_secret = 'CongLy@123!@#'
            _logger.info(f"JWT Secret: {jwt_secret}")
            _logger.info(f"Payload: {payload}")
            token = jwt.encode(payload, jwt_secret, algorithm='HS256')
            _logger.info(f"User {user.name} authenticated successfully")
            return {
                "jwt": token
            }
        else:
            return {
                "error": "Unauthorized access",
                "message": "You are not authorized to access this resource",
                "status": 403
            }