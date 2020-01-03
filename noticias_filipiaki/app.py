from flask import Flask

from noticias_filipiaki.ext import configuration
from noticias_filipiaki.ext import database
from noticias_filipiaki.ext import commands

from noticias_filipiaki.blueprints import webui


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    database.init_app(app)
    commands.init_app(app)
    webui.init_app(app)
    return app
