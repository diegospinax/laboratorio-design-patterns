import json
from fastapi import APIRouter, Request, HTTPException
from modulos.favoritos.acceso_datos.get_factory import obtener_fabrica


from modulos.favoritos.acceso_datos.favorito_dto import FavoritoDTO


favoritoDao = obtener_fabrica().crear_dao()
router = APIRouter()

@router.post("/crear")
async def crear_favorito(req: Request):
    data = await req.json()
    favorito = FavoritoDTO(
        producto_id=data["producto_id"],
        usuario_id=data["usuario_id"]
    )
    
    favoritoDao.guardar(favorito)
    return {"mensaje": "Favorito creado correctamente."}


@router.get("/")
def obtener_favoritos():
    return [c.__dict__ for c in favoritoDao.obtener_todos()]


@router.get("/{id}")
def obtener_favorito(id: int):
    favorito = favoritoDao.obtener_por_id(id)
    if not favorito:
        raise HTTPException(status_code=404, detail="Favorito no encontrado")
    return favorito.__dict__


@router.put("/update/{id}")
async def actualizar_favorito(id: int, req: Request):
    data = await req.json()
    actualizado = FavoritoDTO(
        id=id,
        producto_id=data["producto_id"],
        usuario_id=data["usuario_id"]
    )
    favoritoDao.actualizar(actualizado)
    return {"mensaje": "Favorito actualizado"}


@router.delete("/delete/{id}")
def eliminar_favorito(id: int):
    favoritoDao.eliminar(id)
    return {"mensaje": "Favorito eliminado"}
