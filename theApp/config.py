"""
Constants config variables
"""
from urllib import quote_plus as enc
import os


## Deployment
# SERVER_NAME = 'localhost:5555'
APP_DIR = os.path.realpath(os.path.dirname(__file__))
DEBUG = True
WTF_CSRF_ENABLED = False  # disable CSRF for easy develop...
SECRET_KEY = r'nc29q@e!8ryf=89qri&nfvfan-03y9012'

## Database
SQLALCHEMY_DATABASE_URI = r'postgresql+pg8000://groupdelivery:letitgogo@groupdelivery.cqa4mceiolu6.us-east-1.rds.amazonaws.com:5432/groupdelivery'
# DATABASE_FILE = 'test.db'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE

## Photo Upload
# UPLOADED_PHOTOS_DEST = os.path.join(APP_DIR, 'static', 'upload')
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
