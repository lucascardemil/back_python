import pymysql

def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Agustina1812',  # Agrega tu contraseña real aquí
        db='lectorOMR',
    )

