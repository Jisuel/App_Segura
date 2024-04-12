DOCUMENTACIÓN DETALLADA SOBRE LAS MEDIDAS DE SEGURIDAD IMPLEMENTADAS

1.	Hashing de Contraseñas
Las contraseñas de los usuarios se almacenan en la base de datos en forma de hash utilizando el algoritmo bcrypt. Esto ayuda a proteger las contraseñas originales de cualquier exposición en caso de que la base de datos sea comprometida.

2.	Cifrado de Contraseñas en Repositorio
Las contraseñas de los usuarios almacenadas en la tabla "contraseñas" se cifran utilizando Fernet, que proporciona cifrado simétrico. Esto protege las contraseñas en repositorio y garantiza que no sean visibles incluso si la base de datos es comprometida.

3.	Autenticación de Usuario
Se utiliza el paquete Flask-Login para gestionar la autenticación de usuario. Esto asegura que solo los usuarios autenticados puedan acceder a ciertas rutas y funcionalidades dentro de la aplicación.

4.	Seguridad de la Sesión
La clave secreta utilizada para firmar las sesiones de usuario se mantiene segura en el servidor y no se comparte con el cliente. Esto garantiza que las sesiones de usuario no puedan ser manipuladas o falsificadas.

5.	Verificación de Permisos
Se implementa una lógica para verificar que los usuarios solo puedan acceder, modificar o eliminar sus propias contraseñas, evitando así que accedan a recursos o datos de otros usuarios.

6.	Protección contra Exposición de Claves de Cifrado
Las claves de cifrado utilizadas para proteger las contraseñas en repositorio se almacenan de forma segura en el código del servidor y no se exponen públicamente. Se siguen prácticas recomendadas para proteger estas claves y evitar su divulgación.
