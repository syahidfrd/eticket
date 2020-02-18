import secrets

from app.model import db
from app.model.user import User, UserSchema
from app.model.app import App
from app.model.admin_app import AdminApp
from app.util.http_response import *

user_schema = UserSchema()

def signup(data):
	try:
		user = User.query.filter_by(email=data['email']).first()
		if not user:
			#Save App
			new_app = App(
				code=secrets.token_urlsafe(20)
			)
			save_changes(new_app)

			# Save User
			new_user = User(
				name=data['name'],
				email=data['email'],
				password=data['password'],
				authentication_token=secrets.token_urlsafe(20),
				app=new_app
			)
			save_changes(new_user)

			#Save Admin App
			new_admin_app = AdminApp(
				user_id=new_user.id,
				app_id=new_app.id
			)
			save_changes(new_admin_app)
			
			new_user = user_schema.dump(new_user)
			return http_status_ok(new_user)
		else:
			msg = "Email '{}' already registered".format(data['email'])
			return http_validation_error(msg)

	except Exception as err: 
		return http_internal_server_error(err)

def signin(data):
	print(data)
	try:
		user = User.query.filter_by(email=data['email']).first()
		if user and user.check_password(data['password']):
			user = user_schema.dump(user)
			return http_status_ok(user)
		else:
			return http_authentication_failed('User or password not match')
	except Exception as err:
		return http_internal_server_error(err)

def get_current_user(request):

	auth_token = request.headers.get('Authorization')

	if auth_token:
		user = User.query.filter_by(authentication_token=str(auth_token)).first()
		if user:
			user = user_schema.dump(user)
			return http_status_ok(user)
		else:
			return http_unauthorized('Provide a valid token')
	else:
		return http_unauthorized('Provide a valid token')



def save_changes(data):
	db.session.add(data)
	db.session.commit()