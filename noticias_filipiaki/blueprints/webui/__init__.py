from flask import Blueprint

from .noticias import index, details_news, register_news, modifications_news, form_new_edit_news

bp = Blueprint('noticias', __name__, template_folder='templates', static_folder='static', static_url_path='/admin/static')

bp.add_url_rule('/', view_func=index)
bp.add_url_rule('/noticia/', view_func=details_news)
bp.add_url_rule('/noticia/list', view_func=register_news, endpoint="newslist")
bp.add_url_rule('/noticia/register/new', view_func=register_news, endpoint="newsregister")
bp.add_url_rule('/noticia/register/<int:id>', view_func=modifications_news, endpoint="newsput")
bp.add_url_rule('/noticia/delete/<int:id>', view_func=modifications_news, endpoint="newsdelete")
bp.add_url_rule('/noticia/register', view_func=form_new_edit_news, endpoint="newsadd")


def init_app(app):
    app.register_blueprint(bp)
