from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modulos.comentarios.logica.comentario_service import router as comentarios_router
from modulos.productos.logica.producto_service import router as productos_router
from modulos.usuarios.logica.usuario_service import router as usuarios_router
from modulos.favoritos.logica.favoritos_service import router as favoritos_router

app = FastAPI(title="API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(comentarios_router, prefix="/comentarios")
app.include_router(productos_router, prefix="/productos")
app.include_router(usuarios_router, prefix="/usuarios")
app.include_router(favoritos_router, prefix="/favoritos")