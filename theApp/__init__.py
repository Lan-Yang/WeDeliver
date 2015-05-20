"""
The flask application package.
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
#from flask.ext.uploads import UploadSet, IMAGES, configure_uploads


class CustomFlask(Flask):
    ''' Prevent collision with AngularJS '''
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='{[',
        variable_end_string=']}',
    ))

app = CustomFlask(__name__)
app.config.from_object('theApp.config')

db = SQLAlchemy(app)

lm = LoginManager(app)

#photos = UploadSet('photos', IMAGES)
#configure_uploads(app, (photos,))

import theApp.views
import theApp.api
