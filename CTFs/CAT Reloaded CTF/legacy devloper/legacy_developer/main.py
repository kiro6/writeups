from flask import Flask, request, jsonify, make_response, redirect ,render_template,Response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import uuid
from functools import wraps
import os,signal
import requests,zipfile
from apscheduler.schedulers.background import BackgroundScheduler
app = Flask(__name__)


with open("private.pem", "r") as f:
    private_key = f.read()
app.config["PRIVATE_KEY"] = private_key


app.config["flag"] = os.getenv("FLAG")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
keypath = "/api/secrets/publickey"
db = SQLAlchemy(app)

class User( db.Model):  
    id = db.Column(db.Integer, primary_key = True)  
    name = db.Column(db.String(50))  
    password = db.Column(db.String(80)) 
    admin = db.Column(db.Boolean)


def restart_app():
    os.kill(os.getpid(), signal.SIGINT)

def create_tables():
    db.create_all()
    if not User.query.filter_by(id=1).first():  # check if admin already exists
        hashed_password = generate_password_hash(os.urandom(32).decode("latin-1"), method='sha256')  # replace with your admin password
        admin = User(id=1, name="admin", password=hashed_password, admin=True)
        db.session.add(admin)
        db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:

            unverified_header = jwt.get_unverified_header(token)
            print(unverified_header)
            print("\n")
            if 'iss' not in unverified_header:
                return jsonify({'message': 'Issuer not specified'}), 401

            iss = unverified_header['iss']
            print(iss)
            if not iss.startswith('/api/secrets/publickey'):
                return jsonify({'message': 'Invalid issuer'}), 401

            public_key_url = "http://localhost:5000" + iss 
            response = requests.get(public_key_url)
            print(response.text)
            print("\n")
            if response.status_code != 200:
                return jsonify({'message': 'Unable to fetch public key'}), 401

            public_key = response.text
            data = jwt.decode(token, public_key, algorithms=["RS256"])
            print(data)

            current_user = User.query.filter_by(id=data['id']).first()
        except Exception as e:
            return jsonify({'message': f'token is invalid: {str(e)}'}), 401

        return f(current_user, *args, **kwargs)
    return decorator


@app.route('/register', methods=['GET', 'POST'])
def signup_user():  
    if request.method == 'POST':
        data = request.get_json()  
        hashed_password = generate_password_hash(data['password'], method='sha256')

        new_user = User(name=data['name'], password=hashed_password, admin=False)
        db.session.add(new_user)
        db.session.commit()    

        return jsonify({'message': 'registered successfully'})   
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        auth = request.get_json()

        if not auth or not auth.get('name') or not auth.get('password'):  
            return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})    

        user = User.query.filter_by(name=auth.get('name')).first()   

        if user and check_password_hash(user.password, auth.get('password')):
            
            token = jwt.encode({'id': user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=90), 'iss': keypath}, app.config['PRIVATE_KEY'], algorithm="RS256")  
            return jsonify({'token' : token}) 

        return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})  
    return render_template('login.html')

@app.route('/api/secrets/publickey', methods=['GET'])
def get_public_key():
    with open('public_key.pem', 'r') as f:
        public_key = f.read()
    return Response(public_key, mimetype='text/plain')

@app.route('/logout')
def logout_user():
    redirect_url = request.args.get('r', '/')
    return redirect(redirect_url, code=302)

@app.route('/flag')
@token_required
def get_flag(current_user):
    if current_user.admin:
        return jsonify({'flag' : f'{app.config["flag"]}'})
    else:
        return jsonify({'message' : 'Access denied'})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_tables()
    app.run(host='0.0.0.0', port=5000, debug=False)