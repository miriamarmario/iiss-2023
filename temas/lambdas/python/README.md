# Funciones Lambda en Python

Las funciones lambda en Python son funciones anónimas y pequeñas que se definen en una sola línea y se utilizan en el momento en que se crean. Se definen utilizando la palabra clave `lambda`, seguida de los parámetros de entrada separados por comas y luego de los dos puntos, y finalmente la expresión que debe ser evaluada. 


En este eejmplo, se crea una clase `Mago` con tres atributos: `nombre`, `edad` y `casa`. Luego, se crea una lista de objetos `Mago` llamada `magos`. Para filtrar la lista de magos y obtener solo los mayores de edad y de Gryffindor, se utiliza la función `filter` y una función lambda. 

La función `filter` toma dos argumentos: una función que devuelve un valor booleano y un iterable (en este caso, una lista). La función lambda se utiliza como primer argumento y se define para verificar si el mago tiene al menos 17 años y pertenece a Gryffindor. Si la función lambda devuelve `True`, el mago se mantiene en la lista. De lo contrario, es eliminado de la lista. 

Finalmente, se utiliza un ciclo `for` para imprimir la lista de magos filtrada. Se recorre cada objeto `Mago` en `magos_filtrados` y se imprime su nombre, edad y casa. 

Las funciones lambda son útiles para operaciones simples que se realizan dentro de una función. Al no tener un nombre definido, son fáciles de usar y se pueden utilizar en cualquier parte donde se necesite una función. En este ejemplo la función lambda se utiliza como argumento de `filter`, pero también se puede utilizar en otras funciones, como `map` o `reduce`.