"""
The flask application package.
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
import boto.ses
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

ses = boto.ses.connect_to_region(
    'us-east-1',
    aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'])

#photos = UploadSet('photos', IMAGES)
#configure_uploads(app, (photos,))

import theApp.views
import theApp.api

# ses.send_email(
#     app.config['SES_SENDER_EMAIL'],
#     'WeDeliver online!',
#     'Body!',
#     ['wm19922009@gmail.com'])
