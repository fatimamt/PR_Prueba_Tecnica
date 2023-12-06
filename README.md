#  DATA ENGINEER & BI Analyst - EXAM

Este repositorio incluye los entregables a los Ejecrcicios 1 y 2 de la prueba Técnica para el puesto de Data Engineer.

## Ejercicio 1. Bases de Datos
  * Entregables:
    
    Los resultados de este ejercicio fueron obtenidos bajo el supuesto de que cada cliente no deberá tener más de un protocolo igual. Por lo que, considerando el Data Sample proporcionado, se incluye una agrupación de protocolos para ser considerados todos los tipos de tráficos en el cálculo del tráfico total. Se requeriría más contexto de caso de uso en negocio para determinar si el resultado sería el más conveniente.
    - Resultado de la consulta:
      | **CLIENT** | **PROTOCOL** |
      |-------|----------|
      | 19-58-33-40-6E-66 | BGP,DNS,POP,SNP |
      | 9E-43-EA-54-0A-E7 | HTTPS,BGP,DNS,HTTP |
      | A6-B6-94-1E-07-FE | DHCP,TCP,HTTPS,DNS,BGP |
      | BB-0B-0C-1D-24-F4 | IMAP,TCP,SNP,POP |
      | E4-00-CE-46-3F-26 | IMAP,DNS |
      
    - SQL de la consulta: [E1.sql](E1.sql)

## Ejercicio 2. Programación
  * Entregables:
    - Código de la función: [E2.py](E2.py)
    - Pruebas Unitarias:
      | **equipoA** | **equipoB** | **RESULTADO** |
      |-------------|-------------|---------------|
      | \[1, 2, 3\] | \[2, 4\] | \[2, 3\] |
      | \[40, 41\] | \[22, 5\] | \[0, 0\] |
      | \[22, 5\] | \[40, 41\] | \[2, 2\] |
      | \[88, 48, 99, 38, 37] | \[77, 31, 63, 91, 37, 12, 33, 72, 58, 80] | \[3, 0, 3, 4, 1, 0, 0, 3, 3, 3] |
      | \[77, 31, 63, 91, 37, 12, 33, 72, 58, 80] | \[88, 48, 99, 38, 37] | \[9, 4, 10, 4, 4] |

## Ejercicio 3. Pipeline y orquestación
 * Entregables:
   Se entregan archivos solicitados para ser ejecutados en Airflow. El código en lenguaje Python, se complementa con las funciones declaradas en la carpeta [utils](utils), como función de apoyo para la lectura y manejo del archivo compartido. El flujo completo leerá el archivo en Excel que debe cumplir con las condiciones actuales (dos Sheets: Matriz de Adyacencia y Lista de Actores, columnas de la A a la AZ para la matriz, etc.), dentro de una función de Python, este archivo se convertirá a archivos CSV lo cuales serán los cargados a la base de Datos de MySQL en dos tablas, una de relación donde se ingestarán los valores de la matriz con el código referente a los actores, y otro donde se almacenarán la dimensión de relación código-actor.
   -  Código en Python con la configuración del Pipeline de datos: [palace_resorts_data_eng_test.py](palace_resorts_data_eng_test.py)
   -  Querys utilizados para generar la DB y tablas: [queries](queries)
