from flask import Flask
from flask_cors import CORS  # Importa la extensión CORS
from app.api.scanner_api import scanner_api_bp
from app.api.generator_qr import generador_qr_bp
from app.DB.routes.routes_users import users_db_bp 
from app.DB.routes.routes_hoja_respuestas import hoja_respuestas_bp
from app.DB.routes.routes_pruebas import pruebas_db_bp

app = Flask(__name__)

# Configuración de la aplicación, si es necesario
# app.config['DEBUG'] = True

# Registra la blueprint de la API
app.register_blueprint(scanner_api_bp)
app.register_blueprint(generador_qr_bp)
app.register_blueprint(users_db_bp)
app.register_blueprint(hoja_respuestas_bp)
app.register_blueprint(pruebas_db_bp)
# Configuración de CORS
CORS(app)  # Esto permite solicitudes desde cualquier origen
