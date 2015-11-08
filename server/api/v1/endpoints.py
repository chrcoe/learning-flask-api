''' All API endpoints go here '''
from flask_jwt import jwt_required, current_identity
from flask_security.decorators import roles_required, auth_token_required
#  from flask_principal import Permission, RoleNeed

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
        ''' sample protected function which just returns
        the identity of the caller. '''
        return '%s' % current_identity

    #  admin_permission = Permission(RoleNeed('admin'))


    @app.route('/admin', methods=['GET'])
    #  @admin_permission.require()
    @roles_required('admin')
    @auth_token_required
    def protected_dev():
        ''' sample protected function which just returns
        the identity of the caller. '''
        return '%s' % current_identity
