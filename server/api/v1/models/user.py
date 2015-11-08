''' The User and Roles models go here '''
from api.v1.extensions import jwt
from api.v1.extensions import db
from flask.ext.security import UserMixin, RoleMixin, SQLAlchemyUserDatastore
from flask.ext.security.utils import encrypt_password, verify_password


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class User(db.Model, UserMixin):
    ''' Uses the email as the username ... '''
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    # custom password and hashing...
    password = db.Column(db.String(50))
    password_hash = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer)

    @property
    def password(self):
        ''' do NOT allow anything read a User's password, EVER '''
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = encrypt_password(password)

    def __repr__(self):
        return '<models.User[email=%s]>' % self.email


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)


@jwt.authentication_handler
def authenticate(username, password):
    ''' Auth based on username/password. '''
    user = user_datastore.find_user(email=username)
    if user and username == user.email \
            and verify_password(password, user.password_hash):

        return user
    return None


@jwt.identity_handler
def load_identity(payload):
    ''' Load the identity requested in the payload if valid. '''
    user_id = payload['identity']
    user = user_datastore.find_user(id=user_id)
    return user
