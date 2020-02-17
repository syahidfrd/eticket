StatusOK                   = 200
StatusValidationError      = 400
StatusAuthenticationFailed = 401
StatusNotFound             = 404
StatusUnauthorized         = 403
StatusInternalServerError  = 500

def http_validation_error(error):
	return {
		'status': StatusValidationError,
		'message': 'Validation error',
		'error': error
	}, StatusValidationError

def http_internal_server_error(error):
	return {
		'status': StatusInternalServerError,
		'message': 'Internal server error',
		'error': error
	}, StatusInternalServerError

def http_unauthorized(message):
	return {
		'status': StatusUnauthorized,
		'message': message
	}, StatusUnauthorized

def http_authentication_failed(message):
	return {
		'status': StatusAuthenticationFailed,
		'message': message
	}, StatusAuthenticationFailed

def http_not_found(message):
	return {
		'status': StatusNotFound,
		'message': message
	}, StatusNotFound

def http_status_ok(payload):
	return {
		'status': StatusOK,
		'result': payload
	}, StatusOK
