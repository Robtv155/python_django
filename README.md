
# Instrucciones para el Proyecto Django

Este repositorio contiene un proyecto Django que puedes clonar y ejecutar localmente. A continuación, se describen los pasos para configurar el entorno y poner en marcha el servidor.

## 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/Robtv155/python_django.git
cd mi_pagina_web
```

## 2. Crear un entorno virtual (venv)

Es recomendable crear un entorno virtual para gestionar las dependencias del proyecto. Ejecuta los siguientes comandos:

```bash
python -m venv venv
```

Activa el entorno virtual:


```bash
.\venv\Scripts\activate
```

## 3. Instalar las dependencias

Con el entorno virtual activado, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## 4. Migrar la base de datos

Realiza las migraciones de la base de datos para crear las tablas necesarias:

```bash
python manage.py migrate
```

## 5. Crear un superusuario

Para poder acceder al panel de administración de Django, crea un superusuario:

```bash
python manage.py createsuperuser
```

Sigue las indicaciones en la terminal para configurar el nombre de usuario, correo electrónico y contraseña del superusuario.

## 6. Ejecutar el servidor

Finalmente, ejecuta el servidor de desarrollo de Django con la opción `--nostatic` para evitar que el servidor sirva archivos estáticos (se está utilizando WhiteNoise como configuración personalizada para los archivos estáticos):

```bash
python manage.py runserver --nostatic
```

El servidor se iniciará en `http://127.0.0.1:8000/`. Puedes acceder a la página web o a la administración en `http://127.0.0.1:8000/admin/` con las credenciales del superusuario que creaste.
