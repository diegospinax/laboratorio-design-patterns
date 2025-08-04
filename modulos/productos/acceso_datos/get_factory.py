from modulos.productos.configuracion.config import cargar_configuracion
from modulos.productos.acceso_datos.factory.pg_db_dao_factory import PostgresProductoDAOFactory
from modulos.productos.acceso_datos.factory.sql_db_dao_factory import MySQLProductoDAOFactory


def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresProductoDAOFactory()
    return MySQLProductoDAOFactory()