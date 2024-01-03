# app/DB/controllers/pruebas_controller.py
from app.DB.bd import obtener_conexion

def crear_prueba(prueba):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Insertar nueva prueba
            sql = "INSERT INTO pruebas (nota, activo, id_hoja_de_respuestas) VALUES (%s, %s, %s)"
            cursor.execute(sql, (prueba['nota'], prueba['activo'], prueba['id_hoja_de_respuestas']))
        conexion.commit()
    except Exception as err:
        print('Error al crear prueba:', err)
    finally:
        if conexion:
            conexion.close()

def obtener_pruebas():
    pruebas = []
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Obtener todas las pruebas
            sql = "SELECT * FROM pruebas"
            cursor.execute(sql)
            pruebas = cursor.fetchall()
    except Exception as err:
        print('Error al obtener pruebas:', err)
    finally:
        if conexion:
            conexion.close()
    return pruebas

def obtener_prueba_por_id(prueba_id):
    prueba = None
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Obtener una prueba por ID
            sql = "SELECT * FROM pruebas WHERE id = %s"
            cursor.execute(sql, (prueba_id,))
            prueba = cursor.fetchone()
    except Exception as err:
        print(f'Error al obtener prueba con ID {prueba_id}:', err)
    finally:
        if conexion:
            conexion.close()
    return prueba

def actualizar_prueba(prueba_id, nuevos_datos):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Actualizar una prueba por ID
            sql = "UPDATE pruebas SET nota = %s, activo = %s, id_hoja_de_respuestas = %s WHERE id = %s"
            cursor.execute(sql, (
                nuevos_datos['nota'],
                nuevos_datos['activo'],
                nuevos_datos['id_hoja_de_respuestas'],
                prueba_id
            ))
        conexion.commit()
    except Exception as err:
        print(f'Error al actualizar prueba con ID {prueba_id}:', err)
    finally:
        if conexion:
            conexion.close()

def eliminar_prueba(prueba_id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Eliminar una prueba por ID
            sql = "DELETE FROM pruebas WHERE id = %s"
            cursor.execute(sql, (prueba_id,))
        conexion.commit()
    except Exception as err:
        print(f'Error al eliminar prueba con ID {prueba_id}:', err)
    finally:
        if conexion:
            conexion.close()
