from aspectlib import Aspect, weave

def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        import time
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"La función {funcion.__name__} tardó {fin - inicio} segundos en ejecutarse.")
        return resultado
    return wrapper

class HarryPotter:
    @medir_tiempo
    def lanzar_hechizo(self, hechizo):
        print(f"¡Lanzando el hechizo {hechizo}!")
        # Se simula una espera de 2 segundos
        import time
        time.sleep(2)
        print("¡El hechizo ha sido lanzado!")

harry = HarryPotter()
harry.lanzar_hechizo("Expelliarmus")
