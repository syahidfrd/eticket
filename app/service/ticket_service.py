import secrets
import datetime

from flask import request

from app.util.http_response import *
from app.service.auth_service import get_current_user
from app.model.ticket import Ticket, TicketSchema
from app.model.user import User
from app.model import db
from app.model.admin_app import AdminApp

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

def resolve_ticket(ticket_id):
	try:
		result, status = get_current_user(request)
		current_user = result['result']

		admin_app = AdminApp.query.filter_by(user_id=current_user['id'], app_id=current_user['app_id']).first()
		print(admin_app)
		if not admin_app:
			return http_unauthorized('Unaithorized!')
		else:
			ticket = Ticket.query.filter_by(id=ticket_id).first()
			print(ticket)
			if not ticket:
				msg = "Ticket with id {} not found".format(ticket_id)
				return http_not_found(msg)
			else:
				ticket.status = "resolved"
				ticket.resolved_at = datetime.datetime.now()
				save_changes(ticket)
				return http_status_ok('Ticket successfully resolved')
	except Exception as err:
		return http_internal_server_error(err)

def save_changes(data):
	db.session.add(data)
	db.session.commit()
