# Inyección de dependencias en Java con Spring

Este código muestra un ejemplo de inyección de dependencias en Java utilizando Spring Framework. En este proyecto llamado "Hogwarts", se tiene una clase principal llamada `HogwartsApplication` que es la que se encarga de ejecutar la aplicación. En la clase `HogwartsApplication`, se inicializa un objeto de la clase `Servicio`, que es la que se encargará de realizar un comportamiento específico dependiendo del tipo de estudiante que se tenga.

La clase `Servicio` es una clase que tiene un método estático llamado `realizarComportamiento`, que recibe como parámetro un objeto de la clase `Estudiante`. Este método llama al método `hacerAlgo` del objeto que implementa la interfaz `ComportamientoEstudiante`, que es una interfaz que define un comportamiento que se realiza dependiendo del tipo de estudiante. Esta implementación de `ComportamientoEstudiante` se pasa a la clase `Servicio` a través de la inyección de dependencias.

En la clase `Servicio`, se utiliza la anotación `@Autowired` para indicar que se está inyectando una dependencia. También se utiliza la anotación `@Qualifier` para indicar qué implementación de la interfaz `ComportamientoEstudiante` se va a utilizar. En este caso, se utiliza la implementación de `ComportamientoEstudiante` con el nombre "Slytherin".

```java
 @Autowired
    public Servicio (@Qualifier("Slytherin") ComportamientoEstudiante comportamiento) {
        Servicio.comportamiento = comportamiento;
    }
```

En las clases que implementan la interfaz `ComportamientoEstudiante`, se utiliza la anotación `@Component` para indicar que es un componente que puede ser inyectado como una dependencia. El texto que le sigue es el nombre que se le va a dar a ese componente. Esto se usa para especificar un componente a la hora de inyectar una dependecia, utilizando `@Qualifier`. Un ejemplo en el código es el siguiente:

```java
@Component("Ravenclaw")
public class ComportamientoRavenclaw implements ComportamientoEstudiante {

    @Override
    public void hacerAlgo(Estudiante estudiante) {
        System.out.println(estudiante.getNombre() + " " + estudiante.getApellido() + " de la casa " + estudiante.getCasa() + " ha demostrado su inteligencia al resolver un complicado acertijo.");
    }
}
```

Finalmente, se tiene la clase `Estudiante`, que simplemente representa a un estudiante de Hogwarts con su nombre, apellido, casa y edad.

El archivo `pom.xml` es el archivo de configuración de Maven para el proyecto. En este archivo se especifican las dependencias del proyecto y otra información necesaria para la construcción del proyecto.

Este ejemplo muestra cómo se puede utilizar la inyección de dependencias en Java utilizando Spring Framework. Con esto, se puede desacoplar las dependencias entre clases y hacer que el código sea más fácil de mantener y extender.

## Ejecutar el proyecto
Para ejecutar el proyecto debemos realizar una ejecución del ciclo de vida de un proyecto `Maven` para que se genere el empaquetado .jar . Para ello, usamos los siguientes comandos:
```shell
mvn install -DskipTests
```
El -DskipTests no es necesario, pero se salta los test de prueba que pueden dar fallo. En este caso no hay test, así que ejecutandolo sin más estaría bien.

Ésto generará una carpeta target donde habra generado recursos entre los que se encuentra el proyecto ejecutable. Para probar este codigo cambiando el `Qualifier` es necesario repetir este proceso o disponer de un ide como `Eclipse`, `VScode` o `Intellij Idea` que permita autoindexar el codigo y ejecutarlo sin utilizar maven. El código se ejecuta lanzando este comando:

```
java -jar target/Hogwarts-0.0.1-SNAPSHOT.jar
```