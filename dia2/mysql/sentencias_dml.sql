-- SENTENCIAS DML
-- CRUD
-- C - INSERT
-- R - SELECT
-- U - UPDATE
-- D - DELETE

-- INSERT
insert into alumno(nro_documento,nombre) values('100','cesar');
-- INSERTAR VARIOS REGISTROS
INSERT INTO alumno(nro_documento,nombre,nota)
VALUES
('200','ana',15),
('300','luis',20),
('400','jose',11),
('500','raul',10),
('600','carmen',13),
('700','jorge',16),
('800','daniel',20),
('900','luisa',17),
('1000','pedro',5);

-- ACTUALIZAR DATOS(UPDATE)
UPDATE alumno set email ='codigo@gmail.com';
-- ACTUALIZAR CON CONDICIONAL(WHERE)
UPDATE alumno set email = 'cesar@gmail.com' where id = 1;
-- ACTUALIZAR CON FUNCIONES
UPDATE alumno set email = CONCAT(nombre,'@hotmail.com') WHERE id != 1;

-- ELIMINAR(DELETE)
DELETE from alumno where id = 10;

-- SELECCIONAR

-- seleccionar todos los campos
SELECT * FROM alumno;

-- seleccionar solo algunos campos
SELECT nombre,nota from alumno;
-- seleccionar con filtros
SELECT nombre,nota from alumno where nota > 15;