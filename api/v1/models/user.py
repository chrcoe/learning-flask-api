import hashlib
from learning-flask-api import db
from flask_restful import abort


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(256))

    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if not user:
            abort(401, message="User is not a registered user.")
        return user if user.check_password(password) else False

    def export_data(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username
        }

    def set_password(self, password):
        self.password = hashlib.sha1(password).hexdigest()

    def check_password(self, password):
        return self.password == hashlib.sha1(password).hexdigest()

    def __unicode__(self):
        return "<User %s>" % self.username

    def __repr__(self):
        return "<User %s>" % self.username
