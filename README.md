**DOCUMENTACION M12 A01**

# Setup

## Python Virtual Environment

Crear entorno:

    python3 -m venv .venv

Entrar en el entorno:

    source .venv/bin/activate

**En caso de que no se active el entorno, es por que no esta creado, el entorno esta como excepcion en el .gitignore**

Instala el Flask:

    pip install -U flask

Para generar el fichero de requisitos:

    pip freeze > requirements.txt

Instala el requisito:

    pip install -r requirements.txt

Para salir del entorno Python:

    deactivate

## Para arrancar aplicacion:
    flask --app hello.py run

## Base de datos

Creamos un archivo llamado **schema.sql** y en SQLite creamos una Base de Datos y ejecutamos el codigo SQL del archivo y guardamos la Base de datos en un archivo llamado **database.db**.

