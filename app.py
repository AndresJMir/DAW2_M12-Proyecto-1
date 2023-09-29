from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# afegeixo els paràmetres del config.py
#app.config.from_object("config.Config")

def get_db_connection():
    sqlite3_database_path = "database.db"
    con = sqlite3.connect(sqlite3_database_path)
    # https://docs.python.org/3/library/sqlite3.html#how-to-create-and-use-row-factories
    con.row_factory = sqlite3.Row
    return con

@app.route('/')
def init():
    return redirect(url_for('products_list'))

@app.route('/products/list')
def products_list():
    with get_db_connection() as con:
        res = con.execute("SELECT id, title, price FROM products ORDER BY id ASC")
        products = res.fetchall()

    return render_template('products/list.html', products = products)