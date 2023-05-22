class Module
  def method_added(name)
    unless @_profesor.nil? or @_proxy_method
      @_proxy_method = true
      alias_method "admin#{name}", name
      module_eval <<-STRING
        def #{name}(*args, &block)
          admin#{name}(*args, &block) if admin?
        end
      STRING
      @_proxy_method = false
    end
  end

  def Anotacion_profesor_ONLY     #anotacion
    @_profesor = true
  end

end

# como se usa

class User
  attr_reader :admin

  def initialize(admin = false)
    @admin = admin
  end

  def admin?
    @admin
  end

  def hechizo         #este hechizo lo puede realizar todo el mundo
    puts "ALOHOMORA"
  end

  Anotacion_profesor_ONLY
  # ESTO ES LO QUE ANOTA LOS METODOS QUE SE DEFINAN A PARTIR DE AQUI
  #LOS METODOS QUE SE DEFINAN A PARTIR DE AQUI SOLO PODRAN SER EJECUTADOS POR PROFESORES DE ARTES OSCURAS

  def hechizo1
    puts "AVADA KEDAVRA"
  end

  def hechizo2
    puts "CRUCCIO"
  end
end

user = User.new(true) #si puede hacer los hechizos
user.hechizo
user.hechizo1
user.hechizo2

user2 = User.new 
user2.hechizo  #este es el unico hechizo que puede hacer, ya que está definido antes de la anotacion
user2.hechizo1 #no puede hacer los hechizos porque no es profesor
user2.hechizo2