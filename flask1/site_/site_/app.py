from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///noticias.db'

#Inicializando o banco de dados
db = SQLAlchemy(app)

#criando db model
class CadastroNoticias(db.Model):
    id = db.column(db.integer,primary_key=True)
    titulo = db.column(db.String(200), nullable=False)
    autor = db.column(db.String(50), nullable=False)
    date_created = db.column(db.DateTime, default=datetime.utcnow)
    descricao = db.column(db.String)

    def __repr__(self):
        return '<titulo %r>' % self.id


subscribers = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/novidades')
def novidades():
    return render_template('novidades.html')


@app.route('/jogos')
def jogos():
    return render_template('jogos.html')


@app.route('/inscreva-se')
def comunidade():
    return render_template('form.html')


@app.route('/cadastro_realizado')
def postform():
    return render_template('posform.html')

@app.route('/dev')
def dev():
    return render_template('dev.html')


@app.route('/redes')
def redes():
    return render_template('redes.html')


@app.route('/seguranca')
def seguranca():
    return render_template('sec.html')


@app.route('/noticia')
def noticia():
    return render_template('not1.html')



if __name__ == '__main__':
    app.run(debug=True)
