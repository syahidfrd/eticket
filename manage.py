import os

from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from app import create_app

from app.model.user import User
from app.model.app import App

app = create_app()
manager = Manager(app)

manager.add_command('run', Server())
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()