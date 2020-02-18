from functools import wraps
from flask import request

from app.service.auth_service import get_current_user
from app.util.http_response import http_unauthorized

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		data, status = get_current_user(request)
		token = data.get("result")

		if not token:
			return data, status
		return f(*args, **kwargs)
	
	return decorated

def admin_token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		data, status = get_current_user(request)
		token = data.get("result")

		if not token:
			return data, status

		admin = token.get("admin")
		if not admin:
			return http_unauthorized('Admin token required')

		return f(*args, **kwargs)
	return decorated