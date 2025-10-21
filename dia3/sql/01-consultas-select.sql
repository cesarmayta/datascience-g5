-- CONSULTAS SELECT
select * from empleado;
select nombre,pais from empleado;
select * from empleado order by nombre;
select * from empleado order by salario desc;

-- filtros
select * from empleado where pais = 'Peru';
select * from empleado where salario > 5000;
select * from empleado where salario > 5000 and pais = 'Peru';
select * from empleado where salario BETWEEN 1000 AND 3000;