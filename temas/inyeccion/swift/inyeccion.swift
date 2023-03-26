// Protocolo para la clase Varita
protocol VaritaProtocolo {
    func lanzar(hechizo: HechizoProtocolo) -> String
}

// Implementación de la clase Varita
class Varita: VaritaProtocolo {
    func lanzar(hechizo: HechizoProtocolo) -> String {
        return "¡Expecto Patronum!"
    }
}

// Protocolo para la clase Hechizo
protocol HechizoProtocolo {
    var nombre: String { get }
}

// Implementación de la clase Hechizo
class Hechizo: HechizoProtocolo {
    var nombre: String
    
    init(nombre: String) {
        self.nombre
 = nombre

    }
}

// Implementación de la clase Mago
class Mago {
    let varita: VaritaProtocolo
    let hechizo: HechizoProtocolo
    
    // Inyección de dependencia mediante el constructor
    init(varita: VaritaProtocolo, hechizo: HechizoProtocolo) {
        self.varita = varita
        self.hechizo = hechizo
    }
    
    // Inyección de dependencia mediante una propiedad
    var hechizoFavorito: HechizoProtocolo {
        return self.hechizo
    }
    
    // Inyección de dependencia mediante un método
    func lanzarHechizo() -> String {
        return self.varita.lanzar(hechizo: self.hechizo)
    }
}

// Uso de las clases para crear un objeto de tipo Mago
let varita = Varita()
let hechizo = Hechizo(nombre: "Expecto Patronum")
let harryPotter = Mago(varita: varita, hechizo: hechizo)

// Prueba de que la inyección de dependencias funciona correctamente
print(harryPotter.hechizoFavorito.nombre)
print(harryPotter.lanzarHechizo())