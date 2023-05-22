// Definir el protocolo 
protocol MagoOscuroDelegado: class {
    func magiaOscura()
}
// Clase que realiza magia oscura
class MagoOscuro {
    weak var delegate: MagoOscuroDelegado?
    
    func lanzarHechizo() {
        delegate?.magiaOscura()
    }
}
// Clase que implementa el protocolo de delegado
class DeathEater: MagoOscuroDelegado {
    func magiaOscura() {
        print("¡Morsmordre!")
    }
}

// Otra clase que implementa el protocolo de delegado
class Snape: MagoOscuroDelegado {
    func magiaOscura() {
        print("¡Avada Kedavra!")
    }
}

// Crear instancias de las clases
let mago = MagoOscuro()
let mortifago = DeathEater()
let snape = Snape()

// Asignar los delegados
mago.delegate = mortifago
mago.lanzarHechizo() // Salida: ¡Morsmordre!

mago.delegate = snape
mago.lanzarHechizo() // Salida: ¡Avada Kedavra!