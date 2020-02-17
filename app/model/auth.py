from marshmallow import fields

from . import ma

class SignupSchema(ma.Schema):
	name = fields.Str()
	email = fields.Str()
	password = fields.Str()