
#primer ejemplo con filter
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
    Mago("Luna Lovegood", 17, "Ravenclaw"),
    Mago("Cho Chang", 17, "Ravenclaw")
]

# Filtramos la lista de magos para obtener solo los mayores de edad y de Gryffindor
magos_filtrados = list(filter(lambda mago: mago.edad >= 17 and mago.casa == "Gryffindor", magos))

# Imprimimos la lista de magos filtrada
for mago in magos_filtrados:
    print(f"{mago.nombre}, de {mago.edad} años, es de la casa {mago.casa}")


#segundo ejemplo con list comprehension


# Filtramos la lista de magos para obtener solo los mayores de edad y de Ravenclar
magos_filtrados = [mago for mago in magos if mago.edad >= 17 and mago.casa == "Ravenclaw"]

# Imprimimos la lista de magos filtrada
for mago in magos_filtrados:
    print(f"{mago.nombre}, de {mago.edad} años, es de la casa {mago.casa}")
    
    
#tercer ejemplo con map y enumarate

# Creamos otra lista de estudiantes de Hogwarts
estudiantes = ['Harry Potter', 'Hermione Granger', 'Ron Weasley',
'Draco Malfoy', 'Cedric Diggory', 'Luna Lovegood', 'Neville Longbottom']

# Utilizamos enumerate y map para asignar un número de identificación a cada estudiante
estudiantes_id = list(map(lambda x: {'id': x[0], 'nombre': x[1]}, enumerate(estudiantes)))

# Imprimimos los estudiantes con sus identificadores
print("Estudiantes con sus identificadores:")
for estudiante in estudiantes_id:
    print(f"{estudiante['id']}: {estudiante['nombre']}")
