from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'app_123'

import api.routes.usuario
import api.routes.productos
import api.routes.cliente
import api.routes.facturaProducto
import api.routes.facturaServicio
import api.routes.servicio