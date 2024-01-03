 CREATE TABLE hojas_de_respuestas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        asignatura VARCHAR(20) NOT NULL,
        alternativas VARCHAR(255) NOT NULL,
        preguntas VARCHAR(255) NOT NULL,
        respuestas varchar(255) DEFAULT NULL,
        usuario_id INT,
        FOREIGN KEY (usuario_id) REFERENCES users(id)
    );