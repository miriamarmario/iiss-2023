# Undefined en Python

En Python, los mecanismos de `undefined` se utilizan para manejar situaciones en las que se intenta acceder a un atributo o método de un objeto que no ha sido definido previamente. Estos mecanismos son útiles para evitar errores y excepciones que pueden ocurrir en el código.

## Ejemplo 1
El ejemplo se centra en la clase `Mago`, que tiene tres atributos opcionales: nombre, edad y casa. Para indicar que estos atributos son opcionales, se utiliza la clase `Optional` del módulo `typing`.

En la función `obtener_puntuacion`, se simula un cálculo de la puntuación de un `mago` en función de su casa. Si la casa no está definida, se devuelve un valor `None`.

En la primera parte del código, se crea un objeto `Mago` llamado `Harry Potter` y se obtiene su puntuación. Para verificar si el objeto tiene una puntuación definida o no, se utiliza la sentencia is not `None`. Esto es útil para verificar si un valor existe o no.

Luego se verifica si la puntuación de Harry es mayor a 80. Para ello, se utiliza una variable booleana llamada `tiene_alta_puntuacion`. En la expresión para calcular esta variable, se utiliza de nuevo la sentencia is not `None` para verificar que la puntuación existe.

Finalmente, se obtiene el valor de la propiedad casa de Harry. Si este atributo no está definido, se utiliza la expresión or `'sin casa'` para asignarle un valor por defecto.


## Ejemplo 2

Antes de empezar, hay que instalar la extensión `pyxtension` de la siguiente forma:
```
pip install pyxtension
```

El ejemplo tiene dos clases,`Magia` y `Mago`. La clase `Magia` tiene un atributo `hechizo` que puede ser opcional, representado mediante `Optional[str]`. Esto significa que un objeto `Magia` puede o no tener un hechizo asociado. 

La clase `Mago` tiene un atributo `magia` que también es opcional y está representado por `Optional[Magia]`. Esto permite que un mago pueda o no tener magia.

En el método `obtener_hechizo` de la clase `Mago`, se utiliza el Optional para devolver el hechizo asociado si existe, o None si no hay magia. Esto es útil para realizar comprobaciones y decisiones basadas en la presencia o ausencia de un hechizo.

El método `procesar_stream_magia` muestra cómo se puede utilizar el concepto de Optionals en el contexto de un stream de datos. Se utiliza el módulo `pyxtension.streams` para realizar operaciones en el stream de magos. En este caso, se filtran los magos que tienen un hechizo (es decir, aquellos cuyo `obtener_hechizo()` no es None) y se realiza una operación de mapeo para obtener información sobre cada mago mediante el método `imprimir_mago()`. Luego, se mapean los magos para imprimir sus detalles en mayúsculas y con signos de exclamación agregados. Finalmente, se imprime cada mago en la consola.


## Ejemplo 3

En este ejemplo, la función `obtener_casa` devuelve un `Optional[str]`, lo que significa que puede devolver un valor de tipo cadena (`str`) o ``None``. En el diccionario `casas`, se asignan las casas correspondientes a los nombres de algunos personajes de Harry Potter.

Luego, llamamos a la función `obtener_casa` para obtener la casa de un personaje específico, en este caso, `Harry`. Si la casa no es ``None``, imprimimos la casa. De lo contrario, mostramos un mensaje indicando que no se encontró la casa.

Al utilizar `Optional[str]`, estamos indicando de manera explícita que el valor de la casa puede ser ``None``, lo que ayuda a evitar errores de referencia a nulos (``None`Type`) y hace más claro el manejo de valores opcionales en el código
