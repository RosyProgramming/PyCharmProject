from flask import Flask, render_template, app
from flask_sqlalchemy import SQLAlchemy
from App.db.sqlalchemy import db

from App.home import home


def create_app():
    app = Flask(__name__)
    db.init_app(app)

    app.register_blueprint(home)

    app.register_blueprint(db)

    return app
