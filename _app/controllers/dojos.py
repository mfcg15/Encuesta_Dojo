from flask import render_template, request, redirect, session
from _app.models.dojo import Dojo
from _app import app

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result")
def result():
    request.form = session['informacion']
    return render_template('show.html',nombre = request.form['nombre'], lugar = request.form['ubicacion'], lenguaje = request.form['idioma'],
    comentarios= request.form['comentario'])

@app.route('/create_dojo', methods=["POST"])
def dojoNew():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data = {
        "nombre": request.form["nombre"],
        "ubicacion": request.form["ubicacion"],
        "idioma": request.form["idioma"],
        "comentario": request.form["comentario"]
    }
    session['informacion'] = request.form
    Dojo.save(data)
    return redirect('/result')