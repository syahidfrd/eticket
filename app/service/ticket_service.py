import secrets
from flask import request

from app.util.http_response import *
from app.service.auth_service import get_current_user
from app.model.ticket import Ticket, TicketSchema
from app.model.user import User
from app.model import db

ticket_schema = TicketSchema()


def create_ticket(data):
	try:
		result, status = get_current_user(request)
		current_user = result['result']

		assigned = data.get('user_id')

		print(assigned)

		if not assigned:
			status = 'open'
			user_id = None
		else:
			user = User.query.filter_by(id=data['user_id'], app_id=current_user['app_id']).first()

			if not user:
				msg = "User wiith id {} not found".format(data['user_id'])
				return http_validation_error(msg)

			status = 'assigned'
			user_id = data['user_id']
		
		# Create new ticket
		new_ticket = Ticket(
			public_id=secrets.token_urlsafe(10).upper(),
			subject=data['subject'],
			description=data['description'],
			status=status,
			priority=data['priority'],
			app_id=current_user['app_id'],
			user_id=user_id
		)
		save_changes(new_ticket)
		new_ticket = ticket_schema.dump(new_ticket)
		return http_status_ok(new_ticket)

	except Exception as err:
		return http_internal_server_error(err)

def assign_ticket(data):
	try:
		result, status = get_current_user(request)
		current_user = result['result']

	except Exception as err:
		return http_internal_server_error(err)

def save_changes(data):
	db.session.add(data)
	db.session.commit()
