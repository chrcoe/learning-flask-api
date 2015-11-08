from api.v1.extensions import db
from . import User


class Cookie(db.Model):
    __tablename__ = 'cookies'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), index=True)
    recipe_url = db.Column(db.String(255))
    quantity = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship(User, lazy='joined', join_depth=1, viewonly=True)
