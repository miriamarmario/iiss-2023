# Definimos la clase Personaje
class Personaje:
    def __init__(self, nombre, casa):
        self.nombre = nombre
        self.casa = casa

# Definimos los personajes principales
harry = Personaje("Harry Potter", "Gryffindor")
ron = Personaje("Ron Weasley", "Gryffindor")
hermione = Personaje("Hermione Granger", "Gryffindor")
dumbledore = Personaje("Albus Dumbledore", "Gryffindor")
malfoy = Personaje("Draco Malfoy", "Slytherin")
riddle = Personaje("Tom Riddle", "Slytherin")
hagrid = Personaje("Rubeus Hagrid", "Gryffindor")

# Definimos la lista de personajes
personajes = [harry, ron, hermione, dumbledore, malfoy, riddle, hagrid]

# Definimos la función para encontrar los personajes de una determinada casa
def encontrar_personajes_por_nombre(personajes, nombre):
    for personaje in personajes:
        if personaje.nombre == nombre:
            return personaje
    return None # Si no se encuentra el personaje, se devuelve None

#Definimos una funcion para imprimir los personajes incluso cuando son None
def imprimir_personaje(personaje):
    if personaje is None:
        print("No se encontró el personaje")
    else:
        print(personaje.nombre, personaje.casa)

# Buscamos los personajes
harry_potter = encontrar_personajes_por_nombre(personajes, "Harry Potter")
imprimir_personaje(harry_potter)
# Un caso que no existe
voldemort = encontrar_personajes_por_nombre(personajes, "Voldemort")
imprimir_personaje(voldemort)