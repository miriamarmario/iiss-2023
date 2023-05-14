package hogwarts.magic.hogwarts.implementaciones;

import hogwarts.magic.hogwarts.dominio.Estudiante;
import hogwarts.magic.hogwarts.interfaces.ComportamientoEstudiante;
import org.springframework.stereotype.Component;

@Component("Hufflepuff")
public class ComportamientoHufflepuff implements ComportamientoEstudiante {

    @Override
    public void hacerAlgo(Estudiante estudiante) {
        System.out.println(estudiante.getNombre() + " " + estudiante.getApellido() + " de la casa " + estudiante.getCasa() + " ha mostrado su lealtad al ayudar a un compañero de clase en apuros.");
    }
}

