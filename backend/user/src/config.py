from os import urandom 

DEBUG = True
SECRET_KEY = urandom(24)
SQLALCHEMY_DATABASE_URI = 'mysql://root:gui123@pizzaria-mysql:3306/pizzaria?auth_plugin=mysql_native_password&autocommit=true'
SQLALCHEMY_ECHO = True
CORS_HEADERS = 'Content-Type'
