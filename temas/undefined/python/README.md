# Undefined en Python

En Python, los mecanismos de `undefined` se utilizan para manejar situaciones en las que se intenta acceder a un atributo o método de un objeto que no ha sido definido previamente. Estos mecanismos son útiles para evitar errores y excepciones que pueden ocurrir en el código.

En el ejemplo proporcionado, se define una clase llamada `Mago` con dos atributos: `nombre` y `edad`. Sin embargo, no se define un atributo `casa`. Luego, se crea un objeto de esta clase llamado `harry` con el nombre `Harry Potter`.

Se intenta acceder al atributo `casa` de `harry` usando la sintaxis de punto. Como este atributo no está definido, se genera una excepción AttributeError. Para evitar que el programa se detenga debido a esta excepción, se utiliza un bloque try-except para capturar la excepción y mostrar un mensaje de error adecuado.

Luego, se utiliza la función hasattr() para verificar si el objeto `harry` tiene un atributo específico llamado `casa`. En este caso, como el atributo no está definido, la función devuelve False. Se muestra un mensaje que indica que `Harry Potter` aún no tiene una casa definida.

Finalmente, se utiliza la función getattr() para obtener el valor del atributo `casa` de `harry`, pero se proporciona un valor por defecto (`no definida`) en caso de que el atributo no esté definido. En este caso, el valor devuelto por getattr() es `no definida`, lo que indica que `Harry Potter` no tiene una casa definida.
