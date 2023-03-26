## Anotaciones en Swift
En el código he hecho uso de diferentes mecanismos de anotaciones en Swift. Vamos a explicar cada una.

### Anotación `@available`

La anotación `@available` se utiliza para indicar si una función, clase, propiedad o método está disponible para una versión específica de Swift o de una plataforma en particular. En el ejemplo presentado, se utiliza esta anotación para indicar que la propiedad `nombreCasa` en la clase `Estudiante` está en desuso y que se debe utilizar la propiedad `casa` en su lugar para acceder a la casa del estudiante. El uso de esta anotación se muestra a continuación:

```swift
@available(*, deprecated, message: "Utilizar la propiedad 'casa' en lugar de 'nombreCasa' para acceder a la casa del estudiante")
var nombreCasa: String {
    return self.casa.nombre
}
```



En este caso, se indica que la propiedad está en desuso con la etiqueta `deprecated` y se proporciona un mensaje explicativo para el desarrollador. El asterisco en la primera posición indica que la anotación se aplica a todas las plataformas.
### Anotación `@objcMembers`

La anotación `@objcMembers` se utiliza para que todos los miembros de una clase o estructura sean expuestos a Objective-C. En el ejemplo presentado, se utiliza esta anotación en la clase `Casa` para que la clase y sus propiedades sean accesibles desde Objective-C. El uso de esta anotación se muestra a continuación:

```swift
@objcMemebers
class Casa: NSObject {
    let nombre: String
    
    init(nombre: String) {
        self.nombre = nombre
    }
}
```


### Anotación `@objc`

La anotación `@objc` se utiliza para indicar que una clase, protocolo, propiedad o método se expone a Objective-C. En el ejemplo presentado, se utiliza esta anotación en la clase `Hechizo` y en el protocolo `HabilidadMagica` para que sean accesibles desde Objective-C. El uso de esta anotación se muestra a continuación:

```swift
@objc protocol HabilidadMagica {
    var nombreHabilidad: String { get }
    func realizarHabilidadMagica()
}

class Hechizo: NSObject, HabilidadMagica {
    @objc let nombreHabilidad: String
    let descripcion: String
    
    init(nombre: String, descripcion: String) {
        self.nombreHabilidad = nombre
        self.descripcion = descripcion
    }
    
    @objc func realizarHabilidadMagica() {
        print("¡\(self.nombreHabilidad)!")
    }
}
```


### Conclusión

Las anotaciones de Swift son una herramienta útil para indicar información adicional sobre las clases, métodos y propiedades de una aplicación. En el ejemplo presentado se han utilizado varias anotaciones para indicar la disponibilidad de ciertas características en diferentes plataformas, la exposición de clases y métodos a Objective-C, y la deprecación de una propiedad en favor de otra. El uso correcto de estas anotaciones puede mejorar la legibilidad y el mantenimiento del código de una aplicación.
