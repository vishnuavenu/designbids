from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from app import configuration

app = Flask(__name__)

# adding bootstrap
Bootstrap(app)
# adding runtime configuration
app.config.from_object(configuration.Configuration)
# add SQLAlchemy Orm
db = SQLAlchemy(app)
# Precautions in order to avoid cyclic - redundancy
from app import views
