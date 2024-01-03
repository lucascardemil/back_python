CREATE TABLE alumnos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(255) NOT NULL,
       apellido VARCHAR(255) NOT NULL,
       QR VARCHAR(255),
       id_prueba INT,
       id_respuestas_alumnos INT,
       id_curso INT,
       FOREIGN KEY (id_prueba) REFERENCES pruebas(id),
       FOREIGN KEY (id_respuestas_alumnos) REFERENCES respuestas_alumnos(id),
       FOREIGN KEY (id_curso) REFERENCES cursos(id)
   );
