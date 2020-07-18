from functools import wraps
import logging

from flask import current_app as app


def logger_gunicorn(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

        return f(*args, **kwargs)

    return decorated
