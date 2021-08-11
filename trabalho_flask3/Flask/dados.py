import sqlite3

from sqlalchemy.testing import db

with sqlite3.connect("banco.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE noticias(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor TEXT, descricao TEXT)")
    c.execute('INSERTI INTO noticias VALUES ("0","Criando site com flask", "Rosana Olveira", "Tentando cria o site com flask")')
    c.close()


    class Cadastro(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(50))
        subtitle = db.Column(db.String(50))
        author = db.Column(db.String(20))
        date_posted = db.Column(db.DateTime)
        content = db.Column(db.Text)
