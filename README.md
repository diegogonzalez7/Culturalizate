## Nombre Proyecto: Culturalízate

Nuestro proyecto trata sobre una aplicación cultural enfocada en la exploración de información relativa 
a todos los países del mundo. Los casos de uso de nuestra aplicación son los siguientes:

 - 1.Crear Usuario
 - 2.Iniciar Sesión
 - 3.Cerrar Sesión
 - 4.Añadir país a favoritos
 - 5.Ver favoritos
 - 6.Mostrar información de un país
 - 7.Comparar datos de dos países
 - 8.Buscar países con una divisa
 - 9.Buscar país por capital
 - 10.Buscar países en el que se hable un determinado idioma
 - 11.Listado de países ordenados por su población
 - 12.Listado de países ordenados por su área
 - 13.Guardar gráficas de comparación obtenidas.


## Integrantes Grupo:
 - David Vilariño Da Silva david.vilarino@udc.es
 - Manuel Fontenlos Mato manuel.fontenlos@udc.es
 - Diego González González diego.gonzalez7@udc.es

## Ejecutar la aplicación en una imagen de docker:

desde la carpeta principal:
./run.sh 

O, desde cualquier carpeta:
docker run -p 8000:8000 manufontenlos/countries


## Problemas conocidos:

 - En los distintos buscadores de la aplicación no proporcionamos un listado con las distintas opciones para el usuario, lo que puede dar problemas al mismo, ya que el nombre del país, lenguaje, etc. se debe de escribir en inglés.

 - Los usuarios que no inician sesión tienen acceso a los mismos datos que los que sí que acceden.

 - No se guarda ni se muestra correctamente los países favoritos para cada usuario.


## Instrucciones de uso:

 - Para buscar información de un país (CU6): En la página principal introducir España, Brazil, England o el nombre de otro país cualquiera.

 - Para buscar países que hablen un determinado idioma (CU10): Clicar en search by language en la barra de navegación e introducir español, english, portuguese, russian, arabic u otro idioma que el usuario desee.

 - Para buscar el país de una capital (CU9): Clicar en search by capital y introducir el nombre de la capital: Madrid, París, etc.

 - Para buscar países que hablen un determinado idioma (CU8): Clicar en search by currency en la barra de navegación e introducir euro, dollar, dinar u otro divisa que el usuario desee.

## Información devuelta de cada país (CU6):

Para el país que el usuario busque devolvemos una tabla con la siguiente información:

 - Capital
 - Divisa
 - Continentes
 - Región
 - Subregión
 - Idiomas
 - Área (m²)
 - Población
 - Timezone

## URLS funcionales

 - 127.0.0.1:8000/home -> Home Page
 - 127.0.0.1:8000/login/ -> inicio sesión
 - 127.0.0.1:8000/sign_up/ -> registro usuarios 
 - 127.0.0.1:8000/apidata/ -> datos de la api (primera versión aún (hecho solo el caso de prueba), falta recoger respuesta forms y concatenar con la url para que funcione bien)
 - 127.0.0.1:8000/language -> buscar países por idioma
 - 127.0.0.1:8000/capital -> buscar países por capital
 - 127.0.0.1:8000/currency -> buscar países que usen una divisa

## Primera Iteración

Para la primera iteración del proyecto deberíamos haber completado los casos de uso 1,2,3,4,5,6,8,9 y 10 pero debido a dificultades en el desarrollo y falta de tiempo los casos de uso  3,4 y 5 no funcionan de forma correcta.

## Uso de Pandas

En esta primera iteración usamos pandas para ordenar los listados de países que nos devuelve la API de RestCountries al buscar países en los que se hable un determinado idioma y en los que se use una divisa concreta: estos son los casos de uso 8 y 10.
