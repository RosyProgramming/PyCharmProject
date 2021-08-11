from flask import Flask, render_template
from App.home import home
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'senha'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db = SQLAlchemy(app)
    
    app.register_blueprint(home)

    return app
