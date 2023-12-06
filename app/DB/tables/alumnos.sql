CREATE TABLE alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    QR VARCHAR(255),
    pruebaId INT,
    FOREIGN KEY (pruebaId) REFERENCES pruebas(id)
);