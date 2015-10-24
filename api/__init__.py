"""Boilerplate app to scaffold a Flask RESTful application

   This app is cookiecutter compatible boilerplate application
   that can be used to scaffold new applications.

   moduleauthor:: Chris Coe <chrcoe@ieee.org>

"""
from flask import Flask, jsonify
from flask_restful import abort
from flask.ext.sqlalchemy import SQLAlchemy
from flask_jwt import JWT

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
jwt = JWT(app)

from learning-flask-api.v1.models.user import User


@app.errorhandler(404)
def not_found(e):
    return jsonify({"message": "Resource not found."}), 404


@app.errorhandler(400)
def bad_request(e):
    return jsonify({"message": "Please check request parameters."}), 400


@app.errorhandler(401)
def unauthorized(e):
    return jsonify({"message": "User is not authorized."}), 401


@jwt.authentication_handler
def authenticate(username, password):
    return User.authenticate(username, password)


@jwt.user_handler
def load_user(payload):
    if payload['user_id']:
        return User.query.get(payload['user_id'])


# Get Blueprints from views
from .v1.views.users import user_bp

# Register version 1 blueprints
app.register_blueprint(user_bp, url_prefix='/v{api_version}/users/'.format(api_version=user_bp.API_VERSION))
