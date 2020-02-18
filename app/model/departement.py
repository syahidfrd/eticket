import datetime

from . import db, ma

class Departement(db.Model):
	__tablename__ = 'departement'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())
	updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())

class DepartementSchema(ma.ModelSchema):
	class Meta:
		model = Departement


def departement_seeder():
	db.session.query(Departement).delete()
	departement1 = Departement(id=1, name='General')
	departement2 = Departement(id=2, name='Accounting')
	db.session.add_all([departement1, departement2])
	db.session.commit()