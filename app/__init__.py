from flask import Flask
from flask_cors import CORS  # Importa la extensión CORS
from app.api.scanner_api import scanner_api_bp

app = Flask(__name__)

# Configuración de la aplicación, si es necesario
# app.config['DEBUG'] = True

# Registra la blueprint de la API
app.register_blueprint(scanner_api_bp)

# Configuración de CORS
CORS(app)  # Esto permite solicitudes desde cualquier origen

