from rx import Observable

class Mago:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hechizos = Observable.create(self.editor_de_hechizos)
        
    def editor_de_hechizos(self, observador):
        hechizos = ["Expelliarmus", "Lumos", "Accio", "Expecto Patronum"]
        
        for hechizo in hechizos:
            observador.on_next(hechizo)
            
        observador.on_completed()
        
    def aprender_hechizo(self):
        self.hechizos.subscribe(lambda hechizo: print(f"{self.nombre} aprendió el hechizo: {hechizo}"))

# Crear instancias de Magos
harry_potter = Mago("Harry Potter")
hermione_granger = Mago("Hermione Granger")
ron_weasley = Mago("Ron Weasley")

# Los magos aprenden nuevos hechizos
harry_potter.aprender_hechizo()
hermione_granger.aprender_hechizo()
ron_weasley.aprender_hechizo()
