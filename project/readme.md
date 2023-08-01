# Nombre del proyecto

Proyecto Tienda Online


## Sobre el autor

Mi nombre es Irina Moldavsky. Soy matemática, trabajo con bases de datos y estoy aprendiendo a hacer una página web por primera vez!


## Descripción breve del proyecto

Es un ensayo de desarrollo de aplicación web en django. Se trata de un negocio de venta online. 

Se pueden agregar clientes con un formulario (http://127.0.0.1:8000/crear/) ingresando nombre, apellido, país, fecha de nacimiento y medio de pago. Entrando como admin se puede también agregar, borrar o editar.

También hay una página para visualizar todos los clientes (http://127.0.0.1:8000/clientes/).

Y tiene algunas búsquedas en la base (http://127.0.0.1:8000/busqueda/):

- Clientes cuyo nombre contenga una m
- Clientes que hayan nacido antes de 2005 y, por lo tanto, mayores de edad 
- Clientes de Argentina

## La parte técnica del proyecto

Se utilizó Python, Visual Studio Code, Django Framework con MVT, Git, Github y Html.

Superuser: admin
Clave: 1234


## Errores conocidos




## Futuras mejoras

- Quiero poder calcular la edad (a partir de la fecha de nacimiento), para hacer más exacto el cálculo de los clientes mayores de edad. 
- Me gustaría llevar estadística del porcentaje de clientes argentinos respecto del total. Hacer gráficos con las ventas diarias.
- Acceder a los datos de clientes o búsquedas solo a partir de un login.