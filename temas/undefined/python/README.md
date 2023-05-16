# Undefined en Python

En Python, los mecanismos de `undefined` se utilizan para manejar situaciones en las que se intenta acceder a un atributo o método de un objeto que no ha sido definido previamente. Estos mecanismos son útiles para evitar errores y excepciones que pueden ocurrir en el código.

## Ejemplo 1
El ejemplo se centra en la clase `Mago`, que tiene tres atributos opcionales: nombre, edad y casa. Para indicar que estos atributos son opcionales, se utiliza la clase `Optional` del módulo `typing`.

En la función `obtener_puntuacion`, se simula un cálculo de la puntuación de un `mago` en función de su casa. Si la casa no está definida, se devuelve un valor `None`.

En la primera parte del código, se crea un objeto `Mago` llamado `Harry Potter` y se obtiene su puntuación. Para verificar si el objeto tiene una puntuación definida o no, se utiliza la sentencia is not `None`. Esto es útil para verificar si un valor existe o no.

Luego se verifica si la puntuación de Harry es mayor a 80. Para ello, se utiliza una variable booleana llamada `tiene_alta_puntuacion`. En la expresión para calcular esta variable, se utiliza de nuevo la sentencia is not `None` para verificar que la puntuación existe.

Finalmente, se obtiene el valor de la propiedad casa de Harry. Si este atributo no está definido, se utiliza la expresión or `'sin casa'` para asignarle un valor por defecto.


## Ejemplo 2

En primer lugar, se define la clase `Personaje` que tiene dos atributos: `nombre` y `casa`. Luego se crean varios objetos de tipo `Personaje`. Luego se define la función `encontrar_personajes_por_nombre` que recibe una lista de personajes y un nombre, y busca un personaje específico en la lista. Si encuentra un personaje con el nombre proporcionado, lo devuelve; de lo contrario, devuelve ``None``. Además, se define la función `imprimir_personaje` que recibe un personaje y lo imprime. Si el personaje es ``None``, es decir, no se encontró ningún personaje, se imprime el mensaje `No se encontró el personaje`. De lo contrario, se imprime el nombre y la casa del personaje.

En el código de ejemplo, se utilizan estas funciones para buscar y mostrar información sobre dos personajes: `Harry Potter` y `Voldemort`. Primero se busca a `Harry Potter` en la lista de personajes. En este caso, se encontrará a `Harry Potter` y se imprimirá su nombre y casa.

Sin embargo, cuando se busca a `Voldemort`, no se encuentra ningún personaje con ese nombre en la lista, por lo que la función `encontrar_personajes_por_nombre` devuelve ``None``. Luego, la función `imprimir_personaje` maneja el valor ``None`` y muestra el mensaje `No se encontró el personaje`.

## Ejemplo 3
En este ejemplo, la función `obtener_casa` devuelve un `Optional[str]`, lo que significa que puede devolver un valor de tipo cadena (`str`) o ``None``. En el diccionario `casas`, se asignan las casas correspondientes a los nombres de algunos personajes de Harry Potter.

Luego, llamamos a la función `obtener_casa` para obtener la casa de un personaje específico, en este caso, `Harry`. Si la casa no es ``None``, imprimimos la casa. De lo contrario, mostramos un mensaje indicando que no se encontró la casa.

Al utilizar `Optional[str]`, estamos indicando de manera explícita que el valor de la casa puede ser ``None``, lo que ayuda a evitar errores de referencia a nulos (``None`Type`) y hace más claro el manejo de valores opcionales en el código
