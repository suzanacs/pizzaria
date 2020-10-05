from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from controller.user_controller import UsuarioController
from controller.helper import auth, token_required

app = Flask("universodapizza")
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:gui123@pizzaria-mysql:3306/pizzaria?auth_plugin=mysql_native_password&autocommit=true"
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
    

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
    return jsonify({'message': 'An error occured', 'data': {}}), 401

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
