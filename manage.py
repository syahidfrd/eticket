import os

from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from app import create_app

from app.model.app import App
from app.model.user import User
from app.model.departement import Departement, departement_seeder
from app.model.agent import Agent

app = create_app()
manager = Manager(app)

manager.add_command('run', Server())
manager.add_command('db', MigrateCommand)

@manager.command
def seed():
	departement_seeder()
	print('Seeder data successfully...')

if __name__ == '__main__':
    manager.run()