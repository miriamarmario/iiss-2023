# Anotaciones en Ruby

Las anotaciones en Ruby son una forma de agregar metadatos a los elementos de código, como clases, métodos y variables, para describir su comportamiento y su tipo. Aunque no son necesarias para que el código funcione, pueden mejorar la legibilidad y la claridad del mismo.

En el ejemplo se puede ver cómo utilizar anotaciones en Ruby para agregar funcionalidades adicionales a un método:

Se define el módulo `Anuncio` que se incluye en la clase `AtrapadorDeCriaturas`. Dentro del módulo, se define el método de clase `anunciar_metodo`, que toma una lista variable de símbolos que representan los nombres de los métodos a los que se les agregará la funcionalidad adicional.

Dentro de `anunciar_metodo`, se define una nueva implementación para cada uno de los métodos especificados. La nueva implementación agrega tres funcionalidades:

1. Imprime un anuncio indicando que se va a ejecutar el método, junto con los parámetros que recibió.
2. Imprime el código fuente de la implementación del método.
3. Llama al método original con los mismos parámetros.

Para agregar esta funcionalidad, se utiliza el método `define_method` para definir una nueva implementación para cada uno de los métodos especificados en la lista variable de símbolos.

La anotación `self.included(base)` se utiliza para extender la clase que incluye el módulo `Anuncio` con el módulo `ClassMethods`, lo que permite llamar al método de clase `anunciar_metodo` en la clase.

Finalmente, se crea una instancia de `AtrapadorDeCriaturas` y se llaman a los métodos `lanzar_red` y `usar_varita`. Como resultado, se imprimirán los anuncios y el código fuente de la implementación del método, junto con la ejecución del método original.