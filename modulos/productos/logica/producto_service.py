import json
from fastapi import APIRouter, Request, HTTPException
from modulos.productos.acceso_datos.get_factory import obtener_fabrica


from modulos.productos.acceso_datos.producto_dto import ProductoDTO


productDao = obtener_fabrica().crear_dao()
router = APIRouter()

@router.post("/crear")
async def crear_producto(req: Request):
    data = await req.json()
    producto = ProductoDTO(
        nombre=data["nombre"],
        descripcion=data["descripcion"],
        precio=float(data["precio"]),
        categoria=data["categoria"]
        )
    
    productDao.guardar(producto)
    return {"mensaje": "Producto creado correctamente."}


@router.get("/")
def obtener_productos():
    return [c.__dict__ for c in productDao.obtener_todos()]


@router.get("/{id}")
def obtener_producto(id: int):
    product = productDao.obtener_por_id(id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product.__dict__


@router.put("/update/{id}")
async def actualizar_producto(id: int, req: Request):
    data = await req.json()
    actualizado = ProductoDTO(
        id=id,
        nombre=data["nombre"],
        descripcion=data["descripcion"],
        precio=float(data["precio"]),
        categoria=data["categoria"]
    )
    productDao.actualizar(actualizado)
    return {"mensaje": "Producto actualizado"}


@router.delete("/delete/{id}")
def eliminar_producto(id: int):
    productDao.eliminar(id)
    return {"mensaje": "Producto eliminado"}
