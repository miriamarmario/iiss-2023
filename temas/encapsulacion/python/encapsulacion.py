class Mago:
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

# Obtener los hechizos del mago usando el método get_hechizos
print(harry_potter.get_hechizos())

# Intentar actualizar los hechizos del mago directamente
harry_potter.__hechizos = ["Avada Kedavra"]  # Esto no actualizaría realmente los hechizos del mago

# Actualizar los hechizos del mago usando el método set_hechizos
harry_potter.set_hechizos(["Expelliarmus", "Expecto Patronum", "Wingardium Leviosa", "Alohomora"])

# Lanzar un hechizo
harry_potter.lanzar_hechizo("Wingardium Leviosa")
