
CREATE DATABASE IF NOT EXISTS inventario_python;

USE inventario_python;

CREATE TABLE IF NOT EXISTS categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    id_categoria INT,
    FOREIGN KEY (id_categoria)
        REFERENCES categorias(id_categoria)
);

INSERT INTO categorias (nombre) VALUES
('Informatica'),
('Accesorios'),
('Electronica');

INSERT INTO productos
(nombre, descripcion, precio, stock, id_categoria)
VALUES
('Mouse inalambrico', 'Mouse USB inalambrico', 85000, 15, 1),
('Teclado USB', 'Teclado con conexion USB', 120000, 8, 2),
('Monitor LED', 'Monitor LED de 24 pulgadas', 950000, 5, 3),
('Pendrive 64 GB', 'Memoria USB de 64 GB', 65000, 20, 2),
('Parlante Bluetooth', 'Parlante portatil Bluetooth', 180000, 7, 3);
