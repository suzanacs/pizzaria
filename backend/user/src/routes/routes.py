from flask import jsonify
from src import app
from .controller.user_controller import UsuarioController
from .controller.helper import auth, token_required


@app.route('/', methods=['GET'])
@token_required
def root(current_user):
    return jsonify({'message': f'Hello {current_user.email}'})


@app.route('/users', methods=['POST'])
#@token_required
#def createUser(current_user):
def createUser():
    return UsuarioController.criarUsuario()

@app.route('/auth', methods=['POST'])
def authenticate():
    return auth()

@app.errorhandler(Exception)
def basic_error(e):
    return jsonify({'message': 'An error occured', 'data': {}}), 400

