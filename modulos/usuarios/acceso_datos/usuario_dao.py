
from modulos.usuarios.acceso_datos.usuario_dto import UsuarioDTO
from modulos.usuarios.acceso_datos.db_connection.connection import ConexionDB

conn = ConexionDB().obtener_conexion()
#el enmcargado de interactuar con la base de datos
class UsuarioDAOMySQL:
    def guardar(self, usuario_dto: UsuarioDTO):
        with conn.cursor() as cursor:
            sql = "INSERT INTO usuarios (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (usuario_dto.username, usuario_dto.email, usuario_dto.password))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, username, email, password FROM usuarios")
            rows = cursor.fetchall()
        return [UsuarioDTO(id=row[0], username=row[1], email=row[2], password=row[3]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, username, email, password from usuarios WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return UsuarioDTO(id=row[0], username=row[1], email=row[2], password=row[3])
        return None

    def actualizar(self, usuario_dto: UsuarioDTO):
        with conn.cursor() as cursor:
            sql = "UPDATE usuarios SET username = %s, email = %s, password = %s WHERE id = %s"
            cursor.execute(sql, (usuario_dto.username, usuario_dto.email, usuario_dto.password, usuario_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE from usuarios WHERE id = %s", (id,))
        conn.commit()

class UsuarioDAOPostgres:
    def guardar(self, usuario_dto: UsuarioDTO):
        with conn.cursor() as cursor:
            sql = "INSERT INTO usuarios (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (usuario_dto.username, usuario_dto.email, usuario_dto.password))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, username, email, password from usuarios")
            rows = cursor.fetchall()
        return [UsuarioDTO(id=row[0], username=row[1], email=row[2], password=row[3]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, username, email, password from usuarios WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return UsuarioDTO(id=row[0], username=row[1], email=row[2], password=row[3])
        return None

    def actualizar(self, usuario_dto: UsuarioDTO):
        with conn.cursor() as cursor:
            sql = "UPDATE usuarios SET username = %s, email = %s, password = %s WHERE id = %s"
            cursor.execute(sql, (usuario_dto.username, usuario_dto.email, usuario_dto.password, usuario_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE from usuarios WHERE id = %s", (id,))
        conn.commit()
