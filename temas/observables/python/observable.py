class Observable:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, evento):
        for observador in self.observadores:
            observador.actualizar(evento)


class Mago(Observable):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.puntuacion = 0

    def set_puntuacion(self, puntuacion):
        self.puntuacion = puntuacion
        self.notificar_observadores({'evento': 'puntuacion_cambiada', 'puntuacion': puntuacion})


class Observador:
    def actualizar(self, evento):
        pass


class CasaMago(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, evento):
        if evento['evento'] == 'puntuacion_cambiada':
            print(f"La casa {self.nombre} ha obtenido {evento['puntuacion']} puntos.")


class MinisterioMagia(Observador):
    def __init__(self):
        self.puntuacion_total = 0

    def actualizar(self, evento):
        if evento['evento'] == 'puntuacion_cambiada':
            self.puntuacion_total += evento['puntuacion']
            print(f"El Ministerio de Magia tiene ahora {self.puntuacion_total} puntos.")


harry = Mago("Harry Potter")
ron = Mago("Ron Weasley")
hermione = Mago("Hermione Granger")
dumbledore = MinisterioMagia()
gryffindor = CasaMago("Gryffindor")
slytherin = CasaMago("Slytherin")

harry.agregar_observador(gryffindor)
ron.agregar_observador(gryffindor)
hermione.agregar_observador(gryffindor)
harry.agregar_observador(dumbledore)
ron.agregar_observador(dumbledore)
hermione.agregar_observador(dumbledore)

print("Comienza el torneo de magia en Hogwarts...")

harry.set_puntuacion(10)
ron.set_puntuacion(20)
hermione.set_puntuacion(30)

print("Después de la primera ronda...")

harry.eliminar_observador(gryffindor)
ron.eliminar_observador(gryffindor)
hermione.eliminar_observador(gryffindor)

harry.set_puntuacion(40)
ron.set_puntuacion(50)
hermione.set_puntuacion(60)

print("Después de la segunda ronda...")
#Harry, ron y hermnione usan una pocion multijugos para hacerse pasar por Slytherin
print("Harry, Ron y Hermione usan una poción multijugos para hacerse pasar por Slytherin.")
print("Aun asi siguen anotando puntos para el Ministerio de Magia...")

harry.agregar_observador(slytherin)
ron.agregar_observador(slytherin)
hermione.agregar_observador(slytherin)

harry.set_puntuacion(70)
ron.set_puntuacion(80)
hermione.set_puntuacion(90)

print("Termina el torneo de magia en Hogwarts.")
