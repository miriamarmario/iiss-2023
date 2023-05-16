# Observables en Python 

El código muestra un ejemplo de cómo utilizar los observables en Python utilizando la biblioteca RxPY.

En este ejemplo, la clase `Mago` tiene un atributo llamado `hechizos`, que es un observable. La función `editor_de_hechizos` se utiliza para crear el observable y definir su comportamiento. En este caso, el observable emite una secuencia de hechizos predefinidos.

Dentro de la función `editor_de_hechizos`, se utiliza el parámetro `observador` para notificar a los suscriptores cada vez que ocurre un evento. En este caso, se utiliza el método `on_next` para emitir cada hechizo de la lista `hechizos` y `on_completed` para indicar que no habrá más eventos.

La función `aprender_hechizo` se encarga de suscribirse al observable `hechizos` y definir qué hacer cuando se emite un nuevo hechizo. En este caso, se imprime un mensaje indicando que el mago aprendió el hechizo.

Finalmente, se crean instancias de la clase `Mago` para representar a diferentes magos, como Harry Potter, Hermione Granger y Ron Weasley. Cada mago llama al método `aprender_hechizo` para comenzar a aprender los hechizos.