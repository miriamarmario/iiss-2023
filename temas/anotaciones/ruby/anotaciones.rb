class Module
  def method_added(name)

    #Imprime introduzca la contraseña
    if @_profesor.nil?
    puts "Introduzca la contraseña"
    #Lee la contraseña
    password = gets.chomp

    #Si la contraseña es correcta
    if password == "sorbete_de_limon" 
      @_profesor = true
    else
      @_profesor = false
    end
  end
    unless @_profesor.nil? or @_proxy_method
      @_proxy_method = true
      alias_method "admin#{name}", name
      module_eval <<-STRING
        def #{name}(*args, &block)
          admin#{name}(*args, &block) if @_profesor
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

  def hechizo               #lo podran hacer todos los magos
    puts "ALOHOMORA"
  end

  profesor_only             #a partir de aqui solo los que sepan la contrasela

  def hechizo1
    puts "CRUCCIO"
  end

  def hechizo2
    puts "AVADA KEDAVRA "
  end
end

class EscobaVoladora

  profesor_only
  def volar()
    puts "vuela vuela"
  end
end

user = User.new(true)

user.hechizo1
user.hechizo2

escoba= EscobaVoladora.new

escoba.volar