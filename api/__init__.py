from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'app_123'
 
import api.routes.usuario
import api.routes.productos
