import json
import hashlib
from flask import Blueprint, request, url_for
from flask_restful import Api, Resource, abort
from flask_restful import reqparse, fields, marshal_with
from flask_jwt import jwt_required
from learning-flask-api.v1.models.user import User
from learning-flask-api import db


user_bp = Blueprint('user_bp', __name__)
user_api = Api(user_bp)
user_bp.API_VERSION = '1.0'


@user_bp.after_request
def additional_info(response):
    response.headers['API-Version'] = '1.0'
    if request.method in ['GET', 'HEAD']:
        response.headers['ETag'] = hashlib.sha1(json.dumps(response.data)).hexdigest()
    return response


# By default parse returns the first error caught.
# Setting bundle_errors property to true to get all the errors.
user_parser = reqparse.RequestParser(bundle_errors=True)
user_parser.add_argument('first_name', type=str, required=True, help="User's First Name")
user_parser.add_argument('last_name', type=str, required=True, help="User's Last Name")
user_parser.add_argument('username', type=str, required=True, help="Choose a username. It needs to be unique.")
user_parser.add_argument('password', type=str, required=True, help="Choose a password")


# This will be used to marshal output for users
user_fields = {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'username': fields.String,
    'location': fields.Url('user_bp.user_detail', absolute=True)
}


class UserListResource(Resource):
    """
    This is API endpoint resource for `users` as collection.
    All operations performed here will be for the `users collection`.
    """

    @marshal_with(user_fields)
    @jwt_required()
    def get(self, id=None):
        return User.query.all()

    @marshal_with(user_fields)
    def post(self):
        args = user_parser.parse_args()
        user = User(first_name=args.first_name, last_name=args.last_name, username=args.username)
        user.set_password(args.password)
        db.session.add(user)
        db.session.commit()
        user_url = fields.Url('user_bp.user_detail', absolute=True)
        user_url = user_url.output(user_url.endpoint, {"username": user.username})
        return user, 201, {"Location": user_url}


class UserDetailResource(Resource):

    @marshal_with(user_fields)
    @jwt_required()
    def get(self, username=None):
        if username:
            return User.query.filter_by(username=username).first()

    @jwt_required
    def patch(self, id):
        user = User.query.get(id)
        if not user:
            abort(404, message="User does not exist")
        return {"patch": "Implementation pending"}, 501


user_api.add_resource(UserListResource, '/', endpoint='user_list')
user_api.add_resource(UserDetailResource, '<username>', endpoint='user_detail')
