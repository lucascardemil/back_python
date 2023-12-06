from app.DB.bd import obtener_conexion

def crear_alumno(alumno):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Insertar nuevo alumno
            sql = "INSERT INTO alumnos (nombre, apellido, QR, id_prueba, id_respuestas_alumnos) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (alumno['nombre'], alumno['apellido'], alumno['QR'],alumno['id_prueba'],alumno['id_respuestas_alumnos'] ))
        conexion.commit()
    except Exception as err:
        print('Error al crear alumno:', err)
    finally:
        if conexion:
            conexion.close()

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
            sql = "UPDATE alumnos SET nombre = %s, apellido = %s, QR = %s, id_prueba = %s, id_respuestas_alumnos = %s WHERE id = %s"
            cursor.execute(sql, (
                nuevos_datos['nombre'],
                nuevos_datos['apellido'],
                nuevos_datos['QR'],
                nuevos_datos['id_prueba'],
                nuevos_datos['id_respuestas_alumnos'],
                alumno_id
            ))
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
