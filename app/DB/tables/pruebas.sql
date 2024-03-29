CREATE TABLE pruebas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nota DECIMAL(3, 1) NOT NULL CHECK (nota >= 0.0 AND nota <= 7.0),
        activo BOOLEAN NOT NULL,
        id_hoja_de_respuestas int DEFAULT NUL,
        id_alumno int DEFAULT NULL,
        id_curso int DEFAULT NULL,
        FOREIGN KEY (id_hoja_de_respuestas) REFERENCES hojas_de_respuestas(id)
        FOREIGN KEY (id_alumno) REFERENCES alumnos(id)
        FOREIGN KEY (id_curso) REFERENCES (id)

    )