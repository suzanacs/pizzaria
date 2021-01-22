import bcrypt
import json
from flask import request, jsonify
from src import db
from ..model.user import Usuario, user_schema, users_schema
from ..model.endereco import Endereco, address_schema, addresses_schema

class UsuarioController():
    
    @classmethod
    def criarUsuario(cls):
        try:
            db.session.execute('SELECT 1')
        except:
            db.session.rollback()
            return jsonify({'message': 'Failed to connect to database', 'data': {}}), 200
        msg = jsonify({'message': 'Required fields are blank, user was not created', 'data': {}}), 200
        hashed = ''
        if request.json:
            if request.json.get('senha'):
                salt = bcrypt.gensalt()
                hashed = bcrypt.hashpw(request.json.get('senha').encode('utf8'), salt)
            endereco = Endereco()
            try:
                endereco.setRua(request.json.get('endereco').get('rua'))
                endereco.setNumero(request.json.get('endereco').get('numero'))
                endereco.setComplemento(request.json.get('endereco').get('complemento'))
                endereco.setBairro(request.json.get('endereco').get('bairro'))
                endereco.setCep(request.json.get('endereco').get('cep'))
                endereco.setCidade(request.json.get('endereco').get('cidade'))
                endereco.setEstado(request.json.get('endereco').get('estado'))
            except Exception as e:
                return jsonify({ 'message': str(e), 'data': {} }), 200
            usuario = Usuario(
                    dtNasc=request.json.get('dtNasc'),
                    admin=False,
                    status=True,
                    endereco=endereco
                    )
            try:
                usuario.setNome(request.json.get('nome'))
                usuario.setCpf(request.json.get('cpf'))
                usuario.setCelular(request.json.get('celular'))
                usuario.setEmail(request.json.get('email'))
                usuario.setSenha(hashed)
            except Exception as e:
                return jsonify({ 'message': str(e), 'data': {} }), 200
            if usuario.nome and usuario.dtNasc and usuario.cpf and usuario.celular and usuario.email and usuario.senha and endereco.rua and endereco.numero and endereco.bairro and endereco.cep and endereco.cidade and endereco.estado:
                try:
                    db.session.add(usuario)
                    db.session.flush()
                    db.session.commit()
                    result = user_schema.dump(usuario)
                    result['endereco'] = address_schema.dump(endereco)
                    msg = jsonify({'message': 'User created successfully', 'data': result})
                except:
                    db.session.rollback()
                    return jsonify({'message': 'Failed to create user', 'data': {}}), 200
        return msg

    @classmethod
    def usuarioByEmail(cls, email):
        try:
            return Usuario.query.filter(Usuario.email == email).one()
        except:
            return None
