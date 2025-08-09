
class UsuarioDTO:
    def __init__(self, id=None, username="", email="", password=""):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f"UsuarioDTO(id={{self.id}}, username='{{self.username}}', email='{{self.email}}', password={{self.password}})"
