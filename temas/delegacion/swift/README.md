- # Mecanismos de delegación en Swift

La delegación en Swift es un patrón de diseño que permite que un objeto de una clase transfiera la responsabilidad de ciertas tareas a otro objeto que implemente un protocolo específico. El objeto que transfiere la responsabilidad se llama "delegador", mientras que el objeto que recibe la responsabilidad se llama "delegado".

En el ejemplo proporcionado, se define un protocolo llamado `MagoOscuroDelegado`, que requiere que los objetos que lo implementen tengan una función llamada `magiaOscura()`. Luego, se define una clase llamada `MagoOscuro` que tiene una propiedad `delegate` de tipo `MagoOscuroDelegado?`.

La clase `MagoOscuro` tiene una función llamada `lanzarHechizo()` que llama a la función `magiaOscura()` del objeto delegado a través de la propiedad `delegate`. Si la propiedad `delegate` es `nil`, entonces no se llama a la función.

Luego se definen dos clases llamadas `Mortifago` y `Snape`, ambas implementan el protocolo `MagoOscuroDelegado`. Cada una de estas clases tiene su propia implementación de la función `magiaOscura()`.

Finalmente, se crean instancias de las clases `MagoOscuro`, `Mortifago` y `Snape`. Se asigna el objeto `mortifago` como delegado del objeto `mago`, y se llama a la función `lanzarHechizo()` del objeto `mago`. En este caso, la salida es "¡Morsmordre!" porque la implementación de la función `magiaOscura()` en `DeathEater` imprime ese mensaje.

Luego, se cambia el delegado del objeto `mago` al objeto `snape` y se llama a la función `lanzarHechizo()` del objeto `mago` nuevamente. En este caso, la salida es "¡Avada Kedavra!" porque la implementación de la función `magiaOscura()` en `Snape` imprime ese mensaje.

