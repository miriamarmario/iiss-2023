# Anotaciones en Ruby

El código proporcionado implementa un módulo llamado `Anuncio` en Ruby que agrega un mecanismo similar a las anotaciones en Ruby. A través de la inclusión del módulo `Anuncio` en una clase y el uso del método `anunciar_metodo`, se puede imprimir un anuncio antes de la ejecución de los métodos seleccionados.

El módulo `Anuncio` define un método de clase llamado `anunciar_metodo` que recibe como argumentos una serie de símbolos que representan los nombres de los métodos que se desean anunciar. Dentro de este método, se realiza un bucle para cada método especificado. Se obtiene el método original utilizando `instance_method(metodo)` y se define un nuevo método utilizando `define_method`. Este nuevo método es el que se ejecutará en lugar del método original y contendrá la lógica del anuncio.

En el nuevo método definido, se imprime un mensaje de anuncio que indica el nombre del método y los parámetros que se están utilizando. A continuación, se busca la ubicación del archivo de origen y la línea de inicio del método original utilizando `original_method.source_location`. Si se encuentra la información del archivo y la línea, se lee el archivo línea por línea y se imprimen solo las líneas de código correspondientes al método, evitando las líneas en blanco y deteniéndose cuando se encuentra la palabra clave "end". Finalmente, se llama al método original utilizando `original_method.bind(self).call(*args, &block)` para ejecutar la lógica original del método.

En la clase `AtrapadorDeCriaturas`, se incluye el módulo `Anuncio` utilizando `include Anuncio`, lo que significa que los métodos de esta clase se verán afectados por el mecanismo de anuncios. Además, se utiliza el método `anunciar_metodo` para anunciar los métodos `lanzar_red` y `usar_varita`.

En el ejemplo de uso al final del código, se crea una instancia de `AtrapadorDeCriaturas` llamada `atrapador` y se llaman a los métodos `lanzar_red` y `usar_varita`. Al ejecutarse, se imprimirán los anuncios correspondientes a cada método antes de que se ejecute la lógica original del método.

