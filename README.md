**DOCUMENTACION M12 A01**

## Setup

### Python Virtual Environment

Arrancar entorno:
    python3 -m venv .venv

Activa:
    . bin/activate

Instala el requisito:
    pip install -r requirements.txt

Para generar el fichero de requisitos:
    pip freeze > requirements.txt
Para salir del entorno Python:
    deactivate

#Para arrancar aplicacion:
##Hola Mundo:
    flask --app hello.py run
##Y para el Templates:
    flask --app hello_Templates.py run
