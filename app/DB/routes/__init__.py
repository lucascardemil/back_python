from flask import Blueprint

# ...

users_db_bp = Blueprint('users_db', __name__)
hoja_respuestas_bp = Blueprint('hoja_respuestas', __name__)
pruebas_db_bp = Blueprint('pruebas_db', __name__)
alumnos_db_bp = Blueprint('alumnos_db', __name__)
cursos_db_bp = Blueprint('cursos_db', __name__)

from . import routes_users
from . import routes_hoja_respuestas
from . import routes_pruebas
from . import routes_alumnos
from . import routes_cursos