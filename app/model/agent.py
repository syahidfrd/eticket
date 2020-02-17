import datetime

from . import db, ma

class Agent(db.Model):
	__tablename__ = 'agent'

	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())
	updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user = db.relationship('User', backref='agent')

	app_id = db.Column(db.Integer, db.ForeignKey('app.id'), nullable=False)
	app = db.relationship('App', backref='agents')

	departement_id = db.Column(db.Integer, db.ForeignKey('departement.id'), nullable=False)
	departement = db.relationship('Departement', backref='agents')

class AgentSchema(ma.ModelSchema):
	class Meta:
		model = Agent