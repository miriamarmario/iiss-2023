from typing import Optional

# Ejemplo 1. Para saber si un valor existe o no
class Mago:
    def __init__(self, nombre: Optional[str] = None, edad: Optional[int] = None, casa: Optional[str] = None):
        self.nombre = nombre
        self.edad = edad
        self.casa = casa

    def obtener_puntuacion(self) -> Optional[int]:
        # Simulamos un cálculo de puntuación
        if self.casa == 'Gryffindor':
            return 70
        elif self.casa == 'Slytherin':
            return 80
        elif self.casa == 'Ravenclaw':
            return 100
        elif self.casa == 'Hufflepuff':
            return 90
        else:
            return None

harry = Mago(nombre="Harry Potter")

# Obtener la puntuación del mago
puntuacion = harry.obtener_puntuacion()

if puntuacion is not None:
    print(f"La puntuación de {harry.nombre} es {puntuacion}")
else:
    print(f"{harry.nombre} no tiene una casa definida. No se puede calcular la puntuación.")

# Verificar si el mago tiene una puntuación mayor a 80
tiene_alta_puntuacion = puntuacion is not None and puntuacion > 80

if tiene_alta_puntuacion:
    print(f"{harry.nombre} tiene una puntuación alta.")
else:
    print(f"{harry.nombre} no tiene una puntuación alta o no tiene una casa definida.")

# Obtener el valor de una propiedad específica con un valor por defecto si no está definida
casa = harry.casa or 'sin casa'
print(f"{harry.nombre} pertenece a la casa {casa}.")



