from modulos.usuarios.acceso_datos.factory.usuario_dao_factory import UsuarioDAOFactory
from modulos.usuarios.acceso_datos.usuario_dao import UsuarioDAOPostgres


class PostgresUsuarioDAOFactory(UsuarioDAOFactory):
    def crear_dao(self):
        return UsuarioDAOPostgres()