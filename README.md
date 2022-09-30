# Django Crud App

---
Esta aplicacion fue desarrollada utilizando el lenguaje de programación **Python** con el framework **Django** y el motor de bases de datos **PostgresQl**. Se tulizó la libreria de CSS **Bootstrap** para darle el estilo a la pagina y **Alpine Js** para otorgarle interactividad.
Consiste en un pequeño sistema para administrar productos y sus categorias.

### Tecnologías Utilizadas

- Python
- Django
- PostgresQl
- HTML
- Bootstrap
- JavaScript
- Alpine Js
- Git
- Docker

### URLs Configuradas

- `/`
- `/categorias`

### Plantillas

- `base.html`
- `inicio.html`
- `categorias.html`

### Variables de Entorno

- SECRET_KEY (OBLIGATORIO): Llave secreta utilizada por Django para generar hashes. Crear en `.env` en directorio base del proyecto.
- PORT (OBLIGATORIO): Puerto en el que se ejecutará el servidor de Django
- DEBUG (OPCIONAL): Valor utilizado para activar o desactivar modo DEBUG de Django
- POSTGRES_NAME (OBLIGATORIO): Nombre de la base de datos de PostgresQL
- POSTGRES_USER (OBLIGATORIO): Nombre de usuario para acceder a PostgresQL
- POSTGRES_PASSWORD (OBLIGATORIO): Contraseña para acceder a PostgresQL
- POSTGRES_HOST (OBLIGATORIO): Nombre del host de la Base de Datos
- POSTGRES_PORT (OBLIGATORIO): Puerto en el que se está ejecutando la Base de Datos

### Ejecución
  
 ```bash
 docker-compose build .
 ```
 ```bash
 docker-compose up
 ```
 
