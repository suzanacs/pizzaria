from os import urandom
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Usuario(db.Model):

    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, nullable=False)
    dtNasc = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String, unique=True, nullable=False)
    celular = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    status = db.Column(db.Boolean, nullable=False)

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nome', 'dtNasc', 'cpf', 'celular', 'email', 'senha', 'admin', 'status')

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

secret_key = urandom(24)
