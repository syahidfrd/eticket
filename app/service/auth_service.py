import secrets

from app.model import db
from app.model.user import User, UserSchema
from app.model.app import App
from app.util.http_response import *

user_schema = UserSchema()

def signup(data):
	try:
		user = User.query.filter_by(email=data['email']).first()
		if not user:
			new_app = App(
				code=secrets.token_urlsafe(20)
			)
			save_changes(new_app)

			new_user = User(
				name=data['name'],
				email=data['email'],
				password=data['password'],
				authentication_token=secrets.token_urlsafe(20),
				app=new_app
			)
			save_changes(new_user)
			new_user = user_schema.dump(new_user)
			return http_status_ok(new_user)
		else:
			msg = "Email '{}' already registered".format(data['email'])
			return http_validation_error(msg)

	except Exception as err: 
		return http_internal_server_error(err)

def save_changes(data):
	db.session.add(data)
	db.session.commit()