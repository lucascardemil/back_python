from flask import Blueprint, jsonify, request
import qrcode
from PIL import Image
import os

generador_qr_bp = Blueprint('generador_qr', __name__)

@generador_qr_bp.route('/api/generarqr', methods=['POST'])
def generar_qr():
    try:
        data = request.get_json()

        # Verifica si los datos necesarios están presentes en la solicitud
        required_fields = ['id', 'nombre', 'apellido', 'nota']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Faltan datos requeridos'}), 400

        # Crea una cadena con la información
        info_string = f"ID: {data['id']}\nNombre: {data['nombre']}\nApellido: {data['apellido']}\nNota: {data['nota']}"

        # Crea el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(info_string)
        qr.make(fit=True)

        # Crea una imagen PIL a partir del código QR
        img = qr.make_image(fill_color="black", back_color="white")

        # Guarda la imagen en un archivo en una ruta absoluta
        project_root = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(project_root, 'static', 'codigo_qr.png')
        img.save(img_path)

        response_data = {'image_path': img_path}

        return jsonify(response_data)
    except Exception as e:
        print("Error:", str(e))  
        return jsonify({'error': str(e)}), 500
