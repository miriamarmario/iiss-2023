// Anotación personalizada para definir la casa de un estudiante
@available(*, deprecated, message: "Utilizar la propiedad 'casa' en lugar de 'nombreCasa' para acceder a la casa del estudiante")
@objcMembers
class Casa: NSObject {
    let nombre: String
    
    init(nombre: String) {
        self.nombre = nombre
    }
}

// Anotación para definir una clase con habilidades mágicas
@objc protocol HabilidadMagica {
    var nombreHabilidad: String { get }
    func realizarHabilidadMagica()
}

// Implementación de la clase Hechizo con anotaciones
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

// Implementación de la clase Estudiante con anotaciones
class Estudiante: NSObject {
    let nombre: String
    let casa: Casa
    
    init(nombre: String, casa: Casa) {
        self.nombre = nombre
        self.casa = casa
    }
    
    @available(*, deprecated, message: "Utilizar la propiedad 'casa' en lugar de 'nombreCasa' para acceder a la casa del estudiante")
    var nombreCasa: String {
        return self.casa.nombre
    }
}

// Uso de las clases con anotaciones para crear objetos
let casaGryffindor = Casa(nombre: "Gryffindor")
let harry = Estudiante(nombre: "Harry Potter", casa: casaGryffindor)
let lumosMaxima = Hechizo(nombre: "Lumos Maxima", descripcion: "Ilumina con fuerza tu varita")

// Ejecución de habilidades mágicas con anotaciones
lumosMaxima.realizarHabilidadMagica()
