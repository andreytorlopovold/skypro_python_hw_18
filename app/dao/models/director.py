from app.database import db
from marshmallow import Schema, fields


class Director(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class GenreScheme(Schema):
    id = fields.Int()
    name = fields.Str()
