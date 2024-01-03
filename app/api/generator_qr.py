# generador_qr.py
import os
from flask import Blueprint, jsonify
import qrcode
from PIL import Image
import io

generador_qr_bp = Blueprint('generador_qr', __name__)

@generador_qr_bp.route('/api/generarqr', methods=['POST'])
def generar_qr_imagen(nombre, apellido, info_string):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(info_string)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Ruta absoluta
        ruta_absoluta = os.path.abspath(f"static/qr_images/qr_{nombre}_{apellido}.png")

        # Imprime la ruta para depuración
        print("Ruta absoluta:", ruta_absoluta)

        # Crea la carpeta si no existe
        carpeta_qr_images = os.path.dirname(ruta_absoluta)
        if not os.path.exists(carpeta_qr_images):
            os.makedirs(carpeta_qr_images)

        # Guarda el archivo
        img.save(ruta_absoluta)

        # Devuelve solo la ruta de la imagen
        return ruta_absoluta
    except Exception as e:
        # Imprime el error para depuración
        print("Error:", e)
        # Devuelve un objeto Response con el error en el JSON y el código de estado 500
        return jsonify({'error': str(e)}), 500