package hogwarts.magic.hogwarts.implementaciones;

import hogwarts.magic.hogwarts.dominio.Estudiante;
import hogwarts.magic.hogwarts.interfaces.ComportamientoEstudiante;
import org.springframework.stereotype.Component;

@Component("Ravenclaw")
public class ComportamientoRavenclaw implements ComportamientoEstudiante {

    @Override
    public void hacerAlgo(Estudiante estudiante) {
        System.out.println(estudiante.getNombre() + " " + estudiante.getApellido() + " de la casa " + estudiante.getCasa() + " ha demostrado su inteligencia al resolver un complicado acertijo.");
    }
}