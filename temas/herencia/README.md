- # Herencia en Python

La herencia es un mecanismo fundamental en la programación orientada a objetos (POO) que permite a una clase heredar atributos y métodos de otra clase. En Python, la herencia se logra a través de la definición de una clase secundaria (también llamada "clase derivada" o "subclase") que extiende una clase primaria (también llamada "clase base" o "superclase").

En Python, la sintaxis para definir una clase secundaria que hereda de una clase primaria es la siguiente:

```python
class Subclase(ClaseBase):
    def __init__(self, argumentos_subclase):
        super().__init__(argumentos_superclase)
        # otros atributos y métodos de la subclase
```



En la definición de la subclase, se debe indicar entre paréntesis el nombre de la clase base que se está extendiendo. Además, se debe llamar al método `__init__()` de la clase base dentro del método `__init__()` de la subclase utilizando la función `super()`.
## Ejemplo

Para ilustrar el mecanismo de la herencia en Python, se puede considerar el siguiente ejemplo de tres clases relacionadas entre sí: `Personaje`, `Estudiante` y `Profesor`. La clase `Personaje` es la clase base, mientras que `Estudiante` y `Profesor` son subclases de `Personaje`.

```python
class Personaje:
    def __init__(self, nombre, casa):
        self.nombre = nombre
        self.casa = casa

    def presentar(self):
        print(f"Hola, mi nombre es {self.nombre} y pertenezco a la casa {self.casa}.")

class Estudiante(Personaje):
    def __init__(self, nombre, casa, año):
        super().__init__(nombre, casa)
        self.año = año

    def presentar(self):
        super().presentar()
        print(f"Soy un estudiante de {self.año} año.")

class Profesor(Personaje):
    def __init__(self, nombre, casa, materia):
        super().__init__(nombre, casa)
        self.materia = materia

    def presentar(self):
        super().presentar()
        print(f"Soy el profesor de {self.materia}.")
```



En este ejemplo, la clase `Personaje` tiene un constructor que inicializa los atributos `nombre` y `casa`, y un método `presentar()` que imprime un mensaje de presentación. La clase `Estudiante` extiende la clase `Personaje` y tiene un constructor adicional que inicializa el atributo `año`, y un método `presentar()` que llama al método `presentar()` de la clase base y luego imprime un mensaje adicional. La clase `Profesor` también extiende la clase `Personaje` y tiene un constructor adicional que inicializa el atributo `materia`, y un método `presentar()` que llama al método `presentar()` de la clase base y luego imprime un mensaje adicional.

Se puede utilizar estas clases para crear objetos de `Estudiante` y `Profesor`, que heredan los atributos y métodos de `Personaje`. Por ejemplo:

```python
harry = Estudiante("Harry Potter", "Gryffindor", 4)
dumbledore = Profesor("Albus Dumbledore", "Gryffindor", "Defensa Contra las Artes Oscur
```