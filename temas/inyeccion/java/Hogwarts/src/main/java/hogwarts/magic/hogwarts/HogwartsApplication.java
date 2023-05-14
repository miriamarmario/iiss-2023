package hogwarts.magic.hogwarts;

import hogwarts.magic.hogwarts.dominio.Estudiante;
import hogwarts.magic.hogwarts.interfaces.ComportamientoEstudiante;
import hogwarts.magic.hogwarts.servicio.Servicio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
public class HogwartsApplication {

    private Servicio servicio;

    public static void main(String[] args) {
        //turn off banner and startup info and turn off the info logs
        SpringApplication app = new SpringApplication(HogwartsApplication.class);
        app.setBannerMode(org.springframework.boot.Banner.Mode.OFF);
        app.setLogStartupInfo(false);
        app.setAddCommandLineProperties(false);
        app.run(args);
    Estudiante estudiante = new Estudiante("Harry", "Potter", "Griffindor", 11);
    Servicio.realizarComportamiento(estudiante);

    }





}
