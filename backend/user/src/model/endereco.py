from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .user import Usuario

db = SQLAlchemy()
ma = Marshmallow()

class Endereco(db.Model):

    __tablename__ = 'enderecos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rua = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    complemento = db.Column(db.String(10))
    bairro = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(20), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(Usuario.id, ondelete='CASCADE'), nullable=False)

class AddressSchema(ma.Schema):
    class Meta:
        fields = ('id', 'rua', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado')

address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)

