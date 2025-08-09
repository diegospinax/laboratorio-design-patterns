
class FavoritoDTO:
    def __init__(self, id=None, producto_id=0, usuario_id=0):
        self.id = id
        self.producto_id = producto_id
        self.usuario_id = usuario_id

    def __str__(self):
        return f"FavoritoDTO(id={{self.id}}, producto_id='{{self.producto_id}}', usuario_id='{{self.usuario_id}}')"
