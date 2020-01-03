from noticias_filipiaki.ext.database import db

from noticias_filipiaki.models import News

def init_app(app):

    @app.cli.command()
    def createdb():
        """Create db"""
        db.create_all()

    @app.cli.command()
    def populate_table_news():
        data = [
            News(id=1, title="Teste", body="asiofnsdnfs dsfns f jsdfnsd vjkdsjdnfjsd"),
            News(id=2, title="Teste 1", body="asiofnsdnfs dsfns f jsdfnsd vjkdsjdnfjsd")
        ]
        db.session.bulk_save_objects(data)
        db.session.commit()
        return News.query.all()
