# Clase que representa a un personaje de Harry Potter.
class Personaje
  attr_accessor :nombre, :casa, :edad

  # Inicializa una nueva instancia de la clase Personaje.
  #
  # @param [String] nombre El nombre del personaje.
  # @param [String] casa La casa de Hogwarts a la que pertenece el personaje.
  # @param [Integer] edad La edad del personaje.
  def initialize(nombre, casa, edad)
    @nombre = nombre
    @casa = casa
    @edad = edad
  end

  # Método que hace que el personaje realice un hechizo.
  #
  # @param [String] hechizo El nombre del hechizo que se va a realizar.
  # @param [String] objetivo El objetivo sobre el que se va a realizar el hechizo.
  # @return [String] El resultado de la realización del hechizo.
  def hacer_hechizo(hechizo, objetivo)
    return "#{@nombre} realizó el hechizo #{hechizo} sobre #{objetivo}."
  end


# Método que ha quedado obsoleto y no debe utilizarse.
#
# @deprecated
def pocion_obsoleta
  return "Esta poción está obsoleta y no debe utilizarse... Puede afectar a la tripa"
end

# Método que lanza una excepción cuando se llama.
#
# @raise [RuntimeError] Siempre lanza una excepción.
def hechizo_imperdonable
  if @casa != "Slytherin"
    raise "Tu moral no permite hacer este hechizo."
  end
  return "Convierte a los humanos en piedra."

  end
end


#Prueba del ejemplo
harry = Personaje.new("Harry Potter", "Gryffindor", 17)
puts harry.hacer_hechizo("Expecto Patronum", "Dementores")
puts harry.hacer_hechizo("Avada Kedavra", "Voldemort")
puts harry.hacer_hechizo("Flipendo", "Ron")
puts harry.pocion_obsoleta
draco = Personaje.new("Draco Malfoy", "Slytherin", 17)
puts draco.hacer_hechizo("Avada Kedavra", "Albus Dumbledore")
puts draco.hechizo_imperdonable
puts harry.hechizo_imperdonable

