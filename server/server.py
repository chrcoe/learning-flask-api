#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask_script import Manager, Shell, Server
from flask_script.commands import Clean, ShowUrls, Command
from flask_migrate import MigrateCommand

from api import create_app
from api.v1.models import User, Role, roles_users, user_datastore, Cookie
from api.v1.settings import DevConfig, ProdConfig
from api import db

if os.environ.get("API_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'api/v1/tests')

manager = Manager(app)


def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': app,
            'db': db,
            'User': User
            }


@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code


class DBCreateSampleData(Command):
    ''' Creates sample data for development. '''

    def __init__(self, db, user_datastore):
        self.db = db
        self.user_datastore = user_datastore

    def run(self):
        # add a test user
        testuser = self.user_datastore.create_user(
            email='test', password='test')
        # add a developer role
        testdevrole = self.user_datastore.create_role(
            name='developer', description='access to development APIs')
        testadminrole = self.user_datastore.create_role(
            name='admin', description='access to admin APIs')

        # assign the test user to the developer role
        self.user_datastore.add_role_to_user(testuser, testdevrole)
        # save the new user to use the allow assigning in the same function
        self.user_datastore.commit()
        # add a cookie that belongs to our testuser
        testcookie = Cookie(name='test_cookie', user_id=testuser.id)
        self.db.session.add(testcookie)
        # save everything
        self.db.session.commit()

manager.add_command('runserver', Server(host='testflask.local', port=5000))
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)  # flask-sqlalchemy
manager.add_command('urls', ShowUrls())
manager.add_command('clean', Clean())
manager.add_command('sampledata', DBCreateSampleData(db, user_datastore))

if __name__ == '__main__':
    manager.run()
