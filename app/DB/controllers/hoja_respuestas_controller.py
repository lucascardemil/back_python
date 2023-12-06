from app.DB.bd import obtener_conexion
import json

def crear_hoja_respuestas(hoja_respuestas):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Convertir la lista de respuestas a una cadena JSON
            respuestas_json = json.dumps(hoja_respuestas['respuestas'])

            # Insertar nueva hoja de respuestas
            sql = "INSERT INTO hoja_de_respuestas (asignatura, alternativas, preguntas, respuestas) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (hoja_respuestas['asignatura'], hoja_respuestas['alternativas'], hoja_respuestas['preguntas'], respuestas_json))
        conexion.commit()
    except Exception as err:
        print('Error al crear hoja de respuestas:', err)
    finally:
        if conexion:
            conexion.close()

def obtener_hoja_respuestas():
    hojas_respuestas = []
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "SELECT * FROM hoja_de_respuestas"
            cursor.execute(sql)
            hojas_respuestas = cursor.fetchall()
    except Exception as err:
        print('Error al obtener hojas de respuestas:', err)
    finally:
        if conexion:
            conexion.close()
    return hojas_respuestas

def obtener_hoja_respuestas_por_id(hoja_respuestas_id):
    hoja_respuestas = None
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "SELECT * FROM hoja_de_respuestas WHERE id = %s"
            cursor.execute(sql, (hoja_respuestas_id,))
            hoja_respuestas = cursor.fetchone()
    except Exception as err:
        print(f'Error al obtener hoja de respuestas con ID {hoja_respuestas_id}:', err)
    finally:
        if conexion:
            conexion.close()
    return hoja_respuestas

def actualizar_hoja_respuestas(hoja_respuestas_id, nuevos_datos):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "UPDATE hoja_de_respuestas SET asignatura = %s, alternativas = %s, preguntas = %s, respuestas = %s WHERE id = %s"
            cursor.execute(sql, (nuevos_datos['asignatura'], nuevos_datos['alternativas'], nuevos_datos['preguntas'], nuevos_datos['respuestas'], hoja_respuestas_id))
        conexion.commit()
    except Exception as err:
        print(f'Error al actualizar hoja de respuestas con ID {hoja_respuestas_id}:', err)
    finally:
        if conexion:
            conexion.close()

def eliminar_hoja_respuestas(hoja_respuestas_id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "DELETE FROM hoja_de_respuestas WHERE id = %s"
            cursor.execute(sql, (hoja_respuestas_id,))
        conexion.commit()
    except Exception as err:
        print(f'Error al eliminar hoja de respuestas con ID {hoja_respuestas_id}:', err)
    finally:
        if conexion:
            conexion.close()
