import datetime

from . import db, ma

class Ticket(db.Model):
	__tablename__ = "ticket"

	id = db.Column(db.Integer, primary_key=True)
	public_id = db.Column(db.String(100), nullable=False)
	subject = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(255))
	status = db.Column(db.Enum('open', 'assigned', 'resolved', name='statusticket'), nullable=False)
	priority = db.Column(db.Enum('low', 'medium', 'high', name='priorityticket'), nullable=False)
	resolved_at = db.Column(db.DateTime)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())
	updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())

	app_id = db.Column(db.Integer, db.ForeignKey('app.id'), nullable=False)
	app = db.relationship('App', backref='tickets')

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User', backref='tickets')

class TicketSchema(ma.ModelSchema):
	class Meta:
		model = Ticket
