import datetime

from flask_bcrypt import Bcrypt
from marshmallow import fields

from . import db, ma
from app.model.app import AppSchema

flask_bcrypt = Bcrypt()
app_schema = AppSchema()

class User(db.Model):

	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), nullable=False, unique=True)
	admin = db.Column(db.Boolean, default=True, nullable=False)
	password_hash = db.Column(db.String(100), nullable=False)
	authentication_token = db.Column(db.String(100), nullable=False, unique=True)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())
	updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())

	app_id = db.Column(db.Integer, db.ForeignKey('app.id'), nullable=False)
	app = db.relationship('App', backref='user')


	@property
	def password(self):
		raise AttributeError('password: write-only fields')

	@password.setter
	def password(self, password):
		self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

	def check_password(self, password):
		return flask_bcrypt.check_password_hash(self.password_hash, password)

class UserSchema(ma.ModelSchema):
	class Meta:
		model = User
		exclude = ("app", "password_hash")
		include_fk = True