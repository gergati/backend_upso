from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'app_123'
 
import api.models.usuario
import api.models.cliente
import api.models.producto