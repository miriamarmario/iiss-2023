package hogwarts.magic.hogwarts.servicio;

import hogwarts.magic.hogwarts.dominio.Estudiante;
import hogwarts.magic.hogwarts.interfaces.ComportamientoEstudiante;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;
@Component
public class Servicio {
    @Autowired
    public Servicio (@Qualifier("Slytherin") ComportamientoEstudiante comportamiento) {
        Servicio.comportamiento = comportamiento;
    }
    private static ComportamientoEstudiante comportamiento;
    public static void realizarComportamiento(Estudiante estudiante) {
        comportamiento.hacerAlgo(estudiante);
    }
}

