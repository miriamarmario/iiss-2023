import asyncio

async def buscar_hogwarts():
    print("Buscando el camino a Hogwarts...")
    await asyncio.sleep(2)
    print("¡Lo encontré! Ya llegué a Hogwarts.")

async def estudiar():
    print("Estudiando en Hogwarts...")
    await asyncio.sleep(5)
    print("¡Ya aprendí muchas cosas interesantes!")

async def realizar_tareas_extra():
    print("Realizando tareas extra...")
    await asyncio.sleep(3)
    print("Tareas extra completadas.")

async def main():
    tarea1 = asyncio.create_task(buscar_hogwarts())
    tarea2 = asyncio.create_task(estudiar())

    await asyncio.gather(tarea1, tarea2)

    print("Realizando otras tareas mientras estudias...")
    await realizar_tareas_extra()

if __name__ == "__main__":
    asyncio.run(main())
