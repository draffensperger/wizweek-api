# Code taken from:
# http://flask.pocoo.org/snippets/125/

from httplib2 import Http
import json
from flask import *

def validate_token(access_token):
    '''Verifies that an access-token is valid.
    Returns None on fail, and an e-mail on success'''
    h = Http()
    resp, cont = h.request("https://www.googleapis.com/oauth2/v2/userinfo",
                           headers={'Host': 'www.googleapis.com',
                                    'Authorization': access_token})

    if not resp['status'] == '200':
        return None

    # This expects it to be run in Python 3 where cont is bytes
    data = json.loads(cont.decode())
    return data['email']

def google_authorized(fn):
    """Decorator that checks that requests
    contain an id-token in the request header.
    user_email will be None if the
    authentication failed, and have an id otherwise.

    Usage:
    @app.route("/")
    @google_authorized
    def secured_root(user_email=None):
        pass
    """

    def _wrap(*args, **kwargs):
        if 'Authorization' not in request.headers:
            # Unauthorized
            abort(401)
            return None

        user_email = validate_token(request.headers['Authorization'])
        if user_email is None:
            # Unauthorized
            abort(401)
            return None

        return fn(user_email=user_email, *args, **kwargs)
    return _wrap
