## Inyección de dependencias en Swift

La inyección de dependencias es un patrón de diseño de software que se utiliza para reducir el acoplamiento entre objetos y facilitar el testing unitario. En Swift, existen tres mecanismos principales para implementar la inyección de dependencias: a través del constructor, mediante una propiedad, y mediante un método.

### Inyección de dependencias mediante el constructor
En el ejemplo proporcionado, la inyección de dependencias mediante el constructor se utiliza en la clase `Mago`. La clase `Mago` tiene una dependencia de las clases `Varita` y `Hechizo`, pero en lugar de crear estas dependencias dentro de la clase `Mago`, se pasan como parámetros en el constructor de la clase.
```swift
class Mago {
    let varita: VaritaProtocolo
    let hechizo: HechizoProtocolo
    
    init(varita: VaritaProtocolo, hechizo: HechizoProtocolo) {
        self.varita = varita
        self.hechizo = hechizo
    }
}
```
De esta manera, cuando se crea un objeto de la clase `Mago`, las dependencias se pasan como argumentos en el constructor:
```swift
let varita = Varita()
let hechizo = Hechizo(nombre: "Expecto Patronum")
let harryPotter = Mago(varita: varita, hechizo: hechizo)
```

### Inyección de dependencias mediante una propiedad
Otro mecanismo para implementar la inyección de dependencias es mediante una propiedad. En el ejemplo, la propiedad `hechizoFavorito` de la clase `Mago` es un ejemplo de esto:

```swift
class Mago {
    let varita: VaritaProtocolo
    let hechizo: HechizoProtocolo
    
    // Inyección de dependencia mediante una propiedad
    var hechizoFavorito: HechizoProtocolo {
        return self.hechizo
    }
}
```
En este caso, la propiedad `hechizoFavorito` devuelve la dependencia `hechizo`, que se inyecta en la clase `Mago`.

### Inyección de dependencias mediante un método
El tercer mecanismo para implementar la inyección de dependencias es mediante un método. En el ejemplo, la función `lanzarHechizo` de la clase `Mago` es un ejemplo de esto:
```swift
class Mago {
    let varita: VaritaProtocolo
    let hechizo: HechizoProtocolo
    
    // Inyección de dependencia mediante un método
    func lanzarHechizo() -> String {
        return self.varita.lanzar(hechizo: self.hechizo)
    }
}

```
En este caso, la función `lanzarHechizo` utiliza la dependencia `varita` y `hechizo`, que se inyectan en la clase `Mago`.














