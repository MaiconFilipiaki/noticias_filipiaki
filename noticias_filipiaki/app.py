from flask import Flask

from noticias_filipiaki.ext import configuration

from noticias_filipiaki.blueprints import webui

def create_app():
    app = Flask(__name__)
    app.debug = True
    configuration.init_app(app)
    webui.init_app(app)
    return app
