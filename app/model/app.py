import datetime

from . import db, ma

class App(db.Model):

	__tablename__ = 'app'

	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(100), nullable=False, unique=False)
	active = db.Column(db.Boolean, default=True)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())
	updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())

class AppSchema(ma.ModelSchema):
	class Meta:
		model = App