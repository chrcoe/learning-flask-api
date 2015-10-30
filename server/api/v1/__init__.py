''' Blueprint location '''
from flask import Blueprint


api_bp = Blueprint('api_bp', __name__)
api_bp.API_VERSION = '1.0'
# TODO: figure out API versioning based on blueprints
# this needs to be done after implementing Flask-RESTful


@api_bp.after_request
def additional_info(response):
    response.headers['API-Version'] = '1.0'
    return response
