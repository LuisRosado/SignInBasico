# SignInBasico
Un ejemplo básico de un programa para iniciar sesión

El código que proporcionas implementa un sistema de autenticación básico utilizando un nombre de usuario (Usuario) y una contraseña (Contraseña). A continuación, te explico cómo funciona:

i = 0: Inicializa la variable i en 0. Esta variable se utilizará para contar la cantidad de intentos fallidos de inicio de sesión.

Usuario = 'Luis' y Contraseña = '123': Establece el nombre de usuario y la contraseña válidos para acceder al sistema.

user = '' y password = '': Inicializa las variables user y password en cadenas vacías. Estas variables se utilizarán para almacenar los valores ingresados por el usuario durante el inicio de sesión.

El código entra en un bucle while que se ejecutará mientras la combinación de nombre de usuario y contraseña ingresada por el usuario sea incorrecta (no coincida con Usuario y Contraseña) y el número de intentos fallidos sea menor a 3.

Dentro del bucle, el código solicita al usuario que ingrese su nombre de usuario y contraseña utilizando las variables user y password.

Luego, verifica si la combinación de nombre de usuario y contraseña ingresada coincide con los valores almacenados en Usuario y Contraseña. Si coincide, muestra "Bienvenido XD" y sale del bucle.

Si la combinación es incorrecta, muestra un mensaje de error, incrementa la variable i en 1 para contar el intento fallido y permite al usuario intentarlo nuevamente hasta que se cumpla alguna de las condiciones de salida del bucle.

Si el número de intentos fallidos (i) alcanza o supera 3, el sistema muestra "Su Cuenta ha sido bloqueada".

Es importante tener en cuenta que este sistema de autenticación es muy básico y no es seguro para aplicaciones en entornos reales. En un escenario real, se utilizarían métodos más robustos y seguros para gestionar la autenticación, como contraseñas encriptadas y mecanismos de bloqueo de cuentas después de varios intentos fallidos.
