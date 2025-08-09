
from modulos.favoritos.acceso_datos.favorito_dto import FavoritoDTO
from modulos.favoritos.acceso_datos.db_connection.connection import ConexionDB

conn = ConexionDB().obtener_conexion()
#el enmcargado de interactuar con la base de datos
class FavoritoDAOMySQL:
    def guardar(self, favorito_dto: FavoritoDTO):
        with conn.cursor() as cursor:
            sql = "INSERT into favoritos (producto_id, usuario_id) VALUES (%s, %s)"
            cursor.execute(sql, (favorito_dto.producto_id, favorito_dto.usuario_id))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, producto_id, usuario_id from favoritos")
            rows = cursor.fetchall()
        return [FavoritoDTO(id=row[0], producto_id=row[1], usuario_id=row[2]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, producto_id, usuario_id from favoritos WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return FavoritoDTO(id=row[0], producto_id=row[1], usuario_id=row[2])
        return None

    def actualizar(self, favorito_dto: FavoritoDTO):
        with conn.cursor() as cursor:
            sql = "UPDATE favoritos SET producto_id = %s, usuario_id = %s WHERE id = %s"
            cursor.execute(sql, (favorito_dto.producto_id, favorito_dto.usuario_id, favorito_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE from favoritos WHERE id = %s", (id,))
        conn.commit()

class FavoritoDAOPostgres:
    def guardar(self, favorito_dto: FavoritoDTO):
        with conn.cursor() as cursor:
            sql = "INSERT into favoritos (producto_id, usuario_id) VALUES (%s, %s)"
            cursor.execute(sql, (favorito_dto.producto_id, favorito_dto.usuario_id))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, producto_id, usuario_id from favoritos")
            rows = cursor.fetchall()
        return [FavoritoDTO(id=row[0], producto_id=row[1], usuario_id=row[2]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, producto_id, usuario_id from favoritos WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return FavoritoDTO(id=row[0], producto_id=row[1], usuario_id=row[2])
        return None

    def actualizar(self, favorito_dto: FavoritoDTO):
        with conn.cursor() as cursor:
            sql = "UPDATE favoritos SET producto_id = %s, usuario_id = %s WHERE id = %s"
            cursor.execute(sql, (favorito_dto.producto_id, favorito_dto.usuario_id, favorito_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE from favoritos WHERE id = %s", (id,))
        conn.commit()
