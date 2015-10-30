# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""

#  from flask_bcrypt import Bcrypt
#  bcrypt = Bcrypt()

#  from flask_login import LoginManager
#  login_manager = LoginManager()

#  from flask_sqlalchemy import SQLAlchemy
#  db = SQLAlchemy()

#  from flask_migrate import Migrate
#  migrate = Migrate()

#  from flask_cache import Cache
#  cache = Cache()

#  from flask_debugtoolbar import DebugToolbarExtension
#  debug_toolbar = DebugToolbarExtension()

from flask_jwt import JWT
jwt = JWT()
#  have to import these to set the authentication_handler and identity_handler
#  right away, but to prevent circular import, this import has to be run AFTER
#  jwt is instantiated
from api.v1.models import authenticate, identity
