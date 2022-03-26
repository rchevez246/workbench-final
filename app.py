from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Databases.db import landingdb
from Routes.ruta101b import msg

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

# register blueprints

app.register_blueprint(msg)