from rx import create, just, interval, range, operators as ops
from pyxtension.streams import stream

# Mecanismo 'create' con Observable personalizado
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

# Mecanismo 'just' con personajes de Harry Potter
personajes = just(["Harry Potter", "Hermione Granger", "Ron Weasley"])

personajes.subscribe(
    on_next=lambda personaje: print("Personaje: {0}".format(personaje)),
    on_completed=lambda: print("¡Finalizó la lista de personajes!")
)

# Mecanismo 'interval' con contador de segundos hasta 5
interval (1).pipe(
    ops.take(6)
).subscribe(lambda x: print("Segundos: {0}".format(x)))

# Mecanismo 'range' con lista de números mágicos
numeros_magicos = range(1, 11)

numeros_magicos.subscribe(
    on_next=lambda numero: print("Número mágico: {0}".format(numero)),
    on_completed=lambda: print("¡Finalizó la lista de números mágicos!")
)

# Mecanismo 'filter' con números mágicos
numeros_magicos.pipe(
    ops.filter(lambda numero: numero % 2 == 0)
).subscribe(
    on_next=lambda numero: print("Número mágico: {0}".format(numero)),
    on_completed=lambda: print("¡Finalizó la lista de números mágicos!")
)

# Mecanismo 'map' con magos
magos = just(["Harry Potter", "Hermione Granger", "Ron Weasley"])

magos.pipe(
    ops.map(lambda mago: stream(mago).map(lambda c: c.upper()).to_list())
).subscribe(
    on_next=lambda mago: print("Mago: {0}".format(mago)),
    on_completed=lambda: print("¡Finalizó la lista de magos!")
)

# Mecanismo 'distinct' con magos
magos = just(["Harry Potter", "Hermione Granger", "Ron Weasley", "Harry Potter"])

magos.pipe(
    ops.distinct()
).subscribe(
    on_next=lambda mago: print("Mago: {0}".format(mago)),
    on_completed=lambda: print("¡Finalizó la lista de magos!")
)

# Mecanismo 'distinct_until_changed' con magos
magos = just(["Harry Potter", "Hermione Granger", "Ron Weasley", "Harry Potter"])

magos.pipe(
    ops.distinct_until_changed()
).subscribe(
    on_next=lambda mago: print("Mago: {0}".format(mago)),
    on_completed=lambda: print("¡Finalizó la lista de magos!")
)

lista_de_magos = [ "Harry Potter", "Hermione Granger", "Ron Weasley", "Harry Potter" ]
