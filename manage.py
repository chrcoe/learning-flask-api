import os
import sys

# Set a basepath
basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(basepath)

from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from api import app, db


migrate = Migrate(app, db)
manager = Manager(app)


# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0')
)

# Add Database migrations support
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()
