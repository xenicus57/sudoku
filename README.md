# TITULO:Resolucion de sudokus cuadrados de cualquier dimension

Se pretende resolver cualquier sudoku cuadrado, de cualquier dimension.

Dimension: 4x4
Cadena de elementos posibles: "1234" 
Matriz de trabajo de 16 casillas

Dimensión: 9x9 (Soduku clasico)
Cadena de elementos posibles: "123456789"
Matriz de trabajo de 81 casillas

Dimension: 16x16
Cadena de elementos posibles: "123456789ABCDFG"
Matriz de trabajo de 256 casillas

Dimension: 25x25
Cadena de elementos posibles: "123456789ABCDEFGHIJKLMNOP"
Matriz de trabajo de 625 casillas

Dimension: 36x36
Cadena de elementos posibles: "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZa"
Matriz de trabajo de 1296 casillas

Dimension: 49x49
Cadena de elementos posibles:"123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn"
Matriz de trabajo de 2401 casillas

Sudokus que superen la dimensión 3x3 es dificil encontralos.

Este proyecto esta resuelto personalmente en 2006 con ALASKA-SW, mi intención con esto es aprender Python (actualmente soy un neofito).
***************************************

Conceptos:
Se entiende que se conoce el paradigma del sudoku y el concepto de filas, colunmas y cuadros, en los en sus casillas contienen todos los elementos sin repetir. 

Sudoku de 9 elementos:

2|9|7|8|3|6|1|4|5|
4|6|3|1|9|5|8|7|2|
5|8|1|4|7|2|9|6|3|
------------------
6|7|2|9|5|1|4|3|8|
8|3|5|6|4|7|2|9|1|
1|4|9|2|8|3|6|5|7|
------------------
9|5|4|7|2|8|3|1|6|
3|2|6|5|1|4|7|8|9|
7|1|8|3|6|9|5|2|4|

Si nos fijamos en cualquier fila o colunma se observará que no se repite ningun elemento.
Un cuadro esta formado por por el cruce de 3 filas y 3 columnas, observese los cuadros formados por las 3 primeras filas y todas las columnas
representan a los 3 primeros cuadros, observese que en ellos estan todos los elementos y ninguno repetido. 
2|9|7|     8|3|6|      1|4|5|
4|6|3|     1|9|5|      8|7|2|
5|8|1|     4|7|2|      9|6|3|

Esta explicación es valida para sudokus 2x2, 4x4, 5x5 ....Sudokus cuadrados.

***************
EXTRATEGIA RESOLUCIÓN
***************
Utilizaremos 2 algoritmos de resolución y si no podemos con ellos utilizaremos fuerza bruta (descomposición arborea).

No espereis un entorno GUI, es programación estructurada en entorno de consola.

Pasos:
-----

PRIMERO (carga)

Como vamos a resolver cualquier sudoku cuadrado al modulo de resolucion le pasaremos 2 ficheros:
1.- Un fichero de texto de configuración (sdk.ini) para el modulo de resolución, donde le indicaremos entre otras cosas: los elementos del sudoku, donde queremos la salida, numero maximo de soluciones que ha de hallar, en caso de que tenga mas de una, y otros parametros que veremos mas adelante.
2.- Un fichero de texto con el sudoku a resolver.

SEGUNDO (validación)

Con el sudoku cargado estudiaremos que es incongruente, que no se han cargado algun elemento repetido tanto por fila / columna / cuadro.
A continuacion procederemos a resolverlo
















