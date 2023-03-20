#Definición de las clases
class Personaje:
    def __init__(self, nombre, casa):
        self.nombre = nombre
        self.casa = casa

    def presentar(self):
        print(f"Hola, mi nombre es {self.nombre} y pertenezco a la casa {self.casa}.")

class Estudiante(Personaje):
    def __init__(self, nombre, casa, año):
        super().__init__(nombre, casa)
        self.año = año

    def presentar(self):
        super().presentar()
        print(f"Soy un estudiante de {self.año} año.")

class Profesor(Personaje):
    def __init__(self, nombre, casa, materia):
        super().__init__(nombre, casa)
        self.materia = materia

    def presentar(self):
        super().presentar()
        print(f"Soy el profesor de {self.materia}.")

#Así se usaría 
harry = Estudiante("Harry Potter", "Gryffindor", 4)
dumbledore = Profesor("Albus Dumbledore", "Gryffindor", "Defensa Contra las Artes Oscuras")

harry.presentar() # Imprime: "Hola, mi nombre es Harry Potter y pertenezco a la casa Gryffindor. Soy un estudiante de 4 año."
dumbledore.presentar() # Imprime: "Hola, mi nombre es Albus Dumbledore y pertenezco a la casa Gryffindor. Soy el profesor de Defensa Contra las Artes Oscuras."
