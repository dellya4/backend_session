from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    wishes = db.relationship('Wish', foreign_keys='[Wish.user_id]', backref='user', lazy=True)
    reserved_wishes = db.relationship('Wish', back_populates='reserved_by', foreign_keys='[Wish.reserved_by_id]')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Wish(db.Model):
    __tablename__ = 'wish'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    amount = db.Column(db.Float)
    category = db.Column(db.String(128))
    reserved = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reserved_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reserved_by = db.relationship('User', back_populates='reserved_wishes', foreign_keys=[reserved_by_id])
