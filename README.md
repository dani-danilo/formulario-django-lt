# Validador de Contraseña Segura

Este es un sistema web básico para la validación de contraseñas seguras siguiendo condiciones específicas: la contraseña debe tener na minúscula, una mayúscula, un número, un caracter especial, y debe contener más de 8 caracteres.

## Requisitos

- Python 3.8 o superior
- Django 4.2 o superior

## Instalación

1. **Clona el repositorio y entra a la carpeta del proyecto:**

   ```bash
   git clone <URL-del-repositorio>
   cd formulario_django
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # En Windows
   # source venv/bin/activate   # En Linux/Mac
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuración de la base de datos

Por defecto, el proyecto utiliza SQLite, por lo que no necesitas configuración adicional para pruebas locales.

## Migraciones iniciales

Ejecuta los siguientes comandos para crear las tablas en la base de datos, en caso de que las necesites:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Ejecutar la aplicación

Inicia el servidor de desarrollo con:

```bash
python manage.py runserver
```

Accede a la aplicación en [http://localhost:8000/](http://localhost:8000/)  

## Funcionalidades

- Registrar usuario con contraseña.
