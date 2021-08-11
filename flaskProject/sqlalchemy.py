from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Noticia(db.Model):
        titulo = db.column(db.String)
        autor = db.column(db.String(50))
        date_created = db.column(db.DateTime, default=datetime.utcnow)
        descricao = db.column(db.String)

        def __init__(self, titulo, autor, date_creted, descricao):
            self.autor = autor
            self.titulo = titulo
            self.date_created = date_creted