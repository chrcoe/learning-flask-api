# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask  # , render_template


from api.v1.settings import ProdConfig
#  from api.assets import assets
from api.v1.extensions import (
    jwt,  # flask-jwt
    #  bcrypt,  # flask-bcrypt
    #  cache,  # flask-cache
    #  db,  # flask-sqlalchemy
    #  login_manager,  # flask-login
    #  migrate,  # flask-migrate
    #  debug_toolbar,  # flask-debug toolbar
)
from api.v1 import endpoints
from api.v1 import api_bp
#  from api import public, user # won't use these since its an API ONLY


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.url_map.default_subdomain = 'api'
    register_extensions(app)
    #  register_blueprints(app)
    #  register_errorhandlers(app)
    return app


def register_extensions(app):
    jwt.init_app(app)
    endpoints.init_endpoints(app)
    #  setup_test(app)
    #  assets.init_app(app)
    #  bcrypt.init_app(app)
    #  cache.init_app(app)
    #  db.init_app(app)
    #  login_manager.init_app(app)
    #  debug_toolbar.init_app(app)
    #  migrate.init_app(app, db)
    return None


def register_blueprints(app):
    # TODO: figure out blueprints for API
    app.register_blueprints(api_bp, url_prefix='/v1.0')
    #  app.register_blueprint(public.views.blueprint)
    #  app.register_blueprint(user.views.blueprint)
    return None


#  def register_errorhandlers(app):
    #  def render_error(error):
    #  # If a HTTPException, pull the `code` attribute; default to 500
    #  error_code = getattr(error, 'code', 500)
    #  return render_template("{0}.html".format(error_code)), error_code
    #  for errcode in [401, 404, 500]:
    #  app.errorhandler(errcode)(render_error)
    #  return None
