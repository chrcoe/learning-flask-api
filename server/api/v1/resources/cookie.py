''' API Resource for Cookie model. '''

from flask_restful import reqparse, fields, marshal_with
from flask_jwt import jwt_required
from api.v1.models import Cookie
from api.v1.extensions import db

# This will be used to marshal output for users
COOKIE_FIELDS = {
    'cookie_name': fields.String,
    'cookie_recipe_url': fields.String,
    'quantity': fields.Integer,
    'uri': fields.Url('cookie', absolute=True)
}


class CookieListAPI(Resource):
    '''
    This handles listing collections.
    GET api.[domain]/v1.0/cookies for reading all cookies
    POST api.[domain]/v1.0/cookies for creates
    '''

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('cookie_name', type=str, location='json')
        self.reqparse.add_argument(
            'cookie_recipe_url', type=str, location='json')
        self.reqparse.add_argument('quantity', type=int, location='json')
        super(CookieListAPI, self).__init__()

    @marshal_with(COOKIE_FIELDS, envelope="cookies")
    @jwt_required()
    def get(self):
        return Cookie.query.all()

    @marshal_with(COOKIE_FIELDS, envelope="cookie")
    @jwt_required()
    def post(self):
        args = self.reqparse.parse_args()
        cookie = Cookie(
            cookie_name=args['cookie_name'],
            cookie_recipe_url=args['cookie_recipe_url'],
            quantity=args['quantity']
        )
        db.session.add(cookie)
        db.session.commit()
        return cookie


class CookieAPI(Resource):
    '''
    Handles single resource operations
    GET api.[domain]/v1.0/cookies/<int:cookie_id> for reads
    PUT api.[domain]/v1.0/cookies/<int:cookie_id> for updates
    DELETE api.[domain]/v1.0/cookies/<int:cookie_id> for deletes
    '''

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('cookie_name', type=str, location='json')
        self.reqparse.add_argument(
            'cookie_recipe_url', type=str, location='json')
        self.reqparse.add_argument('quantity', type=int, location='json')
        super(CookieAPI, self).__init__()

    @marshal_with(COOKIE_FIELDS, envelope='cookie')
    @jwt_required()
    def get(self, cookie_id):
        return Cookie.query.get_or_404(cookie_id)

    @marshal_with(COOKIE_FIELDS, envelope='cookie')
    @jwt_required()
    def put(self, cookie_id):
        cookie = Cookie.query.get_or_404(cookie_id)
        args = self.reqparse.parse_args()
        if args['cookie_name']:
            cookie.cookie_name = args['cookie_name']
        if args['cookie_recipe_url']:
            cookie.cookie_recipe_url = args['cookie_recipe_url']
        if args['quantity']:
            cookie.quantity = args['quantity']
        db.session.commit()
        return cookie

    @jwt_required()
    def delete(self, cookie_id):
        db.session.delete(Cookie.query.get_or_404(cookie_id))
        db.session.commit()
        return {'result': True}
