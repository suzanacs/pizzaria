import bcrypt
from sys import path
path.append('..')
from model.user import Usuario, user_schema, users_schema
path.append('..')
from model.endereco import Endereco, address_schema, addresses_schema
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify

db = SQLAlchemy()

class UsuarioController():
    
    @classmethod
    def criarUsuario(cls):
        try:
            db.session.execute('SELECT 1')
        except:
            db.session.rollback()
            return jsonify({'message': 'Failed to connect to database', 'data': {}}), 401
        msg = jsonify({'message': 'An error ocurred', 'data': {}}), 401
        hashed = ''
        if request.json:
            if request.json.get('senha'):
                salt = bcrypt.gensalt()
                hashed = bcrypt.hashpw(request.json.get('senha').encode('utf8'), salt)
            usuario = Usuario(
                    nome=request.json.get('nome'),
                    dtNasc=request.json.get('dtNasc'),
                    cpf=request.json.get('cpf'),
                    celular=request.json.get('celular'),
                    email=request.json.get('email'),
                    senha=hashed,
                    admin=False,
                    status=True
                    )
            endereco = Endereco(
                    rua=request.json.get('endereco').get('rua'),
                    numero=request.json.get('endereco').get('numero'),
                    complemento=request.json.get('endereco').get('complemento'),
                    bairro=request.json.get('endereco').get('bairro'),
                    cep=request.json.get('endereco').get('cep'),
                    cidade=request.json.get('endereco').get('cidade'),
                    estado=request.json.get('endereco').get('estado')
                    )
            if endereco.rua and endereco.numero and endereco.bairro and endereco.cep and endereco.cidade and endereco.estado:
                try:
                    db.session.add(usuario)
                    db.session.flush()
                    endereco.user_id = usuario.id
                    db.session.add(endereco)
                    db.session.commit()
                    result = user_schema.dump(usuario)
                    result['endereco'] = address_schema.dump(endereco)
                    msg = jsonify({'message': 'User created successfully', 'data': result})
                except:
                    db.session.rollback()
                    return jsonify({'message': 'An error occured', 'data': {}}), 401
        return msg

    @classmethod
    def usuarioByEmail(cls, email):
        try:
            return Usuario.query.filter(Usuario.email == email).one()
        except:
            return None
