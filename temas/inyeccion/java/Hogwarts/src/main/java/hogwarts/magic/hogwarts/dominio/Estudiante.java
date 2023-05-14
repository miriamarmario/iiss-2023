package hogwarts.magic.hogwarts.dominio;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class Estudiante {
    private String nombre;
    private String apellido;
    private String casa;
    private int edad;

    public Estudiante(String nombre, String apellido, String casa, int edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.casa = casa;
        this.edad = edad;
    }

}
