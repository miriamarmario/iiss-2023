class Mago:
    def __init__(self, nombre, edad, casa):
        self.nombre = nombre
        self.edad = edad
        self.casa = casa

# Creamos una lista de magos
magos = [
    Mago("Harry Potter", 17, "Gryffindor"),
    Mago("Hermione Granger", 17, "Gryffindor"),
    Mago("Ron Weasley", 17, "Gryffindor"),
    Mago("Ginny Weasley", 16, "Gryffindor"),
    Mago("Draco Malfoy", 17, "Slytherin"),
    Mago("Luna Lovegood", 16, "Ravenclaw")
]

# Filtramos la lista de magos para obtener solo los mayores de edad y de Gryffindor
magos_filtrados = list(filter(lambda mago: mago.edad >= 17 and mago.casa == "Gryffindor", magos))

# Imprimimos la lista de magos filtrada
for mago in magos_filtrados:
    print(f"{mago.nombre}, de {mago.edad} años, es de la casa {mago.casa}")
