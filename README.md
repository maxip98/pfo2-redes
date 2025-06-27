
PFO 2 - Sistema de Gestión de Tareas con API y Base de Datos

Este proyecto consiste en una API RESTful desarrollada con Flask que permite registrar usuarios, iniciar sesión y mostrar una página HTML de bienvenida.

Tecnologías utilizadas:

    - Python 3.x

    - Flask

    - SQLite

    - Werkzeug (para hash de contraseñas)

Instrucciones para ejecutar el proyecto

1. Clonar el repositorio

git clone https://github.com/usuario/tu-repo.git
cd tu-repo

(Reemplazar “usuario/tu-repo” por tu nombre de usuario y nombre real del repositorio)

2. Crear entorno virtual (opcional pero recomendado)

python -m venv venv
(Linux/macOS) source venv/bin/activate
(Windows) venv\Scripts\activate

3. Instalar dependencias

pip install flask werkzeug

4. Ejecutar el servidor

python servidor.py

El servidor quedará activo en http://localhost:5000

Cómo probar los endpoints

Podés usar Postman, Insomnia o curl. A continuación, algunos ejemplos:
Registro de usuario

    Endpoint: POST /registro

    URL: http://localhost:5000/registro

    Cuerpo JSON:

{
"usuario": "maxi",
"contraseña": "1234"
}

Respuesta esperada:

{
"mensaje": "Usuario registrado exitosamente"
}

Inicio de sesión

    Endpoint: POST /login

    URL: http://localhost:5000/login

    Cuerpo JSON:

{
"usuario": "maxi",
"contraseña": "1234"
}

Respuesta esperada:

{
"mensaje": "Bienvenido, maxi"
}
Página de bienvenida

    Endpoint: GET /tareas

    URL: http://localhost:5000/tareas

    Se puede acceder desde el navegador o con curl

Resultado: Página HTML con mensaje de bienvenida

Capturas de pantalla

Las pruebas exitosas se encuentran en la carpeta capturas/:

    registro_ok.jpg

    login_ok.jpg

    tareas.jpg

GitHub Pages

Este repositorio está acompañado por una página en GitHub Pages donde se encuentra esta misma documentación para consulta rápida:
https://usuario.github.io/tu-repo/

(Activar GitHub Pages desde “Settings > Pages” en el repositorio si se desea usar)

👤 Autor

    Pereyra Maximiliano

Materia: Programacion sobre redes
Carrera: Tecnicatura Superior en Desarrollo de Software
Año: 2025