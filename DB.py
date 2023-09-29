import sqlite3
from flask import Flask, render_template, g

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello')
def hello(name=None):
    return render_template('hello.html', name=name)

#Comenzamos a hacer una conexion a una base de datos con SQLite

# Definimos la ruta de la DB
DATABASE = 'database.db'

# Conecta a la BD
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Función para cerrar la conexion

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
