import os
import datetime
import hashlib
import jwt
import redis

from functools import wraps
from flask import request, jsonify, abort, make_response, current_app as app

from fetch_stock_data_api.decorators import logger_gunicorn
from fetch_stock_data_api.user.service import UserService as service

from jwt import exceptions

redis_db = redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), db=os.environ.get('REDIS_DB'))


@logger_gunicorn
def save_token(login, token):
    app.logger.info('Saving token')
    redis_db.ttl(86400)  # Ttl is valid for one day
    redis_db.set(login, token)


@logger_gunicorn
def get_token(user, token):
    app.logger.info('Retrieve token')
    stored_token = redis_db.get(user.get('login'))

    if stored_token is None:
        return False

    return token == stored_token.decode("utf-8")


@logger_gunicorn
def check_auth(request):
    app.logger.info('Checking if request is authenticated')
    auth = request.get_json()

    user = service.find_by_login(auth.get('login'))

    if not user:
        abort(404)
        return dict(reasom='User not found')

    if user.get('password') != hashlib.sha224(auth.get('password').encode('utf-8')).hexdigest():
        abort(401)
        return dict(reasom='Invalid credentials', code=401)

    token = jwt.encode(dict(exp=datetime.datetime.utcnow() + datetime.timedelta(days=1), user=user),
                       'secret',
                       algorithm='HS256')
    save_token(user.get('login'), token.decode('utf-8'))

    return dict(authorized=True, token=str.format('Basic {0}', token.decode('utf-8')))


@logger_gunicorn
def check_user(request):
    token = request.headers.get('Authorization')


@logger_gunicorn
def create_user(register_request):
    return service.create(register_request)


@logger_gunicorn
def valid_token(request):
    app.logger.info('Start token validation')
    token = request.headers.get('Authorization')

    if token is None:
        return False

    token = token.split(' ')

    if len(token) != 2:
        return False

    if token[0] != 'Basic':
        return False

    if not token[1]:
        return False

    try:
        payload = jwt.decode(token[1], 'secret', algorithms=['HS256'])

        if not payload.get('user'):
            return False

    except exceptions.DecodeError:
        return False

    return get_token(payload.get('user'), token[1])


@logger_gunicorn
def unauthorized():
    """Sends a 401 response that enables basic auth"""
    return make_response(jsonify(dict(reason="Unauthorized")), 401)


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not valid_token(request):
            return unauthorized()
        return f(*args, **kwargs)

    return decorated
