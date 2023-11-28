from flask import jsonify, request
from functools import wraps
import jwt
from api import app
from api.db.db import mysql


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'Message': 'Falta el Token'}),401

        user_id = None

        if 'usuario-id' in request.headers:
            user_id = request.headers['usuario-id']

        if not user_id:
            return jsonify({'Message': 'Falta el usuario'}),401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            token_id = data['id']
            if int(user_id) != int(token_id):
                return jsonify({'Message': 'Error en el token_id'})
        
        except Exception as e:
            print(e)
            return jsonify({'Message': str(e)}),401

        return func(*args, **kwargs)
    return decorated

def client_resource(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        print('Argumentos en client_resource: ', kwargs)
        cliente_id = kwargs['cliente-id'] 
        cur = mysql.cursor()
        cur.execute('SELECT cliente_id FROM client WHERE cliente_id = {0}'.format(cliente_id))
        data = cur.fetchone()
        if data:
            id_prop = data[0]
            user_id = request.headers['cliente-id']
            if int(id_prop) != int(user_id):
                return jsonify({'Message': 'No tienes permiso para acceder a este recurso'})

        return func(*args, **kwargs)
    return decorated


def user_resources(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        print('Argumentos en client_resource: ', kwargs)
        id_user_route = kwargs['usuario-id'] 
        user_id = request.headers['usuario-id']
        if int(id_user_route) != int(user_id):
            return jsonify({'Message': 'No tienes permisos par acceder a este recurso'}),401
            
        return func(*args, **kwargs)
    return decorated

