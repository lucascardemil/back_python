CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    materia VARCHAR(30),
    curso VARCHAR(30),
    activo BOOLEAN,
    id_alumnos INT,
    prueba_id INT,
    user_id INT,
    FOREIGN KEY (id_alumnos) REFERENCES alumnos(id),
    FOREIGN KEY (prueba_id) REFERENCES pruebas(id),
    FOREIGN KEY (user_id) REFERENCES usuarios(id)
);
