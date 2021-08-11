from flask.templating import render_template
from flask import url_for, redirect
from . import home


@home.route('/')
def index():
    return render_template('index.html')

@home.route('/novidades')
def novidades():
    return render_template('novidades.html')

@home.route('/jogos')
def jogos():
    return render_template('jogos.html')

@home.route('/jogo/download')
def download():
    return redirect('http://playvalorant.com/en-gb/')

@home.route('/jogo/requisitos')
def requisito():
    return redirect('http://www.systemrequirementslab.com/cyri/requirements/valorant/19638')

@home.route('/dev')
def dev():
    return render_template('dev.html')

@home.route('/redes')
def redes():
    return render_template('redes.html')

@home.route('/seguranca')
def sec():
    return render_template('sec.html')

@home.route('/noticia')
def noticia():
    return render_template('not1.html')
