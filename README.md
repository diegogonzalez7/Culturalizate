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

## Primera Iteración

Para la primera iteración del proyecto deberíamos haber completado los casos de uso 1,2,3,4,5,6,8,9 y 10 pero debido a dificultades en el desarrollo y falta de tiempo los casos de uso  3,4 y 5 no funcionan de forma correcta.

## Entrega final

Para la entrega final hemos hecho con éxito todos los casos de uso, así como solventado los errores indicados en la primera iteración. Ahora la gestión de usuarios funciona correctamente, así como la funcionalidad de favoritos para los usuarios registrados.

## Uso de Pandas

En esta primera iteración usamos pandas para ordenar los listados de países que nos devuelve la API de RestCountries al buscar países en los que se hable un determinado idioma y en los que se use una divisa concreta: estos son los casos de uso 8 y 10.
En la entrega final hemos usado Pandas para los casos de uso relacionados con ordenar el dataframe de países por área y población, y en la comparación de datos entre dos países.

## Librerías third-party de Python

Hemos usado la librería/API googletrans para traducir los datos obtenidos con la predicción meteorológica en un determinado país o capital.
También hemos empleado el framework bootstrap para hacer las páginas web para hacerlos adaptables con un diseño responsive.

## Soporte de usuarios

Tal y como habíamos diseñado en la propuesta, hemos implementado una gestión de usuarios con vistas creadas por nosotros combinadas con las vistas predefinidas de Django para User Management.

## Separación del proyecto en aplicaciones

Hemos separado el proyecto en diferentes aplicaciones, obteniendo así unas vistas más cómodas y manejables, así como unas urls distinguibles dentro del proyecto.

## Experiencia de usuario e interfaz cuidadas

Los tiempos de respuesta ante peticiones los hemos reducido lo máximo posible, gracias a la concurrencia. Hemos diseñado también pantallas de error, spinners de carga mientras se realizan las operaciones y diseños atractivos para el usuario.

## Documentación

Dentro de /doc tenemos una versión final de documentación con un resumen de los casos de uso y su flujo de datos, así como una documentación más detallada sobre el proyecto
