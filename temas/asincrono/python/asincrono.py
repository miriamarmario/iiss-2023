import threading
import time
import asyncio

#Primer ejemplo usando threading
class LanzamientoDeHechizo(threading.Thread):
    def __init__(self, personaje, hechizo, tiempo):
        threading.Thread.__init__(self)
        self.personaje = personaje
        self.hechizo = hechizo
        self.tiempo = tiempo

    def run(self):
        print(f"{self.personaje} está lanzando el hechizo {self.hechizo}...")
        time.sleep(self.tiempo)
        print(f"{self.personaje} ha lanzado el hechizo {self.hechizo} en {self.tiempo} segundos.")


# Creamos dos objetos LanzamientoDeHechizo para simular que dos personajes lanzan hechizos
duelo1 = LanzamientoDeHechizo("Harry Potter", "Expelliarmus", 5)
duelo2 = LanzamientoDeHechizo("Draco Malfoy", "Avada Kedavra", 3)

# Iniciamos los dos hilos para que ejecuten las tareas en paralelo
duelo1.start()
duelo2.start()

# Esperamos a que ambos hilos terminen antes de salir del programa
duelo1.join()
duelo2.join()

print("El duelo ha terminado.")


#Segundo ejemplo usando asyncio
async def buscar_hogwarts():
    print("Buscando el camino a Hogwarts...")
    await asyncio.sleep(2)
    print("¡Lo encontré! Ya llegué a Hogwarts.")

async def estudiar():
    print("Estudiando en Hogwarts...")
    await asyncio.sleep(5)
    print("¡Ya aprendí muchas cosas interesantes!")

async def main():
    tarea1 = asyncio.create_task(buscar_hogwarts())
    tarea2 = asyncio.create_task(estudiar())

    await tarea1
    await tarea2

if __name__ == "__main__":
    asyncio.run(main())
