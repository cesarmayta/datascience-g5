-- AGRUPACIONES
-- 1 CONTAR
select count(*) from empleado;
select count(*) from empleado where salario > 5000;

-- 2 MAXIMOS Y MINIMOS
select max(salario) from empleado;
select min(salario) from empleado;
select avg(salario) from empleado;

select max(salario),min(salario),avg(salario) from empleado;

select DISTINCT pais from empleado;

-- SELECCIONAR EL TOTAL DE EMPLEADOS POR PAIS
select pais,count(*) from empleado
group by pais
order by count(*) desc;

select pais,area,max(salario),min(salario),avg(salario) from empleado
where salario > 5000
group by pais,area

-- subconsultas
-- consultas todos los empleados cuyo salario es mayor al promedio
select avg(salario) from empleado;
select nombre,salario from empleado
where salario > (select avg(salario) from empleado);

select pais,count(*) as total,(select avg(salario) from empleado) as salario_promedio
from empleado
group by pais order by count(*) desc