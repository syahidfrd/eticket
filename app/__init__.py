import os

from flask import Flask
from flask_migrate import Migrate

from app.config import ProdConfig, DevConfig
from app.api import api_blueprint
from app.model import db, ma

migrate = Migrate()

if os.getenv("FALSK_ENV") == "prod":
	DefaultConfig = ProdConfig
else:
	DefaultConfig = DevConfig

def create_app(config_object=DefaultConfig):
	app = Flask(__name__)
	app.config.from_object(config_object)
	register_extensions(app)
	register_blueprints(app)

	return app


def register_extensions(app):
	db.init_app(app)
	ma.init_app(app)
	migrate.init_app(app, db)


def register_blueprints(app):
	app.register_blueprint(api_blueprint)
