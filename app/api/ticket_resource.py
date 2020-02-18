from flask import request
from flask_restful import Resource
from marshmallow import Schema, fields, ValidationError, validate

from app.service.ticket_service import create_ticket, resolve_ticket
from app.api import api
from app.util.http_response import http_validation_error
from app.util.decorator import admin_token_required


class TicketSchema(Schema):
	subject = fields.Str(required=True)
	description = fields.Str()
	priority = fields.Str(required=True, validate=validate.OneOf(["low", "medium", "high"]))
	user_id = fields.Int()

class TicketResolveSchema(Schema):
	ticket_id = fields.Int(required=True)

ticket_schema = TicketSchema()
ticket_resolve_schema = TicketResolveSchema()


class TicketResource(Resource):
	@admin_token_required
	def post(self):
		try:
			data = ticket_schema.load(request.json)
		except ValidationError as err:
			return http_validation_error(err.messages)
		return create_ticket(data)

class TicketResolve(Resource):
	@admin_token_required
	def post(self):
		try:
			data = ticket_resolve_schema.load(request.json)
		except ValidationError as err:
			return http_validation_error(err.messages)
		return resolve_ticket(data['ticket_id'])

api.add_resource(TicketResource, '/ticket')
api.add_resource(TicketResolve, '/ticket/resolve')