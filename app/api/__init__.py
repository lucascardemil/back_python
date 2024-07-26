from flask import Blueprint

generador_qr_bp = Blueprint('generador_qr', __name__)

from . import generator_qr