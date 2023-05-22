module Anuncio
  def self.included(base)
    base.extend(ClassMethods)
  end

module ClassMethods
  def anunciar_metodo(*metodos)
    metodos.each do |metodo|
      original_method = instance_method(metodo)
      define_method metodo do |*args, &block|
        # Imprimir anuncio
        puts "#{metodo} va a ejecutarse con los parametros #{args.inspect}"

        # Imprimir solo el código de la función
        if original_method.source_location
          file, line = original_method.source_location
          if file && line
            puts "Código de #{metodo}:"
            File.open(file, 'r') do |f|
              f.each_line.with_index do |linea, numero|
                if (numero+1) >= line && !linea.strip.empty?
                  break if linea.include?("end")
                  puts "#{numero+1}: #{linea}"
                end
              end
            end
          end
        end

        # Llamar al método original
        original_method.bind(self).call(*args, &block)
      end
    end
  end
end
end

class AtrapadorDeCriaturas
  include Anuncio

  def lanzar_red(criatura, ubicacion)
    puts "¡Lanzando red para atrapar a #{criatura} en #{ubicacion}!"
  end

  def usar_varita(hechizo, objetivo)
    puts "¡Usando hechizo #{hechizo} para atrapar a #{objetivo}!"
  end

  anunciar_metodo :lanzar_red, :usar_varita
end


atrapador = AtrapadorDeCriaturas.new

atrapador.lanzar_red("hipogrifo", "Bosque Prohibido")
# => Lanzando red para atrapar a hipogrifo en Bosque Prohibido!

atrapador.usar_varita("Expelliarmus", "niffler")
# => Usando hechizo Expelliarmus para atrapar a niffler!