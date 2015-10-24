import os

basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basepath, 'dev.db')
SECRET_KEY = 'Your Secret Key!!!'
JWT_AUTH_URL = '/auth/token'
