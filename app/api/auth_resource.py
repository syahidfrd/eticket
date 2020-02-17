from flask import request
from flask_restful import Resource
from marshmallow import Schema, fields, ValidationError

from app.service.auth_service import signup, signin
from app.api import api
from app.util.http_response import http_validation_error

class SignupSchema(Schema):
	name =  fields.Str(required=True)
	email = fields.Email(required=True)
	password = fields.Str(required=True)

class SigninSchema(Schema):
	email = fields.Email(required=True)
	password = fields.Str(required=True)

signup_schema = SignupSchema()
signin_schema = SigninSchema()

class SignupResource(Resource):
	def post(self):
		try:
			data = signup_schema.load(request.json)
		except ValidationError as err:
			return http_validation_error(err.messages)
		return signup(data)

class SigninResource(Resource):
	def post(self):
		try:
			data = signin_schema.load(request.json)
		except ValidationError as err:
			return http_validation_error(err.messages)
		return signin(data)

api.add_resource(SignupResource, '/auth/signup')
api.add_resource(SigninResource, '/auth/signin')