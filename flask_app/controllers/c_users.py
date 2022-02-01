from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.m_user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt( app )
#rutas principales
@app.route( '/', methods=['GET'] )
def inicio():
    return render_template( "index.html" )

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template("dashboard.html")

#Validación con re
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        # redirigimos a la plantilla con el formulario
        return redirect('/')
    # ...hacer otras cosas
    return redirect('/dashboard')