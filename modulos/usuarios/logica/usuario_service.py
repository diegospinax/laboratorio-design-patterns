import json
from fastapi import APIRouter, Request, HTTPException
from modulos.usuarios.acceso_datos.get_factory import obtener_fabrica


from modulos.usuarios.acceso_datos.usuario_dto import UsuarioDTO


usuarioDao = obtener_fabrica().crear_dao()
router = APIRouter()

@router.post("/crear")
async def crear_usuario(req: Request):
    data = await req.json()
    usuario = UsuarioDTO(
        username=data["username"],
        email=data["email"],
        password=data["password"]
    )
    
    usuarioDao.guardar(usuario)
    return {"mensaje": "Usuario creado correctamente."}


@router.get("/")
def obtener_usuarios():
    return [c.__dict__ for c in usuarioDao.obtener_todos()]


@router.get("/{id}")
def obtener_usuario(id: int):
    usuario = usuarioDao.obtener_por_id(id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario.__dict__


@router.put("/update/{id}")
async def actualizar_usuario(id: int, req: Request):
    data = await req.json()
    actualizado = UsuarioDTO(
        id=id,
        username=data["username"],
        email=data["email"],
        password=data["password"]
    )
    usuarioDao.actualizar(actualizado)
    return {"mensaje": "Usuario actualizado"}


@router.delete("/delete/{id}")
def eliminar_usuario(id: int):
    usuarioDao.eliminar(id)
    return {"mensaje": "Usuario eliminado"}
