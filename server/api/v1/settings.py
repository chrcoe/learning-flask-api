# -*- coding: utf-8 -*-
import os

os_env = os.environ


class Config(object):
    SECRET_KEY = 'super-secret'
    #  SECRET_KEY = os_env.get('API_SECRET', 'secret-key')  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    #  BCRYPT_LOG_ROUNDS = 13
    #  ASSETS_DEBUG = False
    #  DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    #  DEBUG_TB_INTERCEPT_REDIRECTS = False
    #  CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    JWT_AUTH_URL_RULE = '/auth/token'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = 'not used with pbkdf2_sha512'
    SECURITY_UNAUTHORIZED_VIEW = None # instead of returning a view, return a 403
    SECURITY_LOGIN_URL = '/login' # need to change this to use different front end


class ProdConfig(Config):
    """Production configuration."""
    #  ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'  # TODO: Change
    #  DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class DevConfig(Config):
    """Development configuration."""
    #  ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    #  DEBUG_TB_ENABLED = True
    #  ASSETS_DEBUG = True  # Don't bundle/minify static assets
    #  CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    #  SQLALCHEMY_DATABASE_URI = 'sqlite://'
    #  BCRYPT_LOG_ROUNDS = 1  # For faster tests
    #  WTF_CSRF_ENABLED = False  # Allows form testing
