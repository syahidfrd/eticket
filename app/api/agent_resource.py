from flask import request
from flask_restful import Resource
from marshmallow import Schema, fields, ValidationError

from app.service.agent_service import create_agent
from app.api import api
from app.util.http_response import http_validation_error
from app.util.decorator import admin_token_required

class AgentSchema(Schema):
	name = fields.Str(required=True)
	email = fields.Email(required=True)
	password = fields.Str(required=True)
	departement_id = fields.Int(required=True)

agent_schema = AgentSchema()

class AgentResource(Resource):
	@admin_token_required
	def post(self):
		try:
			data = agent_schema.load(request.json)
		except ValidationError as err:
			return http_validation_error(err.messages)
		return create_agent(data)

api.add_resource(AgentResource, '/agent')