from flask import Flask, render_template

from App.db import db

app = Flask(__name__)


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
    db.create_all()
    app.run(debug=True)
