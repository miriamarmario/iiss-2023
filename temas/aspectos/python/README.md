# Aspectos en Python 

Los mecanismos de aspectos en Python son una técnica de programación que permite modificar el comportamiento de un programa sin alterar su código fuente. Los aspectos se pueden utilizar para agregar, eliminar o modificar funcionalidades en el código existente sin modificarlo directamente. Esto permite mejorar la modularidad, la reutilización y la mantenibilidad del código.

Antes, el mecanismo de implementar aspectos en Python eran los "Decoradores de Clase" (Class Decorators). Este mecanismo se introdujo en Python 2.2 como una forma de modificar el comportamiento de una clase completa en lugar de métodos individuales. Los decoradores de clase permitían agregar o reemplazar métodos, agregar o eliminar atributos de clase, y hacer otras modificaciones en la clase en sí.

Sin embargo, el uso de decoradores de clase se ha desaconsejado debido a su complejidad y efectos secundarios no deseados. Además, los decoradores de clase no se integraban bien con otros mecanismos de metaprogramación en Python, como la herencia y la composición.

En su lugar, se han desarrollado otras bibliotecas de aspectos más modernas y flexibles, como `AspectLib`, que se basan en los decoradores de funciones y la introspección en tiempo de ejecución. Estas bibliotecas de aspectos son más fáciles de usar, más flexibles y tienen menos efectos secundarios no deseados que los decoradores de clase.

Antes de nada, hay que instalar la librería `Aspectlib` de la siguiente manera:

```
pip install aspectlib
```

`Aspectlib` es una biblioteca Python que proporciona una implementación de aspectos. El código de ejemplo utiliza aspectos para medir el tiempo de ejecución de un método de una clase. La función `medir_tiempo` es un decorador que devuelve un envoltorio que mide el tiempo de ejecución de la función original. El envoltorio se agrega al método `lanzar_hechizo` de la clase `HarryPotter` mediante el decorador `@medir_tiempo`.

La línea `from aspectlib import Aspect, weave` importa la clase `Aspect` y la función `weave` de la biblioteca Aspectlib. La clase `Aspect` se utiliza para definir el comportamiento que se agregará a la función original, y la función `weave` se utiliza para aplicar el aspecto al objeto. En este ejemplo, el aspecto es la medición del tiempo de ejecución, y se aplica al método `lanzar_hechizo` de la instancia `harry` de la clase `HarryPotter`.

Cuando se llama al método `lanzar_hechizo` de la instancia `harry`, se ejecuta primero el envoltorio que mide el tiempo de ejecución, y luego se ejecuta la función original que lanza el hechizo. Al final, se imprime el tiempo de ejecución medido por el envoltorio.

