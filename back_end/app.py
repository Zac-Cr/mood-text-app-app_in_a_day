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
    user = db.Column(db.String(15), unique = True, nullable=False)
    message = db.Column(db.String, unique = False, nullable=False)
    color = db.Column(db.String(), unique = False, nullable=False)


    def __init__(self,user,message):
        self.user = user
        self.id = id
        self.message = message

class Login(db.Model):
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

@app.route('/guide', methods=["POST"])
def add_guide():
    username = request.get_json().get('username')
    password = request.get_json().get('password')

    new_guide = Login(username, password)

    db.session.add(new_guide)
    db.session.commit()

    login = Login.query.get(new_guide.id)

    return guide_schema.jsonify(login)

# Endpoint to query all guides
@app.route("/guides", methods=["GET"])
def get_guides():
    all_guides = Login.query.all()
    result = guides_schema.dump(all_guides)
    return jsonify(result)

# Endpoint for querying a single guide
@app.route("/guide/<id>", methods=["GET"])
def get_guide(id):
    login = Login.query.get(id)
    return guide_schema.jsonify(login)

# Endpoint for updating a guide
@app.route("/guide/<id>", methods=["PUT"])
def guide_update(id):
    login = Login.query.get(id)
    username = request.json['username']
    password = request.json['password']

    guide.user_name = username
    guide.password = password

    db.session.commit()
    return guide_schema.jsonify(login)

# Endpoint for deleting a record
@app.route("/guide/<id>", methods=["DELETE"])
def guide_delete(id):
    login = Login.query.get(id)
    db.session.delete(login)
    db.session.commit()

    return guide_schema.jsonify(login)

if __name__ == '__main__':
    app.run(debug=True)