CREATE TABLE alumnos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(255) NOT NULL,
       apellido VARCHAR(255) NOT NULL,
       QR VARCHAR(255),
       id_curso INT,
       FOREIGN KEY (id_curso) REFERENCES cursos(id)
   );
