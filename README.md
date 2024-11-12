Descripción General:
Este componente de React, AdminConsole, muestra una consola de administración para visualizar las sesiones de los usuarios. Los datos se obtienen de una API y se presentan en una tabla y dos gráficos de barras: uno para los clics en dos botones específicos y otro para la duración de las sesiones de los usuarios.

Credenciales de Acceso:
Administrador:

Nombre de usuario: admin
Contraseña: adminpass
Usuarios:

Nombre de usuario: user1, user2, user3, etc. (El número al final del nombre de usuario varía según el usuario)
Contraseña: password123
Estas credenciales pueden ser utilizadas para acceder al sistema, tanto para el rol de administrador como para los usuarios regulares. El administrador tiene acceso a todas las funcionalidades de la consola, mientras que los usuarios pueden visualizar sus propias sesiones y datos de clics.

Funcionamiento:
useEffect:

Se ejecuta una vez cuando el componente se monta. Hace una solicitud HTTP a la API para obtener los datos de las sesiones de los usuarios (nombre, duración de la sesión, y clics en dos botones).
Si los datos son válidos, se almacenan en el estado userData.
Tabla:

Se utiliza el componente Table de Ant Design para mostrar una tabla con las columnas definidas:
Usuario
Duración de la sesión en minutos
Clics en el Botón 1
Clics en el Botón 2
Gráficos de Barras:

El primer gráfico muestra la cantidad de clics en los Botones 1 y 2 para cada usuario.
El segundo gráfico muestra la duración de la sesión en minutos para cada usuario.
Estilos:

Se utiliza Ant Design para el layout y los componentes visuales como tablas, tarjetas, y gráficos. Los estilos se personalizan en el archivo AdminConsole.css.
Requisitos:
Ant Design: Se utilizan componentes como Layout, Table, Card, y Typography de Ant Design.
Recharts: Se usa para los gráficos de barras.
Axios: Se utiliza para hacer la solicitud a la API que devuelve los datos de las sesiones de los usuarios.


Notas:
Asegúrate de tener un backend que proporcione los datos correctos en la URL 'http://127.0.0.1:8000/api/user-sessions/' y que el formato de los datos sea el esperado (un array de objetos con propiedades como username, sessionDuration, button1Clicks, button2Clicks).
Si la API no responde o los datos son incorrectos, se mostrará un mensaje de error en la consola del navegador.
