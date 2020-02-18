from . import db, ma

class AdminApp(db.Model):
	__tablename__ = 'admin_app'

	id = db.Column(db.Integer, primary_key=True)
	
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	app_id = db.Column(db.Integer, db.ForeignKey('app.id'), nullable=False)

	def __repr__(self):
		return "<AdminApp user_id: {}, app_id: {}>".format(self.user_id, self.app_id)

class AdminAppSchema(ma.ModelSchema):
	class Meta:
		model = AdminApp
