import secrets

from flask import request

from app.model.agent import Agent, AgentSchema
from app.model.departement import Departement
from app.model.user import User
from app.model import db
from app.util.http_response import *
from app.service.auth_service import get_current_user

agent_schema = AgentSchema()

def create_agent(data):
	try:
		result, status = get_current_user(request)
		current_user = result['result']

		user = User.query.filter_by(email=data['email']).first()
		if not user:
			departement = Departement.query.filter_by(id=data['departement_id']).first()
			if not departement:
				msg = "Departement id {} not found".format(data['departement_id'])
				return http_validation_error(msg)
			else:
				new_user = User(
					name=data['name'],
					email=data['email'],
					admin=False,
					password=data['password'],
					authentication_token=secrets.token_urlsafe(20),
					app_id=current_user['app_id']
				)
				save_changes(new_user)

				new_agent = Agent(
					user_id=new_user.id,
					app_id=current_user['app_id'],
					departement_id=data['departement_id']
				)
				save_changes(new_agent)
				new_agent = agent_schema.dump(new_agent)

				return http_status_ok(new_agent)
		else:
			msg = "Email '{}' already registered".format(data['email'])
			return http_validation_error(msg)

	except Exception as err:
		return http_internal_server_error(err)

def save_changes(data):
	db.session.add(data)
	db.session.commit()
