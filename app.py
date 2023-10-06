from flask import Flask, request, abort, render_template, redirect, url_for
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
        #res = con.execute("SELECT id, title, price FROM products ORDER BY id ASC")
        res = con.execute("SELECT * FROM products ORDER BY id ASC")
        products = res.fetchall()

    return render_template('products/list.html', products = products)

# Controlador
@app.route('/products/create', methods=["GET", "POST"])
def products_create():
	if request.method == 'GET':
		# Show form
		return render_template('products/create.html')
	elif request.method == 'POST':
		# Get POST data
		data = request.form
		# TODO Validate data
		# TODO Generate data
		# TODO Save data (database insert)
		# Redirect to list page

		#Recibe del Post los datos
		title = str(request.form['title'])
		description = request.form['description']
		photo = request.form['photo']
		price = float(request.form['price'])
		category_id = request.form['category_id']
		seller_id = request.form['seller_id']
		#Valida
		if len(title) > 255 or len(title) == 0:
			return render_template('products/create.html', "No se cumplen las condiciones")
		else:
			with get_db_connection() as ins:
				inserte = """INSERT INTO products (title, description, photo, price, category_id, seller_id, created, updated) VALUES  ( ?, ?, ?, ?, ?, ?, DATETIME('now'), DATETIME('now'))"""
				tupla = title, description, photo, price, category_id, seller_id
				ins = ins.execute(inserte, tupla)
				products = ins.fetchall()
			return redirect(url_for('products_list')) 
	else:
		# Not found response
		abort(404)

@app.route('/products/update/<int:id>')
def products_update(id):
   # TODO Everything
    return