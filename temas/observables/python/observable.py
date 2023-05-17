from rx import Observable

class Mago:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hechizos = Observable.create(self.hechizos_ de_editor)
        
    def editor_de_hechizos(self, observador):
        hechizos = ["Expelliarmus", "Lumos", "Accio", "Expecto Patronum"]
        
        for hechizo in hechizos:
            observador.on_next(hechizo)
            
        observador.on_completed()
        
    def aprender_hechizo(self):
        self.hechizos.subscribe(lambda hechizo: print(f"{self.nombre} aprendió el hechizo: {hechizo}"))

    def obtener_hechizos(self):
        return self.hechizos

# Crear instancias de Magos
harry_potter = Mago("Harry Potter")
hermione_granger = Mago("Hermione Granger")
ron_weasley = Mago("Ron Weasley")

# Los magos aprenden nuevos hechizos
harry_potter.aprender_hechizo()
hermione_granger.aprender_hechizo()
ron_weasley.aprender_hechizo()

# Obtener todos los hechizos en un solo stream
todos_los_hechizos = Observable.merge(harry_potter.obtener_hechizos(),
                                      hermione_granger.obtener_hechizos(),
                                      ron_weasley.obtener_hechizos())

# Filtrar los hechizos que comienzan con "E"
hechizos_con_e = todos_los_hechizos.filter(lambda hechizo: hechizo.startswith("E"))

# Transformar los hechizos a mayúsculas
hechizos_mayusculas = hechizos_con_e.map(lambda hechizo: hechizo.upper())

# Reducir los hechizos en una sola cadena separada por comas
hechizos_concatenados = hechizos_mayusculas.reduce(lambda acc, hechizo: acc + ", " + hechizo)

# Imprimir los hechizos concatenados
hechizos_concatenados.subscribe(lambda hechizos: print("Hechizos con E:", hechizos))
