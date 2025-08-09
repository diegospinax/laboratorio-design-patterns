from modulos.favoritos.acceso_datos.factory.favorito_dao_factory import FavoritoDAOFactory
from modulos.favoritos.acceso_datos.favorito_dao import FavoritoDAOPostgres


class PostgresFavoritoDAOFactory(FavoritoDAOFactory):
    def crear_dao(self):
        return FavoritoDAOPostgres()