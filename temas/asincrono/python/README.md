# Asíncrono en Python

En Python, la programación asíncrona se logra utilizando las palabras clave `async` y `await`, junto con la biblioteca `asyncio`. Estas características permiten definir funciones asíncronas que pueden suspender su ejecución mientras esperan que se complete una operación costosa, como la entrada/salida o la espera de un tiempo determinado.

## Asíncrono.py
En Python, la programación asíncrona se logra utilizando las palabras clave `async` y `await`, junto con la biblioteca `asyncio`. Estas características permiten definir funciones asíncronas que pueden suspender su ejecución mientras esperan que se complete una operación costosa, como la entrada/salida o la espera de un tiempo determinado.

En el código de ejemplo, se definen varias funciones asíncronas que simulan diferentes tareas en Hogwarts. Cada una de estas funciones utiliza la palabra clave `await` para indicar los puntos en los que se debe esperar a que se complete una operación costosa, como la espera de un tiempo determinado utilizando `asyncio.sleep()`.

La función `main()` se encarga de organizar las tareas principales utilizando `asyncio.create_task()` para crear tareas asíncronas y `asyncio.gather()` para ejecutarlas de forma concurrente. Esto permite que las tareas de búsqueda de Hogwarts y estudio en Hogwarts se ejecuten en paralelo.

Después de esperar a que se completen las tareas principales, el programa continúa ejecutando el código restante, como la impresión de "Realizando otras tareas mientras estudias...". Permite que el programa continúe realizando otras acciones mientras se espera que se completen las tareas principales.

## Asíncrono2.py

El ejemplo se muestra un escenario en el que se simula el trabajo de dos "Elfos Domésticos" en una cocina mágica. Cada elfo es responsable de solicitar y preparar diferentes productos de un pedido. Utilizando la programación asíncrona, los elfos pueden solicitar y preparar los productos de forma concurrente, lo que mejora la eficiencia y la velocidad de procesamiento.

En el código, la clase `ElfoDomestico` contiene métodos asíncronos para manejar la solicitud y preparación de los pedidos. El método `solicitar_pedidos` se ejecuta en un bucle mientras hay pedidos en la cola de pedidos. Utiliza el método `solicitar_pedido` para procesar cada pedido de manera individual.

Dentro de `solicitar_pedido`, se itera sobre los productos del pedido y se utiliza el método `solicitar_producto` para solicitar y esperar la preparación de cada producto. Cada producto tiene un tiempo de preparación definido en el diccionario `TIEMPO_PREPARACION`, y se utiliza `asyncio.sleep()` para simular la espera.

Una vez que se han preparado todos los productos del pedido, se ejecuta el método `despachar_pedido` para indicar que el pedido ha sido despachado. Este método simplemente imprime los productos despachados.

En la función `main`, se crea una cola de pedidos utilizando `asyncio.Queue()`, y se agregan dos pedidos a la cola. Luego, se crean instancias de la clase `ElfoDomestico` y se asignan tareas asíncronas a cada elfo utilizando `asyncio.create_task()`. Estas tareas se ejecutan de forma concurrente utilizando `asyncio.gather()`.
