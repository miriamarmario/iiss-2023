class VaritaMagica:
    def __init__(self, madera, nucleo):
        self.madera = madera
        self.nucleo = nucleo
    
    def lanzar_hechizo(self, hechizo):
        print(f"¡{hechizo}!")
        
class Personaje:
    def __init__(self, nombre, casa, varita_magica):
        self.nombre = nombre
        self.casa = casa
        self.varita_magica = varita_magica
    
    def lanzar_hechizo(self, hechizo):
        self.varita_magica.lanzar_hechizo(hechizo)

# Creamos una varita mágica de madera de fresno y núcleo de pelo de unicornio
varita_de_harry = VaritaMagica("fresno", "pelo de unicornio")

# Creamos un personaje llamado Harry que pertenece a la casa Gryffindor y posee la varita de fresno con núcleo de pelo de unicornio
harry = Personaje("Harry Potter", "Gryffindor", varita_de_harry)

# Harry lanza un hechizo utilizando su varita mágica
harry.lanzar_hechizo("Expelliarmus")
