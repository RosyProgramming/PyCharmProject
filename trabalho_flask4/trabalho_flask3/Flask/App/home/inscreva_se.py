from flask.templating import render_template

from . import home
from ...models.formulario import cadastroForm


@home.route('/increva-se', methods=["GET", "POST"])
def comunidade():
    form = cadastroForm()
    if form.validate_on_submit():
        print(form.name.data)
        print(form.email.data)
        print(form.opc.data)
        return finalizado() 
    else: 
        print(form.errors)
    return render_template('form.html')

@home.route('/cadastrar')
def finalizado():
    return render_template('posform.html')
