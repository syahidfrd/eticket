import os

postgres_url = 'postgres://postgres@localhost:5432/e_ticket'
postgres_test_url = 'postgres://postgres@localhost:5432/e_ticket_test'

class Config:
	SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
	DEBUG = False

class DevConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = postgres_url
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
	DEBUG = True
	TESTING = True
	SQLALCHEMY_DATABASE_URI = postgres_test_url
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')