from typing import Optional
from pyxtension.streams import stream

class Magia:
    def __init__(self, hechizo: Optional[str] = None):
        self.hechizo = hechizo

    def obtener_hechizo(self) -> Optional[str]:
        return self.hechizo

    def lanzar_hechizo(self) -> None:
        print(f"Lanzando hechizo: {self.hechizo}")

    def imprimir_magia(self):
        print(f"Magia: {self.hechizo}")



class Mago:
    def __init__(self, nombre: str, edad: int, casa: Optional[str] = None, magia: Optional[Magia] = None):
        self.nombre = nombre
        self.edad = edad
        self.casa = casa
        self.magia = magia

    def obtener_hechizo(self) -> Optional[str]:
        if self.magia:
            return self.magia.obtener_hechizo()
        else:
            return None

    def lanzar_hechizo(self) -> None:
        if self.magia:
            self.magia.lanzar_hechizo()

    def imprimir_mago(self):
        if self.casa is not None:
            return (f"Nombre: {self.nombre}, Edad: {self.edad}, Casa: {self.casa}, Magia: {self.magia.obtener_hechizo()}")
        else:
            return ("Un momento... ¿Quién eres?")



def procesar_stream_magia(lista_magia) :
   for mago in stream(lista_magia).filter(lambda mago: mago.obtener_hechizo() is not None).map(lambda mago : mago.imprimir_mago()).map(lambda str : str.upper() + "!!!").to_list():
       print(mago)
    #return lista_magia_sin_hechizo

def imprimir_lista_mago(lista_magia):
    print(f"Lista de magos: {lista_magia}")

# lista de magos con sus respectivas edades
print ("A continuacion se muestra la lista de magos que si tienen hechizos con sus respectivas edades donde nadie que no sea de hogwarts y que por tanto no tenga casa esta incluido:")
lista_magos = [
    Mago(nombre="Harry Potter", edad=11, casa="Gryffindor", magia=Magia(hechizo="Expecto Patronum")),
    Mago(nombre="Hermione Granger", edad=11, casa="Gryffindor", magia=Magia(hechizo="Wingardium Leviosa")),
    Mago(nombre="Ron Weasley", edad=11, casa="Gryffindor", magia=Magia(hechizo="Lumos")),
    Mago(nombre="Draco Malfoy", edad=11, casa="Slytherin"),
    Mago(nombre="Severus Snape", edad=35, casa="Slytherin", magia=Magia(hechizo="Avada Kedavra")),
    Mago(nombre="Albus Dumbledore", edad=60, casa="Gryffindor", magia=Magia(hechizo="Expecto Patronum")),
    Mago(nombre="Minerva McGonagall", edad=60, casa="Gryffindor"),
    Mago(nombre="Rubeus Hagrid", edad=60, casa="Gryffindor"),
    Mago(nombre="Lord Voldemort", edad=60, magia=Magia(hechizo="Expecto Patronum")) # no tiene casa porque no es de Hogwarts (Es Voldemort)
    ]

procesar_stream_magia(lista_magos)