from modulos.favoritos.configuracion.config import cargar_configuracion
from modulos.favoritos.acceso_datos.factory.pg_db_dao_factory import PostgresFavoritoDAOFactory
from modulos.favoritos.acceso_datos.factory.sql_db_dao_factory import MySQLFavoritoDAOFactory


def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresFavoritoDAOFactory()
    return MySQLFavoritoDAOFactory()