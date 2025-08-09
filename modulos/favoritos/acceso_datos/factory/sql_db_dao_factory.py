from modulos.favoritos.acceso_datos.factory.favorito_dao_factory import FavoritoDAOFactory
from modulos.favoritos.acceso_datos.favorito_dao import FavoritoDAOMySQL


class MySQLFavoritoDAOFactory(FavoritoDAOFactory):
    def crear_dao(self):
        return FavoritoDAOMySQL()