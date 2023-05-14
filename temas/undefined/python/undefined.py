#Clase Mago 
class Mago:
    def __init__(self, nombre=None, edad=None):
        self.nombre = nombre
        self.edad = edad



harry = Mago(nombre="Harry Potter")
# Intentamos acceder a un atributo no definido
try:
    print(harry.casa)
except AttributeError:
    print("La casa de este mago no ha sido definida aún.")

# Verificamos si el objeto tiene un atributo específico
if hasattr(harry, 'casa'):
    print(f"La casa de {harry.nombre} es {harry.casa}")
else:
    print(f"{harry.nombre} aún no tiene una casa definida.")

# Obtenemos el valor de un atributo específico, con un valor por defecto si no está definido
casa = getattr(harry, 'casa', 'no definida')
print(f"La casa de {harry.nombre} es {casa}.")
