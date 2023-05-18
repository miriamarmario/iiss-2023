# Uso de Observables en Python

Los observables son una parte fundamental de la programación reactiva y permiten trabajar con secuencias de datos asincrónicos. En Python, puedes utilizar la biblioteca RxPY para trabajar con observables y aprovechar los beneficios de la programación reactiva. A continuación, se presenta un ejemplo de uso de observables en Python utilizando diferentes mecanismos de RxPY:

## Mecanismo 'create' con un Observable personalizado

```python
from rx import create

def obtener_hechizos(observador, planificador):
    hechizos = ["Expelliarmus", "Lumos", "Accio", "Avada Kedavra"]
    for hechizo in hechizos:
        observador.on_next(hechizo)
    observador.on_completed()

fuente_hechizos = create(obtener_hechizos)

fuente_hechizos.subscribe(
    on_next=lambda hechizo: print("Lanzando hechizo: {0}".format(hechizo)),
    on_completed=lambda: print("¡Finalizó el lanzamiento de hechizos!")
)
```

En este ejemplo, creamos un observable personalizado utilizando el mecanismo `create()`. El observador recibe una secuencia de hechizos y los emite utilizando el método `on_next()`. Al finalizar la secuencia, se llama al método `on_completed()` para indicar que se han emitido todos los elementos. Finalmente, nos suscribimos al observable y proporcionamos funciones para manejar los eventos `on_next` y `on_completed`. 

## Mecanismo 'just' con personajes de Harry Potter

```python
from rx import just

personajes = just(["Harry Potter", "Hermione Granger", "Ron Weasley"])

personajes.subscribe(
    on_next=lambda personaje: print("Personaje: {0}".format(personaje)),
    on_completed=lambda: print("¡Finalizó la lista de personajes!")
)
```

En este ejemplo, utilizamos el mecanismo `just()` para crear un observable que emite una lista de personajes de Harry Potter. Luego, nos suscribimos al observable y proporcionamos funciones para manejar los eventos `on_next` y `on_completed`. Cada personaje se imprimirá en la consola y se mostrará un mensaje al finalizar la emisión.

## Mecanismo 'interval' con contador de segundos hasta 5

```python
from rx import interval, operators as ops

interval(1).pipe(
    ops.take(6)
).subscribe(lambda x: print("Segundos: {0}".format(x)))
```

En este ejemplo, utilizamos el mecanismo `interval()` para crear un observable que emite un valor cada segundo. Luego, utilizamos el operador `take()` para limitar la emisión a 6 valores. Nos suscribimos al observable y proporcionamos una función lambda para manejar los eventos `on_next`. En cada evento, se imprimirá el número de segundos transcurridos.

## Mecanismo 'range' con lista de números mágicos

```python
from rx import range

numeros_magicos = range(1, 11)

numeros_magicos.subscribe(
    on_next=lambda numero: print("Número mágico: {0}".format(numero)),
    on_completed=lambda: print("¡Finalizó la lista de números mágicos!")
)
```

En este ejemplo, utilizamos el mecanismo `range()` para crear un observable que emite

 una secuencia de números mágicos del 1 al 10. Nos suscribimos al observable y proporcionamos funciones para manejar los eventos `on_next` y `on_completed`. Cada número mágico se imprimirá en la consola y se mostrará un mensaje al finalizar la emisión.

## Mecanismo 'filter' con números mágicos

```python
from rx import of, operators as ops

numeros_magicos = of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

numeros_magicos.pipe(
    ops.filter(lambda numero: numero % 2 == 0)
).subscribe(
    on_next=lambda numero: print("Número mágico par: {0}".format(numero)),
    on_completed=lambda: print("¡Finalizó la lista de números mágicos!")
)
```

En este ejemplo, utilizamos el operador `filter()` para crear un observable que filtra solo los números mágicos pares. Nos suscribimos al observable y proporcionamos funciones para manejar los eventos `on_next` y `on_completed`. Solo se imprimirán los números mágicos pares.

## Mecanismo 'map' con magos

```python
from rx import of, operators as ops

magos = ["Harry Potter", "Hermione Granger", "Ron Weasley"]

observable = of(*magos).pipe(
    ops.map(lambda mago: mago.upper())
)

observable.subscribe(lambda mago: print(mago))
```

En este ejemplo, utilizamos el operador `map()` para crear un observable que transforma cada mago en letras mayúsculas. Nos suscribimos al observable y proporcionamos una función lambda para manejar los eventos `on_next`. Cada mago en mayúsculas se imprimirá en la consola.

## Mecanismo 'distinct' con magos

```python
from rx import of, operators as ops

magos = {"Harry Potter", "Harry Potter", "Hermione Granger", "Ron Weasley"}

observable = of(*magos).pipe(
    ops.distinct()
)

observable.subscribe(lambda mago: print(mago))
```

En este ejemplo, utilizamos el operador `distinct()` para crear un observable que emite únicamente magos únicos. Nos suscribimos al observable y proporcionamos una función lambda para manejar los eventos `on_next`. Solo se imprimirán los magos únicos.

## Mecanismo 'distinct_until_changed' con magos

```python
from rx import of, operators as ops

magos = ["Harry Potter", "Harry Potter", "Hermione Granger", "Ron Weasley"]

observable = of(*magos).pipe(
    ops.distinct_until_changed()
)

observable.subscribe(lambda mago: print(mago))
```

En este ejemplo, utilizamos el operador `distinct_until_changed()` para crear un observable que emite magos únicos consecutivos, omitiendo los elementos duplicados consecutivos. Nos suscribimos al observable y proporcionamos una función lambda para manejar los eventos `on_next`. Solo se imprimirán los magos únicos consecutivos.

Estos ejemplos demuestran diferentes mecanismos y operadores disponibles en RxPY para trabajar con observables en Python. La programación reactiva proporciona una manera poderosa de trabajar con secuencias de datos asincrónicos y permite desarrollar aplicaciones más concisas y eficientes.

# Instalación de RxPY

RxPY es una biblioteca de programación reactiva que te permite trabajar con observables en Python. Sigue estos pasos para instalar RxPY en tu entorno de desarrollo:

## Pasos de instalación
Instala RxPY utilizando el administrador de paquetes `pip`. Ejecuta el siguiente comando:

   ```bash
   pip install rx
   ```

   Esto descargará e instalará RxPY y sus dependencias.
    Se ha añadido un fichero `observable.py` con los ejemplos de la documentación implementados.