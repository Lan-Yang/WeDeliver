"""
The flask application package.
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.uploads import UploadSet, IMAGES, configure_uploads


app = Flask(__name__)
app.config.from_object('theApp.config')

db = SQLAlchemy(app)

lm = LoginManager(app)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, (photos,))

# import FlaskWebProject.apis
import theApp.views
