CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        contrasena VARCHAR(255) NOT NULL,
        activo BOOLEAN NOT NULL
    );