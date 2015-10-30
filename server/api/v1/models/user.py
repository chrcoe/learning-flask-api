''' The User model and RESTful resource go here '''
from werkzeug.security import safe_str_cmp
from api.v1.extensions import jwt


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

# TODO: replace this with a DB (would be imported from api
users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

# TODO: replace these with ORM in the functions instead of building tables here
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


@jwt.authentication_handler
def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'),
                             password.encode('utf-8')):
        return user


@jwt.identity_handler
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
