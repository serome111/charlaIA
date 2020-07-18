#como determinar una palabra que corta

#quiza requiera pip install -U flask-cors
from flask import Flask, render_template, request,redirect,url_for,jsonify,make_response
from flask_mysqldb import MySQL
import cerebro as cr

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'CharlaIA'
mysql = MySQL(app)

@app.route('/')
def Index():
	return render_template('setup.html')

@app.route('/sistema')
def sistema():
	print('apagando el sistema')
	#return url_for("index.html")
	return redirect(url_for('Index'))

@app.route('/setup', methods=['POST'])
def setup():
	cur = mysql.connection.cursor()
	cur.execute('SELECT nombre,estado,conciencia FROM setup')
	data = cur.fetchall()
	return render_template('index.html', data = jsonify(data[0]))

@app.route('/get_data', methods=['POST'])
def get_data():
	if request.method == 'POST':
		palabra = request.form['palabra']
		if(palabra == 'salir'):
			print('llamando al sistema')
			return redirect(url_for('sistema'))
			#return sistema()
		else:
			nombre = 'Serome'
			conciencia = 'si'
			usuario = 'serome'
			mc = cr.cerebro()
			mc.transmisor(palabra)
			return jsonify(palabra)
		# cur.execute('SELECT usuariosh_id,nombre,apellidos,correo FROM usuariosh')
		# data = cur.fetchall()
		# cur.execute('SELECT usuariosh_id,nombre,apellidos,correo FROM usuariosh')
		# data = cur.fetchall()
		# return render_template('base.html', palabra = palabra)

@app.route('/nueva_conciencia', methods=['POST'])
def nueva_conciencia():
	if request.method == 'POST':
		palabra = request.form['palabra']
		nombre = 'Serome'
		conciencia = 'si'
		usuario = 'serome'
		cur = mysql.connection.cursor()
		cur.execute('INSERT INTO setup (nombre,conciencia,usuario) VALUES (%s, %s, %s)',(nombre,conciencia,usuario))
		mysql.connection.commit()



if __name__ == '__main__':
	app.run(port = 3000, debug = True)