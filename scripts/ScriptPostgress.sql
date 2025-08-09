-- Crear base de datos (ejecutar en consola psql como superusuario)
CREATE DATABASE comentarios_db;

-- Conectarse a la base de datos (dentro de psql)
-- \c comentarios_db

-- Crear tabla comentarios
CREATE TABLE IF NOT EXISTS comentarios (
    id SERIAL PRIMARY KEY,
    texto TEXT NOT NULL,
    usuario_email VARCHAR(255) NOT NULL,
    calificacion INT NOT NULL CHECK (calificacion BETWEEN 1 AND 5),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY not null, 
    nombre varchar(255) not null, 
    descripcion varchar(255) not null, 
    precio numeric(10,2) not null, 
    categoria varchar(255) not null
);

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY not null, 
    username varchar(255) not null, 
    email varchar(255) not null, 
    password varchar(255) not null
);

CREATE TABLE IF NOT EXISTS favoritos (
    id SERIAL PRIMARY KEY not null, 
    producto_id INT not null, 
    usuario_id INT not null, 

    constraint fk_favorito_producto_id foreign key (producto_id) references productos(id),
    constraint fk_favorito_usuario_id foreign key (usuario_id) references usuarios(id)
);