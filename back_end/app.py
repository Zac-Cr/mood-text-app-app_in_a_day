from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

# setupdatabase tables(classes) - drea
# build endpoint connections - Ian Joseph

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(15), unique = True, nullable=False)
    message = db.Column(db.String, unique = False, nullable=False)

    def __init__(self,user,message):
        self.user = user
        self.id = id
        self.message = message

class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(), unique=False, nullable=False)
    #parens is unlimited char length
    #nullable means not able to leave blank

    def __init__(self, username, password):
        self.username = username
        self.password = password


class GuideSchema(ma.Schema):
    class Meta:
        fields = ('username', 'password')


guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)

if __name__ == '__main__':
    app.run(debug=True)