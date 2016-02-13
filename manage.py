#!flask/bin/python
from app import app
from flask_script import Manager, Server, Shell

manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell)

@manager.command
def createdb():
    from app.models import db
    db.create_all()

manager.run()

