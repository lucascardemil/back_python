from app.DB.bd import obtener_conexion
from app.api.generator_qr import generar_qr_imagen
from flask import jsonify

def crear_alumno(alumno):
    try:
        with obtener_conexion() as conexion:
            sql = "INSERT INTO alumnos (nombre, apellido, QR, id_curso) VALUES (%s, %s, %s, %s)"

            qr_info = f"nombre: {alumno['nombre']}\napellido: {alumno['apellido']}"

            # Genera el código QR y obtiene la ruta de la imagen
            qr_path = generar_qr_imagen(alumno['nombre'], alumno['apellido'], qr_info)

            print(qr_path, "path")

            with conexion.cursor() as cursor:
                cursor.execute(sql, (
                    alumno['nombre'],
                    alumno['apellido'],
                    qr_path,
                    alumno['id_curso']  # Utiliza directamente el identificador del curso
                ))

            conexion.commit()

            return jsonify({"status": "success", "message": "Alumno creado correctamente", "QR": qr_path})
    except Exception as err:
        print('Error al crear alumno:', err)
        return jsonify({"status": "error", "message": f"Error al crear alumno: {err}"}), 500
              
def obtener_alumnos():
    alumnos = []
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Obtener todos los alumnos
            sql = "SELECT * FROM alumnos"
            cursor.execute(sql)
            alumnos = cursor.fetchall()
    except Exception as err:
        print('Error al obtener alumnos:', err)
    finally:
        if conexion:
            conexion.close()
    return alumnos

def obtener_alumnos_por_curso(id_curso):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Consultar todos los alumnos de un curso específico
            sql = "SELECT * FROM alumnos WHERE id_curso = %s"
            cursor.execute(sql, (id_curso,))
            alumnos = cursor.fetchall()
        print(alumnos)
        return alumnos
    except Exception as err:
        print(f'Error al obtener alumnos por curso {id_curso}: {err}')
        return []
    finally:
        if conexion:
            conexion.close()
            
def obtener_alumno_por_id(alumno_id):
    alumno = None
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Obtener un alumno por ID
            sql = "SELECT * FROM alumnos WHERE id = %s"
            cursor.execute(sql, (alumno_id,))
            alumno = cursor.fetchone()
    except Exception as err:
        print(f'Error al obtener alumno con ID {alumno_id}:', err)
    finally:
        if conexion:
            conexion.close()
    return alumno

def actualizar_alumno(alumno_id, nuevos_datos):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Actualizar un alumno por ID
            sql = "UPDATE alumnos SET nombre = %s, apellido = %s, QR = %s WHERE id = %s"
            nuevo_qr = generar_qr_imagen(nuevos_datos['nombre'], nuevos_datos['apellido'], f"{nuevos_datos['nombre']} {nuevos_datos['apellido']}")
            cursor.execute(sql, (
                nuevos_datos['nombre'],
                nuevos_datos['apellido'],
                nuevo_qr,
                alumno_id
            ))

            # Después de actualizar el nombre y el apellido, genera un nuevo QR

        conexion.commit()
    except Exception as err:
        print(f'Error al actualizar alumno con ID {alumno_id}:', err)
    finally:
        if conexion:
            conexion.close()

def eliminar_alumno(alumno_id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Eliminar un alumno por ID
            sql = "DELETE FROM alumnos WHERE id = %s"
            cursor.execute(sql, (alumno_id,))
        conexion.commit()
    except Exception as err:
        print(f'Error al eliminar alumno con ID {alumno_id}:', err)
    finally:
        if conexion:
            conexion.close()

def eliminar_alumnos_por_curso(id_curso):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Eliminar alumnos por id_curso
            sql = "DELETE FROM alumnos WHERE id_curso = %s"
            cursor.execute(sql, (id_curso,))
        conexion.commit()
    except Exception as err:
        print(f'Error al eliminar alumnos por curso con ID {id_curso}:', err)
    finally:
        if conexion:
            conexion.close()            