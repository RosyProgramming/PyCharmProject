from flask.templating import render_template
from . import home

@home.route('/increva-se')
def comunidade():
    return render_template('form.html')

@home.route('/cadastrar')
def cadastro():
    return render_template('posform.html')
