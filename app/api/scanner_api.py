from flask import Blueprint, jsonify, request, json
from app.functions.image_processing import process_image
from app.DB.controllers.respuestas_alumnos_controller import agregar_respuestas_alumnos
from app.DB.controllers.pruebas_controller import crear_prueba

scanner_api_bp = Blueprint('scanner_api', __name__)

@scanner_api_bp.route('/api/scanner', methods=['POST'])
def scanner():
    try:
        request_data = request.get_json()
        jsonData = request_data["jsonData"]
        image = request_data["image"]
        # Procesa la imagen y obtiene el score
        response_data = process_image(request_data)
        agregar_respuestas_alumnos(image)

        print("Request data:", response_data)

        nota = response_data.get('nota', 0.0)
        print()  # Obtiene el score o establece 0.0 por defecto
        id_hoja_de_respuestas = request_data.get('id_hoja_de_respuestas')
        id_curso = jsonData.get('id_curso')
        id_alumno = jsonData.get('id_alumno')

        print(id_curso)
        print(id_alumno)
        print(id_hoja_de_respuestas)
        print(nota)

        prueba = {
            'id_alumno': id_alumno,
            'id_curso': id_curso,
            'id_hoja_de_respuestas': id_hoja_de_respuestas,
            'nota': nota,
            'activo': True  # Puedes ajustar esto según tus necesidades
        }
        print(prueba)
        # Crea la prueba con el id_alumno, id_curso, id_hoja y nota (score)
        crear_prueba(prueba)

        return jsonify(response_data)
    except Exception as e:
        print("Error:", str(e))  # Agrega este print para verificar cualquier error
        return jsonify({'error': str(e)}), 500