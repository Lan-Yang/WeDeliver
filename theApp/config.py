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

## Admin
ADMIN_USER = 'root'
ADMIN_PSWD = 'root2015'

## Database
# DB_STR = """
#     Driver={SQL Server Native Client 11.0};
#     Server=tcp:n51h3xigeq.database.windows.net,1433;
#     Database=wesublease;Uid=wesublease@n51h3xigeq;
#     Pwd=WeSub%2015;Encrypt=yes;Connection Timeout=30;"""
db_pwd = r'WeSub%2015'
db_driver = r'SQL Server Native Client 11.0'
sqlachemy_uri = r'mssql+pyodbc://wesublease:%s@n51h3xigeq.database.windows.net/wesublease?driver=%s'
# SQLALCHEMY_DATABASE_URI = sqlachemy_uri % (enc(db_pwd), enc(db_driver))
DATABASE_FILE = 'test.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE

## Photo Upload
UPLOADED_PHOTOS_DEST = os.path.join(APP_DIR, 'static', 'upload')
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
