from .app import db

class User(db.Model):
    __tablename_="users"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    opt = db.Column(db.String, unique=True)

    def __init__(self, name, email, opt):
        self.username = username
        self.password = password
        self.email = email


    def __repr__(self):
        return "<usr %r>" % self.username