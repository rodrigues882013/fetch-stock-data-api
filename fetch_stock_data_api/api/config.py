# -*- coding: utf-8 -*-

import os

INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')


class BaseConfig(object):

    PROJECT = "fetch_stock_data_api"

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = False

    ADMINS = ['youremail@yourdomain.com']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'secret key'

    LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'


class DefaultConfig(BaseConfig):

    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    if 'DEV' not in os.environ:
        user = os.environ.get('POSTGRES_USER')
        pwd = os.environ.get('POSTGRES_PASSWORD')
        schema = os.environ.get('POSTGRES_DB')
        host = os.environ.get('POSTGRES_HOST')
        port = os.environ.get('POSTGRES_PORT')
        SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (user, pwd, host, port, schema)

    YAHOO_FINANACE_URL = os.environ.get('YAHOO_FINANACE_URL')


class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'