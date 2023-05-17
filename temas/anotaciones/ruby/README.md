# Anotaciones en Ruby


La clase `Module` es el punto de partida de este ejemplo. Dentro de esta clase, se define el método `method_added`, que se ejecutará automáticamente cada vez que se defina un nuevo método en una clase que incluye este módulo. 

Dentro de `method_added`, se realiza una verificación para asegurarse de que el método no haya sido añadido anteriormente y que no se esté ejecutando en el contexto de un método proxy. Si se cumplen estas condiciones, se crea un alias del método original agregando el prefijo "admin" al nombre del método, lo que permite conservar una referencia al método original. 

Luego, se define un nuevo método utilizando `module_eval`, el cual reemplazará al método original. Este nuevo método verifica si el usuario actual es un administrador llamando al método `admin?`. Si el usuario es un administrador, se ejecuta el método original a través del alias creado previamente. En resumen, se está creando un mecanismo de proxy para interceptar la ejecución de los métodos y aplicar la lógica de verificación de administrador.

Además, se proporciona el método `profesor_only` que se utiliza como anotación para marcar el punto a partir del cual los métodos definidos en la clase solo pueden ser ejecutados por profesores de Artes Oscuras. Este método establece la variable de instancia `@_profesor` como `true`, lo que indica que los métodos siguientes solo estarán disponibles para los administradores.

La clase `User` tiene un atributo `admin` y se inicializa con un valor booleano que indica si el usuario es un administrador o no. También se definen los métodos `admin?`, `hechizo1` y `hechizo2`. Antes de los métodos `hechizo1` y `hechizo2`, se llama al método `profesor_only`, lo que significa que estos dos métodos solo podrán ser ejecutados por usuarios que sean profesores de Artes Oscuras, es decir, aquellos que tengan el atributo `admin` establecido como `true`.

Se crea una instancia de `User` llamada `user` con el atributo `admin` establecido como `true`, lo que le otorga acceso a los métodos `hechizo1` y `hechizo2`. Al ejecutar estos métodos en `user`, se imprime el mensaje correspondiente.

Después, se crea otra instancia de `User` llamada `user2` sin especificar el atributo `admin`, lo que significa que `user2` no es un profesor de Artes Oscuras y, por lo tanto, no tiene acceso a los métodos `hechizo1` y `hechizo2`. Al intentar ejecutar estos métodos en `user2`, se lanzará un error.

