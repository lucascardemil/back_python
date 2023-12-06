CREATE TABLE pruebas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nota INT,
    activo BOOLEAN,
    id_hoja_de_respuestas INT,
    id_respuestas_alumnos INT,
    FOREIGN KEY (id_hoja_de_respuestas) REFERENCES hoja_de_respuestas(id),
    FOREIGN KEY (id_respuestas_alumnos) REFERENCES respuestas_alumnos(id)
);
