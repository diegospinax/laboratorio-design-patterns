### Laboratorio sobre patrones de diseño

En este laboratorio implementamos algunos patrones de diseño cómo el Factory, DAO, DTO, Singleton, entre otros. En una API hecha con FastAPI en python ![Python](https://img.shields.io/badge/Python-3.x-blue.svg). ✔

## Cómo ejecutar? 

- Primero, debemos asegurarnos de tener la base de datos creada (Es importante revisar el archivo de configuración dentro de la carpeta de cada módulo). ⚙

-  En la ruta `/modulos/comentarios/configuracion` están los respectivos scripts para la base de datos que desee montar. (Postgres o MySQL)

- Una vez creada la base de datos, debemos ejecutar:
    `pip install -r requirements.txt` -> para instalar las dependencias.

- Ahora, ejecutamos el proyecto con:
    `python -m uvicorn gateway.main:app --reload`

- Opcionalmente, podemos instalar en Visual Studio la extensión de REST Client, y utilizar los endpoints que se encuentran en comentarios_rest_client.http

NOTA: También hay una interfaz web dentro de frontend/web, que podemos utilizar para probar la aplicación.