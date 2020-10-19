from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from src import db, ma

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
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=False)

    def setRua(self, value):
        if value and len(value) > Endereco.rua.type.length:
            raise Exception("Value too long to 'rua' field")
        self.rua = value

    def setNumero(self, value):
        if value and len(value) > Endereco.numero.type.length:
            raise Exception("Value too long to 'numero' field")
        self.numero = value

    def setComplemento(self, value):
        if value and len(value) > Endereco.complemento.type.length:
            raise Exception("Value too long to 'complemento' field")
        self.complemento = value

    def setBairro(self, value):
        if value and len(value) > Endereco.bairro.type.length:
            raise Exception("Value too long to 'bairro' field")
        self.bairro = value

    def setCep(self, value):
        if value and len(value) > Endereco.cep.type.length:
            raise Exception("Value too long to 'cep' field")
        self.cep = value

    def setCidade(self, value): 
        if value and len(value) > Endereco.cidade.type.length:
            raise Exception("Value too long to 'cidade' field")
        self.cidade = value

    def setEstado(self, value):
        if value and len(value) > Endereco.estado.type.length:
            raise Exception("Value too long to 'estado' field")
        self.estado = value

class AddressSchema(ma.Schema):
    class Meta:
        fields = ('id', 'rua', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado')

address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)

