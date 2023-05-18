from rx import of, create, just, interval, range, operators as ops
import sys
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
print("\nMecanismo 'just' con personajes de Harry Potter")
personajes = just(["Harry Potter", "Hermione Granger", "Ron Weasley"])

personajes.subscribe(
    on_next=lambda personaje: print("Personaje: {0}".format(personaje)),
    on_completed=lambda: print("¡Finalizó la lista de personajes!")
)


print("\nMecanismo 'interval' con contador de segundos hasta 5")
Fin = True
intervalo = interval(1).pipe(
    ops.take(5)
)

intervalo.subscribe(
    on_next=lambda segundo: print("Segundo: {0}".format(segundo)),
    on_completed=lambda: exit()
)

print("\nMecanismo 'range' con lista de números mágicos")
numeros_magicos = range(1, 11)

numeros_magicos.subscribe(
    on_next=lambda numero: print("Número mágico: {0}".format(numero)),
    on_completed=lambda: print("¡Finalizó la lista de números mágicos!")
)

print("\nMecanismo 'filter' con números mágicos")
numeros_magicos.pipe(
    ops.filter(lambda numero: numero % 2 == 0)
).subscribe(
    on_next=lambda numero: print("Número mágico: {0}".format(numero)),
    on_completed=lambda: print("¡Finalizó la lista de números mágicos!")
)

# Mecanismo 'map' con magos
print("\nMecanismo 'map' con magos")
magos = ["Harry Potter", "Hermione Granger", "Ron Weasley"]

observable = of(*magos).pipe(
    ops.map(lambda mago: mago.upper())
)

observable.subscribe(lambda mago: print(mago))


# Mecanismo 'distinct' con magos
print("\nMecanismo 'distinct' con magos")
magos = {"Harry Potter" , "Harry Potter", "Hermione Granger", "Ron Weasley", "Harry Potter"}
#Este mecanismo no funciona con listas, solo con conjuntos

observable = of(magos).pipe(
    ops.distinct()
)

observable.subscribe(lambda mago: print(mago))

# Mecanismo 'distinct_until_changed' con magos
print("\nMecanismo 'distinct_until_changed' con magos")
magos = ["Harry Potter","Harry Potter", "Hermione Granger", "Ron Weasley" ]

observable = of(*magos).pipe(
    ops.distinct_until_changed()
).subscribe(
    on_next=lambda mago: print("Mago: {0}".format(mago)),
    on_completed=lambda: print("¡Finalizó la lista de magos!")
)

lista_de_magos = [ "Harry Potter", "Hermione Granger", "Ron Weasley", "Harry Potter" ]

while(Fin):
    entrada = input("Cuando la cuenta llegue a 4, presione ENTER y sera liberado de este bucle infinito\n")
    #loop infinito para que no se cierre el programa
    