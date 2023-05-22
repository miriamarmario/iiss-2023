# Anotaciones en Ruby

Las anotaciones en Ruby son una forma de agregar metadatos o información adicional a las clases y métodos. En el ejemplo, se utiliza una anotación personalizada llamada `profesor_only` para restringir el acceso a ciertos métodos únicamente a profesores.

La clase `Module` define un método llamado `method_added` que se ejecuta cada vez que se añade un nuevo método a una clase. Se realizan una serie de pasos. Para empezar, se verifica si la variable `@_profesor` es nula. Si es así, se imprime el mensaje "Introduzca la contraseña" para solicitar al usuario que ingrese una contraseña, que se almacena en `password`. Si la contraseña es correcta,  se establece la variable `@_profesor` como verdadera; de lo contrario, se establece como falsa.

Luego, se utiliza la anotación `profesor_only` para marcar los métodos que solo deben ser accesibles para los profesores. Esta anotación simplemente establece la variable `@_profesor` como verdadera.

Dentro del método `method_added`, se agrega un alias para el método recién definido, precediendo su nombre con "admin". Luego, se crea una versión modificada del método que solo se ejecutará si `@_profesor` es verdadero.

El resultado es que los métodos definidos después de la anotación `profesor_only` solo podrán ser ejecutados si la contraseña ingresada es correcta y `@_profesor` es verdadera.

Para probarlo se muestra una clase `User` y una clase `EscobaVoladora`. Ambas clases usan la anotación `profesor_only`, lo que significa que los métodos definidos después de la anotación solo podrán ser ejecutados por profesores.

La instancia de `User` tiene acceso a los métodos `hechizo1` y `hechizo2`, mientras que la instancia de `EscobaVoladora` tiene acceso al método `volar`. Sin embargo, se requiere que la contraseña sea ingresada correctamente antes de ejecutar los métodos restringidos.

