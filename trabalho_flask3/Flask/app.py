from datetime import datetime

from flask import Flask, render_template, g, request
from App.home import home
import sqlite3


app = Flask(__name__)
app.secret_key = "segredo"
app.database = "banco.db"

@app.route("/")
def index():
    g.db = sqlite3.connect.db('select + fom noticias ORDER BY id DESC;')
    return render_template('index.html')


@app.route('/')
def index():
    posts = Cadastro.query.order_by(Cadastro.date_posted.desc()).all()

    return render_template('index.html', posts=posts)


@app.route('/add')
def add():
    return render_template('cadastro.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Cadastro(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())


def create_app():
    app = Flask(__name__)

    app.register_blueprint(home)

    return app
