from modulos.productos.acceso_datos.factory.product_dao_factory import ProductoDAOFactory
from modulos.productos.acceso_datos.producto_dao import ProductoDAOMySQL


class MySQLProductoDAOFactory(ProductoDAOFactory):
    def crear_dao(self):
        return ProductoDAOMySQL()