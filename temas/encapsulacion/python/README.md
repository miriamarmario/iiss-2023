## Encapsulación en Python

En Python, la encapsulación se refiere a la capacidad de ocultar los detalles internos de una clase de forma que no puedan ser accedidos o modificados directamente desde fuera de la misma. Esto se logra mediante el uso de atributos y métodos privados, los cuales están indicados por el doble guión bajo ("__") antes del nombre del atributo o método.

En el ejemplo anterior, el atributo `hechizos` de la clase `Mago` está encapsulado utilizando el doble guión bajo. Esto significa que no puede ser accedido directamente desde fuera de la clase. En su lugar, se proporcionan métodos públicos como `get_hechizos` y `set_hechizos` para obtener y actualizar el valor del atributo.

Cuando se intenta acceder al atributo encapsulado directamente, como en la línea `print(harry_potter.__hechizos)`, se genera un error ya que el atributo no es accesible desde fuera de la clase. En cambio, se debe utilizar el método "get_hechizos" para obtener su valor, como se hace en la línea `print(harry_potter.get_hechizos())`.

También el uso de `pass` es importante para la encapsulación. Se utiliza para indicar una sentencia vacía, es decir, no hse va a implementar en la clase interfaz. En el ejemplo, se utiliza `pass` en el método `lanzar_hechizo` de la clase `IMago` (que es la clase que simula la Interfaz de Mago) para indicar que la implementación del método se definirá en la clase `Mago`.