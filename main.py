from flask import Flask, escape, request, make_response,redirect, render_template
#from flask_wtf import FlaskForm # libreria para formularios
#from wtforms.fields import StringField, PasswordField, SubmitField #capturar string y contraseñas
#from wtforms.validators import DataRequired # para agregar los required en los imputs
app = Flask(__name__)

todos=['TODO 1','TODO 2','TODO 3']

#class LoginForm(FlaskForm):
	#username = StringField('Nombre de usuario', validators=[DataRequired()])
	#password = PasswordField('password', validators=[DataRequired()])
	#submit = SubmitField('Enviar')

app.errorhandler(404)
def not_found(error):
	return render_template('404.html', error=error)

@app.route('/')
def index():
	user_ip = request.remote_addr
	response = make_response(redirect('/hello'))
	response.set_cookie('user_ip',user_ip)

	return response

@app.route('/base', methods=['GET','POST'])
def base():
	user_ip = request.remote_addr
	response = make_response(redirect('/base'))
	response.set_cookie('user_ip',user_ip)

	return response

@app.route('/hello')
def hello():
	user_ip = request.cookies.get('user_ip')
	user_ip = request.remote_addr
	#login_form = LoginForm()
	context ={
	'user_ip': user_ip,
	'todos': todos,
	#'login_form': login_form
	}

	return render_template('index.html',**context)
	#'Hello worlds tu ip es{}'.format(user_ip)
	#     name = request.args.get("name", "World")
	#     return f'Hello, {escape(name)}!'

