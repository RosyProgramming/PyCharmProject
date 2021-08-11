from flask_wtf import FlaskForm
from sqlalchemy import null
from wtforms import StringField, SelectField 
from wtforms.validators import DataRequired 


all=[(null), ('Novidades'), ('Jogos'), ('Dev'), ('Redes'), ('Segurança')] 

class cadastroForm(FlaskForm): 
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    opc = SelectField("opc", validators=[DataRequired()], choices=all)

