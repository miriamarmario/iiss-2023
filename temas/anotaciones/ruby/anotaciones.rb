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

  def profesor_only
    @_profesor = true
  end
end

# Example usage

class User
  attr_reader :admin

  def initialize(admin = false)
    @admin = admin
  end

  def admin?
    @admin
  end

  profesor_only # ESTO ES LO QUE ANOTA LOS METODOS QUE SE DEFINAN A PARTIR DE AQUI
  #LOS METODOS QUE SE DEFINAN A PARTIR DE AQUI SOLO PODRAN SER EJECUTADOS POR PROFESORES DE ARTES OSCURAS

  def hechizo1
    puts "AVADA KEDAVRA"
  end

  def hechizo2
    puts "CRUCCIO"
  end
end

user = User.new(true)

# example of the code
user.hechizo1
user.hechizo2

user2 = User.new
user2.hechizo1
user2.hechizo2