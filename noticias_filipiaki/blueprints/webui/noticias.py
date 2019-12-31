from flask import render_template
from flask import request
from flask import jsonify


def index():
    return render_template('index.html', title="Noticias Filipiaki")


def details_news():
    return render_template('details.html')


def register_news():
    if request.method == 'GET':
        return render_template('list.html')
    elif request.method == 'POST':
        return jsonify({'msg': 'criada com sucesso'})
    return jsonify({'msg': 'ERROR NOT METHOD LIST'}), 503


def modifications_news(id):
    if request.method == 'PUT':
        return render_template('register.html')
    elif request.method == 'DELETE':
        return jsonify({'msg': 'criada com sucesso'})
    return jsonify({'msg': 'ERROR NOT METHOD LIST'}), 503


def form_new_edit_news():
    return render_template('register.html')

