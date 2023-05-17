# Observables en Python 
Los observables en Python son una parte de la biblioteca RxPy (Reactive Extensions for Python) que permite la programación reactiva utilizando el patrón Observable.

En el ejemplo, se utilizan diferentes mecanismos para crear y manipular observables:

## Mecanismo 'create' con Observable personalizado
El método `create` se utiliza para crear un observable personalizado. Se define una función `obtener_hechizos` que toma un observador y un planificador como parámetros. Dentro de esta función, se itera sobre una lista de hechizos y se notifica al observador con cada hechizo utilizando el método `on_next`. Finalmente, se llama al método `on_completed` para indicar que se han completado todas las notificaciones. El observable se crea mediante `create(get_spells)`, donde `get_spells` es la función definida anteriormente.

## Mecanismo 'just'
El método `just` se utiliza para crear un observable que emite un valor específico o una secuencia de valores especificados. En este caso, se utiliza `just(["Harry Potter", "Hermione Granger", "Ron Weasley"])` para crear un observable que emite una secuencia de personajes de Harry Potter.

## Mecanismo 'interval'
El método `interval` se utiliza para crear un observable que emite secuencialmente números enteros en intervalos regulares de tiempo. En el código, se crea un observable `interval(1)` que emite números enteros cada segundo. Luego se utiliza el operador `ops.take(6)` para limitar la emisión a solo los primeros 6 números.

## Mecanismo 'range'
El método `range` se utiliza para crear un observable que emite una secuencia de números enteros dentro de un rango especificado. En este caso, se crea el observable `magic_numbers = range(1, 11)` que emite números enteros del 1 al 10.

## Operadores de transformación: 'filter', 'map', 'distinct', 'distinct_until_changed'
Estos operadores se utilizan para manipular los datos emitidos por un observable:

- El operador `ops.filter` filtra los elementos emitidos por el observable según una condición específica. En el código, se utiliza `numeros_magicos.pipe(ops.filter(lambda numero: numero % 2 == 0))` para filtrar y emitir solo los números mágicos pares.
- El operador `ops.map` transforma cada elemento emitido por el observable aplicando una función específica. En el código, se utiliza `magos.pipe(ops.map(lambda mago: stream(mago).map(lambda c: c.upper()).to_list()))` para transformar cada mago en una lista de caracteres en mayúscula.
- El operador `ops.distinct` emite solo los elementos distintos, eliminando duplicados. En el código, se utiliza `magos.pipe(ops.distinct())` para emitir solo una vez cada mago de la lista.
- El operador `ops.distinct_until_changed` emite los elementos distintos consecutivos, es decir, solo emite un elemento si es diferente al elemento anterior. En el código, se utiliza `magos.pipe(ops.distinct_until_changed())` para emitir solo los magos que son diferentes al mago anterior.

## Subscripción a los observables
Una vez que se crean los observables, se realiza la suscripción a ellos mediante el método `subscribe`. Se proporcionan funciones de devolución de llamada (`on_next`, `on_completed`) que se ejecutan cuando se reciben elementos o cuando el observable se completa. Dentro de estas funciones de devolución de llamada, se realiza la manipulación o procesamiento de los datos emitidos por el observable.

