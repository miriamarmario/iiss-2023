# Funciones Lambda en Python

## Filter

Las funciones lambda en Python son funciones anónimas y pequeñas que se definen en una sola línea y se utilizan en el momento en que se crean. Se definen utilizando la palabra clave `lambda`, seguida de los parámetros de entrada separados por comas y luego de los dos puntos, y finalmente la expresión que debe ser evaluada. 


En este eejmplo, se crea una clase `Mago` con tres atributos: `nombre`, `edad` y `casa`. Luego, se crea una lista de objetos `Mago` llamada `magos`. Para filtrar la lista de magos y obtener solo los mayores de edad y de Gryffindor, se utiliza la función `filter` y una función lambda. 

La función `filter` toma dos argumentos: una función que devuelve un valor booleano y un iterable (en este caso, una lista). La función lambda se utiliza como primer argumento y se define para verificar si el mago tiene al menos 17 años y pertenece a Gryffindor. Si la función lambda devuelve `True`, el mago se mantiene en la lista. De lo contrario, es eliminado de la lista. 

Finalmente, se utiliza un ciclo `for` para imprimir la lista de magos filtrada. Se recorre cada objeto `Mago` en `magos_filtrados` y se imprime su nombre, edad y casa. 

## List Comprehesion

La sintaxis de list comprehension es una forma concisa de crear listas en Python y se utiliza para simplificar la creación de listas en una sola línea de código. En este caso, se utiliza para imprimir los atributos de cada objeto `Mago` en una sola línea.

La sintaxis de list comprehension utiliza corchetes [] para crear una lista, seguido de una expresión y una cláusula for que recorre un iterable. En mi ejemplo, la expresión es una cadena de texto formateada que incluye los atributos del mago (nombre, edad y casa), y la cláusula for recorre cada objeto `Mago` en `magos_filtrados`.

Al utilizar list comprehension, el código se simplifica y se hace más legible al reducir la cantidad de código que se necesita para imprimir los atributos del mago.

## Map y Enumerate

En el tercer ejemplo utilizamos la función `enumerate()` para crear una enumeración de la lista de estudiantes. La función `enumerate()` toma una lista como argumento y devuelve un objeto enumerado que contiene pares de (índice, valor) para cada elemento de la lista. En este caso, estamos utilizando `enumerate()` para asignar un número de identificación a cada estudiante de la lista. Luego, utilizamos la función `map()` para aplicar una función lambda a cada elemento de la enumeración. La función lambda toma dos argumentos, `x[0]` y `x[1]`, que representan el índice y el valor de cada elemento en la enumeración, respectivamente. La función lambda crea un diccionario con un par clave-valor para el número de identificación y el nombre de cada estudiante. Finalmente, convertimos la enumeración resultante en una lista utilizando la función `list()` y almacenamos los resultados en una nueva lista llamada `estudiantes_id`.


