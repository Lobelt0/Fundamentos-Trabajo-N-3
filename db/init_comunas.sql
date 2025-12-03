CREATE DATABASE inmobiliario;
USE inmobiliario;

CREATE TABLE comuna (
    id_comuna INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(5) UNIQUE,
    nombre VARCHAR(150)
);
