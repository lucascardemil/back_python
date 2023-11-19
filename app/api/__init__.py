from flask import Blueprint

scanner_api_bp = Blueprint('scanner_api', __name__)

from . import scanner_api  # Importa las rutas después de crear la Blueprint
