from flask import render_template
from flask import request
from flask import jsonify
from flask import Blueprint

noticias_blueprint = Blueprint('noticias', __name__)


@noticias_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="Noticias Filipiaki")


@noticias_blueprint.route('/noticia/<int:id>', methods=['GET'])
def details_news(id):
    return render_template('details.html', id=id)


@noticias_blueprint.route('/noticia/list', methods=['GET'])
@noticias_blueprint.route('/noticia/register/new', methods=['POST'])
def register_news():
    if request.method == 'GET':
        return render_template('list.html')
    elif request.method == 'POST':
        return jsonify({'msg': 'criada com sucesso'})
    return jsonify({'msg': 'ERROR NOT METHOD LIST'}), 503


@noticias_blueprint.route('/noticia/register/<int:id>', methods=['PUT'])
@noticias_blueprint.route('/noticia/delete/<int:id>', methods=['DELETE'])
def modifications_news(id):
    if request.method == 'PUT':
        return render_template('register.html')
    elif request.method == 'DELETE':
        return jsonify({'msg': 'criada com sucesso'})
    return jsonify({'msg': 'ERROR NOT METHOD LIST'}), 503


@noticias_blueprint.route('/noticia/register', methods=['GET'])
def form_new_edit_news():
    return render_template('register.html')

