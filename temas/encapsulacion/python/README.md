## Encapsulación en Python

En Python, la encapsulación se refiere a la capacidad de ocultar los detalles internos de una clase de forma que no puedan ser accedidos o modificados directamente desde fuera de la misma. Esto se logra mediante el uso de atributos y métodos privados, los cuales están indicados por el doble guión bajo ("__") antes del nombre del atributo o método.

En el ejemplo anterior, el atributo `hechizos` de la clase `Mago` está encapsulado utilizando el doble guión bajo. Esto significa que no puede ser accedido directamente desde fuera de la clase. En su lugar, se proporcionan métodos públicos como `get_hechizos` y `set_hechizos` para obtener y actualizar el valor del atributo.

Cuando se intenta acceder al atributo encapsulado directamente, como en la línea `print(harry_potter.__hechizos)`, se genera un error ya que el atributo no es accesible desde fuera de la clase. En cambio, se debe utilizar el método "get_hechizos" para obtener su valor, como se hace en la línea `print(harry_potter.get_hechizos())`.

Además, cuando se intenta actualizar el atributo encapsulado directamente, como en la línea `harry_potter.__hechizos = ["Avada Kedavra"]`, esto no actualiza realmente el valor del atributo. En su lugar, se debe utilizar el método "set_hechizos" para actualizar el valor del atributo de manera segura, como se hace en la línea `harry_potter.set_hechizos(["Expelliarmus", "Expecto Patronum", "Wingardium Leviosa", "Alohomora"])`.

En resumen, la encapsulación es una herramienta importante en Python para garantizar la seguridad y la integridad de los datos de una clase. Al ocultar los detalles internos de una clase, se puede controlar el acceso y la modificación de los mismos, lo que puede ayudar a prevenir errores y problemas en el código.