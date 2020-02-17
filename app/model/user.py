import datetime

from . import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), nullable=False, unique=True)
	admin = db.Column(db.Boolean, default=True, nullable=False)
	password_hash = db.Column(db.String(100), nullable=False)
	authentication_token = db.Column(db.String(100), nullable=False, unique=True)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())
	updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())
