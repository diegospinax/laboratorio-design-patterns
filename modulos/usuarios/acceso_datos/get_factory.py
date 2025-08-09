from modulos.usuarios.configuracion.config import cargar_configuracion
from modulos.usuarios.acceso_datos.factory.pg_db_dao_factory import PostgresUsuarioDAOFactory
from modulos.usuarios.acceso_datos.factory.sql_db_dao_factory import MySQLUsuarioDAOFactory


def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresUsuarioDAOFactory()
    return MySQLUsuarioDAOFactory()