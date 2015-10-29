# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask  # , render_template


from api.settings import ProdConfig
#  from api.assets import assets
from api.extensions import (
    jwt,  # flask-jwt
    #  bcrypt,  # flask-bcrypt
    #  cache,  # flask-cache
    #  db,  # flask-sqlalchemy
    #  login_manager,  # flask-login
    #  migrate,  # flask-migrate
    #  debug_toolbar,  # flask-debug toolbar
)
#  from api import public, user # won't use these since its an API with no
#  views...


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    #  register_blueprints(app)
    #  register_errorhandlers(app)
    return app


def register_extensions(app):
    jwt.init_app(app)
    #  setup_test(app)
    #  assets.init_app(app)
    #  bcrypt.init_app(app)
    #  cache.init_app(app)
    #  db.init_app(app)
    #  login_manager.init_app(app)
    #  debug_toolbar.init_app(app)
    #  migrate.init_app(app, db)
    return None


#  def register_blueprints(app):
    #  app.register_blueprint(public.views.blueprint)
    #  app.register_blueprint(user.views.blueprint)
    #  return None


#  def register_errorhandlers(app):
    #  def render_error(error):
    #  # If a HTTPException, pull the `code` attribute; default to 500
    #  error_code = getattr(error, 'code', 500)
    #  return render_template("{0}.html".format(error_code)), error_code
    #  for errcode in [401, 404, 500]:
    #  app.errorhandler(errcode)(render_error)
    #  return None

class User(object):
    # TODO: replace this with ORM model (Flask-Security's user/role setup)

    def __init__(self, id, username, password,
                 first_name=None, last_name=None):
        self.id = id
        self.username = username
        # TODO: obviously when building this out, should never allow the PW to
        # be set directly
        self.password = password

    def __repr__(self):
        return str(self)

    def __str__(self):
        # TODO: never want to make the password visible
        attrs = vars(self)
        return '<User: {' + \
            ', '.join("%s: %s" % item for item in attrs.items()) + '}>'


def setup_test(app):
    # TODO: replace this with a DB
    users = [
        User(1, 'user1', 'abcxyz'),
        User(2, 'user2', 'abcxyz'),
    ]

    # TODO: replace these with ORM in the functions instead of building tables
    # here
    username_table = {u.username: u for u in users}
    userid_table = {u.id: u for u in users}

    from werkzeug.security import safe_str_cmp
    from flask_jwt import JWT

    def authenticate(username, password):
        user = username_table.get(username, None)
        if user and safe_str_cmp(user.password.encode('utf-8'),
                                 password.encode('utf-8')):
            return user

    def identity(payload):
        user_id = payload['identity']
        return userid_table.get(user_id, None)

    jwt = JWT(app, authenticate, identity)
