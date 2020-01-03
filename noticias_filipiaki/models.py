from noticias_filipiaki.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class News(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text)
