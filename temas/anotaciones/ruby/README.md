# Anotaciones en Ruby

## Métodos de anotaciones en Ruby (simulación)

El código  muestra una simulación de anotaciones en Ruby utilizando módulos y métodos. Aunque Ruby no tiene un mecanismo incorporado para anotaciones como en otros lenguajes, es posible simular esta funcionalidad mediante el uso de técnicas específicas.

El módulo `Anuncio` define un método llamado `anunciar_metodo` en su módulo anidado `ClassMethods`. Este método se utiliza para agregar anotaciones a los métodos especificados.

El código en sí mismo recibe una clase llamada `AtrapadorDeCriaturas` y la incluye el módulo `Anuncio`. Dentro de `AtrapadorDeCriaturas`, se definen dos métodos: `lanzar_red` y `usar_varita`. Estos métodos son posteriormente anunciados mediante la llamada al método `anunciar_metodo` en la clase `AtrapadorDeCriaturas`.

Cuando se llama a cualquiera de los métodos anunciados, se ejecuta una secuencia de acciones definidas en el bloque del método `define_method`. Primero, se imprime un anuncio que muestra el método que va a ejecutarse y los parámetros proporcionados. Luego, se muestra el código fuente del método utilizando la ubicación del archivo fuente y la línea inicial del método. Finalmente, se llama al método original utilizando `original_method.bind(self).call(*args, &block)`.

A continuación, se muestra un ejemplo de uso del código:

```ruby
atrapador = AtrapadorDeCriaturas.new

atrapador.lanzar_red("hipogrifo", "Bosque Prohibido")
# => Lanzando red para atrapar a hipogrifo en Bosque Prohibido!

atrapador.usar_varita("Expelliarmus", "niffler")
# => Usando hechizo Expelliarmus para atrapar a niffler!
```

En este trozo de código, se crea una instancia de `AtrapadorDeCriaturas` y se llaman a los métodos `lanzar_red` y `usar_varita`. Cada método, además de realizar su lógica principal, muestra anuncios y el código fuente correspondiente.

