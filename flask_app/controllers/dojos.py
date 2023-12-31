from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def dojo():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos = Dojo.get_all())


@app.route('/create/dojo', methods=['POST'])
def create_dojo():
   Dojo.save(request.form)
   return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        'id': id
    }
    return render_template('dojo.html', dojo=Dojo.get_one_with_ninjas(data))

