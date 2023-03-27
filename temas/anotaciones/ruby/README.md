- # Anotaciones en Ruby

Las anotaciones en Ruby son comentarios que permiten documentar el código de manera estructurada. Estos comentarios son interpretados por herramientas como RDoc para generar documentación automática en distintos formatos.

Las anotaciones en Ruby se escriben con el símbolo `#` y se ubican justo encima de la clase, método o atributo que se desea documentar. A continuación, se muestra un ejemplo de anotaciones en Ruby:

```ruby
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
```



En este ejemplo, se puede ver cómo se han utilizado las anotaciones para documentar la clase `Personaje` y los métodos `initialize`, `hacer_hechizo`, `pocion_obsoleta` y `hechizo_imperdonable`. A continuación, se explican algunas de las anotaciones utilizadas: 

- `# @param [String] nombre El nombre del personaje.`: Esta anotación indica el tipo de dato y el nombre del parámetro `nombre` que recibe el método `initialize`. 
- `# @return [String] El resultado de la realización del hechizo.`: Esta anotación indica el tipo de dato que devuelve el método `hacer_hechizo`. 
- `# @deprecated`: Esta anotación indica que el método `pocion_obsoleta` ha quedado obsoleto y no debe utilizarse. 
- `# @raise [RuntimeError] Siempre lanza una excepción.`: Esta anotación indica que el método `hechizo_imperdonable` lanza una excepción cuando se llama.

## RDoc
Para generar la documentación de un proyecto en Ruby, se puede utilizar la herramienta RDoc. Esta herramienta permite generar documentación en distintos formatos, como HTML, PDF, etc. Para instalar RDoc, se debe ejecutar el siguiente comando:

```
    gem install rdoc
    rdoc main.rb
```

La documentación generada por RDoc se puede visualizar en el navegador web. Para ello, se debe abrir el archivo `index.html` que se encuentra en la carpeta `doc`. ![capturaRdoc](.\Captura.png)

