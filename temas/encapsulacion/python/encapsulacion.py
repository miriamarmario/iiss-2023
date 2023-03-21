#Simulamos la interfaz
class IMago:
    def lanzar_hechizo(self, hechizo):
        pass

class Mago(IMago):
    def __init__(self, nombre, hechizos):
        self.nombre = nombre
        self.__hechizos = hechizos  # el atributo hechizos está encapsulado con "__"

    def get_hechizos(self):
        return self.__hechizos

    def set_hechizos(self, nuevos_hechizos):
        self.__hechizos = nuevos_hechizos
        print("¡Hechizos actualizados!")

    def lanzar_hechizo(self, hechizo):
        if hechizo in self.__hechizos:
            print(f"{self.nombre} ha lanzado el hechizo {hechizo}.")
        else:
            print(f"{self.nombre} no sabe lanzar el hechizo {hechizo}.")

# Crear un mago
harry_potter = Mago("Harry Potter", ["Expelliarmus", "Expecto Patronum", "Wingardium Leviosa"])

# Intentar acceder al atributo encapsulado directamente
#print(harry_potter.__hechizos)  # Esto generaría un error

# Obtener los hechizos del mago usando el método get_hechizos, en lugar de acceder al atributo privado
print(harry_potter.get_hechizos())

# Lanzar un hechizo usando la interfaz IMago
hechizo = "Expelliarmus"
if isinstance(harry_potter, IMago):
    harry_potter.lanzar_hechizo(hechizo)
else:
    print("El objeto no implementa la interfaz IMago.")
