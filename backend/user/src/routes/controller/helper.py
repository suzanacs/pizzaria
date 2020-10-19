import jwt
import datetime
from flask import request, jsonify
from bcrypt import checkpw
from src import app
from functools import wraps
from .user_controller import UsuarioController

def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    user = UsuarioController.usuarioByEmail(auth.username)
    if not user:
        return jsonify({'message': 'User not found', 'data': {}}), 401
    if user and checkpw(auth.password.encode('utf8'), user.senha.encode('utf8')):
        token = jwt.encode({'email': user.email, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}, app.config['SECRET_KEY'])
        return jsonify({'message': 'Validated successfully', 'token': token.decode('UTF-8'), 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})
    return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'token is missing', 'data': {}}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = UsuarioController.usuarioByEmail(data['email'])
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': {}}), 401
        return f(current_user, *args, **kwargs)
    return decorated
