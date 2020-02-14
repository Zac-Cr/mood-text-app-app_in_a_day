from flask import Flask, request, jsonify
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
    user = db.Column(db.String(15), unique = True)
    message = db.Colum(db.String, unique = False)

    def __init__(self,user,message):
        self.user = user
        self.id = id
        self.message = message






if __name__ == "__main__":
    app.run(debug=True)