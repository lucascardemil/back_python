CREATE TABLE cursos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        curso VARCHAR(20) NOT NULL,
        activo BOOLEAN NOT NULL,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES users(id)
     )