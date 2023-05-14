# Observables en Python 

Los observables son un patrón de diseño muy útil en programación para notificar a los objetos interesados sobre los cambios en un objeto observado. En Python, podemos implementar el patrón Observable creando una clase que tenga una lista de observadores, que son objetos que se registran para ser notificados de los cambios. 

En este ejemplo, la clase `Observable` tiene una lista de observadores y tres métodos: `agregar_observador`, `eliminar_observador` y `notificar_observadores`. El método `agregar_observador` añade un observador a la lista de observadores, `eliminar_observador` elimina un observador de la lista y `notificar_observadores` itera sobre la lista de observadores y llama al método `actualizar` de cada observador, pasando un evento como argumento.

La clase `Mago` hereda de la clase `Observable` y tiene un método adicional llamado `set_puntuacion` que establece la puntuación del mago y llama al método `notificar_observadores` con un evento que indica que la puntuación ha cambiado.

Las clases `CasaMago` y `MinisterioMagia` heredan de la clase `Observador` y sobrescriben el método `actualizar`. La clase `CasaMago` imprime un mensaje cuando se actualiza la puntuación de un mago y la clase `MinisterioMagia` mantiene la puntuación total de todos los magos y la imprime cuando se actualiza la puntuación de un mago.

En el ejemplo se crean objetos de las clases `Mago`, `CasaMago` y `MinisterioMagia`, y se agregan y eliminan observadores para cada mago. Luego se establece la puntuación de cada mago y se observa cómo los observadores responden a los cambios en la puntuación.

