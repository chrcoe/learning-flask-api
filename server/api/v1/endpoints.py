''' All API endpoints go here '''
from flask_jwt import jwt_required, current_identity


def init_endpoints(app):
    ''' Sets up all endpoints for the API. '''
    # currently these are NOT RESTful resources from Flask-RESTful
    # just a sampling of endpoints

    #  @app.route('/protected', methods=['GET'], subdomain='api')
    #  @app.route('/protected', subdomain='api')
    @app.route('/protected')
    #  @limit(requests=10, window=60, by="ip")
    @jwt_required()
    def protected():
        ''' sample protected function '''
        return '%s' % current_identity
