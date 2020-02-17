from flask import request
from flask_restful import Resource
from marshmallow import Schema, fields, ValidationError

from app.service.auth_service import signup
from app.api import api
from app.util.http_response import http_validation_error

class SignupSchema(Schema):
	name =  fields.Str(required=True)
	email = fields.Str()
	password = fields.Str()

signup_schema = SignupSchema()

class SignupResource(Resource):
	def post(self):
		try:
			data = signup_schema.load(request.json)
		except ValidationError as err:
			return http_validation_error(err.messages)
		return signup(data)

api.add_resource(SignupResource, '/auth/signup')