
<body>
    <h1>📚 Gestor de Biblioteca - Proyecto Django</h1>
    <p>
        Este proyecto es una plataforma web desarrollada en <b>Django</b> para la gestión de una biblioteca. Permite a usuarios y bibliotecarios interactuar con un catálogo de libros, administrar géneros, editar perfiles, gestionar favoritos y enviar notificaciones por correo electrónico.
    </p>

  <div class="section">
        <h2>🔑 Funcionalidades principales</h2>
        <ul>
            <li>Registro y autenticación de usuarios.</li>
            <li>Edición de datos personales desde el perfil.</li>
            <li>Catálogo de libros con portada, autor, género y valor en saberes.</li>
            <li>Gestión de favoritos: agregar y quitar libros favoritos.</li>
            <li>Gestión de géneros: agregar, editar y eliminar géneros (solo bibliotecarios).</li>
            <li>Panel especial para bibliotecarios con:
                <ul>
                    <li>Envío de mensajes a todos, uno o varios usuarios (por email).</li>
                    <li>Modificación de saberes de usuarios.</li>
                    <li>Búsqueda avanzada de usuarios.</li>
                </ul>
            </li>
            <li>Edición y eliminación de libros (solo bibliotecarios).</li>
        </ul>
    </div>

  <div class="section">
        <h2>🗂️ Estructura del proyecto</h2>
        <ul>
            <li><b>Modelos:</b> <code>Libro</code>, <code>Genero</code>, <code>Perfil</code> (extiende <code>User</code>), etc.</li>
            <li><b>Vistas:</b> Catálogo, perfil, edición de perfil, favoritos, gestión de géneros, mensajes, etc.</li>
            <li><b>Formularios:</b> Registro, autenticación, edición de perfil, libros, géneros.</li>
            <li><b>Templates:</b> HTML con Bootstrap para una interfaz moderna y responsive.</li>
        </ul>
    </div>

  <div class="section">
        <h2>👤 Roles de usuario</h2>
        <ul>
            <li><b>Usuario:</b> Puede ver el catálogo, gestionar sus favoritos y editar su perfil.</li>
            <li><b>Bibliotecario:</b> Tiene acceso a funciones administrativas: gestión de libros, géneros, usuarios y envío de notificaciones.</li>
        </ul>
    </div>

  <div class="section">
        <h2>✉️ Envío de mensajes</h2>
        <ul>
            <li>Desde el perfil de bibliotecario se pueden enviar mensajes por email a:
                <ul>
                    <li>Todos los usuarios.</li>
                    <li>Uno o varios usuarios seleccionados.</li>
                    <li>Correos electrónicos adicionales ingresados manualmente.</li>
                </ul>
            </li>
        </ul>
    </div>

  <div class="section">
        <h2>⚙️ Tecnologías utilizadas</h2>
        <ul>
            <li>Django (backend y ORM)</li>
            <li>Bootstrap (frontend)</li>
            <li>SQLite/PostgreSQL (base de datos)</li>
            <li>Correo SMTP para notificaciones</li>
        </ul>
    </div>

  <div class="section">
        <h2>🚀 Despliegue</h2>
        <ul>
            <li>Preparado para deploy en <b>Railway</b>, <b>Render</b> o cualquier plataforma compatible con Django.</li>
            <li>Incluye <code>requirements.txt</code> y <code>Procfile</code> para despliegue rápido.</li>
        </ul>
    </div>

  <div class="section">
        <h2>📄 Instalación rápida</h2>
        <ol>
            <li>Clona el repositorio: <code>git clone ...</code></li>
            <li>Instala dependencias: <code>pip install -r requirements.txt</code></li>
            <li>Configura <code>settings.py</code> y variables de entorno.</li>
            <li>Realiza migraciones: <code>python manage.py migrate</code></li>
            <li>Ejecuta el servidor: <code>python manage.py runserver</code></li>
        </ol>
    </div>

  <div class="section">
        <h2>🙌 Créditos</h2>
        <p>
            Proyecto desarrollado por el equipo de la biblioteca.<br>
            Basado en Django 4+ y Bootstrap 5.<br>
            <b>¡Contribuciones y sugerencias son bienvenidas!</b>
        </p>
    </div>
</body>
</html>
