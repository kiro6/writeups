
## after open the zip file

- source code

```python
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
  
  
with open(private.pem, r) as f:  
   private_key = f.read()  
app.config[PRIVATE_KEY] = private_key  
  
  
app.config[flag] = os.getenv(FLAG)  
  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  
keypath = /api/secrets/publickey  
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
   if not User.query.filter_by(id=1).first():  # check if admin already exists  
       hashed_password = generate_password_hash(os.urandom(32).decode(latin-1), method='sha256')  # replace with your admin password  
       admin = User(id=1, name=admin, password=hashed_password, admin=True)  
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
           print(n)  
           if 'iss' not in unverified_header:  
               return jsonify({'message': 'Issuer not specified'}), 401  
  
           iss = unverified_header['iss']  
           print(iss)  
           if not iss.startswith('/api/secrets/publickey'):  
               return jsonify({'message': 'Invalid issuer'}), 401  
  
           public_key_url = http://localhost:5000 + iss    
           response = requests.get(public_key_url)  
           print(response.text)  
           print(n)  
           if response.status_code != 200:  
               return jsonify({'message': 'Unable to fetch public key'}), 401  
  
           public_key = response.text  
           data = jwt.decode(token, public_key, algorithms=[RS256])  
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
           return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: login required'})       
  
       user = User.query.filter_by(name=auth.get('name')).first()      
  
       if user and check_password_hash(user.password, auth.get('password')):  
              
           token = jwt.encode({'id': user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=90), 'iss': keypath}, app.config['PRIVATE_KEY  
'], algorithm=RS256)     
           return jsonify({'token' : token})    
  
       return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: login required'})     
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
       return jsonify({'flag' : f'{app.config[flag]}'})  
   else:  
       return jsonify({'message' : 'Access denied'})  
  
if __name__ == __main__:  
   with app.app_context():  
       db.create_all()  
       create_tables()  
   app.run(host='0.0.0.0', port=5000, debug=False)
```

## that is not the only important thing

- public key
```
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA0YLu8FLu0bki5Pm6EB82
K2wRS9GJ9oPhta34ytqyIE/+pRFqb9ggXWHmDEJNgXkw/vT9aEH/Nadpzok59sl9
w/Ry1eK2e6S/xMTdbQr/fRKsJfCO+W5NdjxeIiHP1Ulx0pCbTb4MWnOuQwPBIgM8
ySzDbA5kehYDxBrX/qBGV4XvniZVKR96IlBmkLFMk9BL5U5llikHtkv5Nfe7hvqn
OsgcCOL4wh97e+x73pY/JKs3cGUbmOps3AMtalj6TpHsNXBXIt5dy9beuZfu+hyz
mzfVSlFVmmZHndUSPdhGLhanngA0J2Y+JPIFyakK0JkL7H9n3zLXi/9MdMFEc/oo
amIbpfc4Ke0t/bbw13EYDGPRX7IpROiQiJ+Xg9Ce9/wIc3Io6Aml9ct+yBRfoXPs
UE3tDi4tH6LTuIP02OgFBIHvkcAjXgPHRCf0HCnZyJ8X4Uo2obW42YwdsdHXrgBy
O+H3tka2F20ARZhwQumzP3Oig9IzoHcNhXcHwhx8DTZajxnEA+mbqWQRpOeqMSVr
eXdFxtL+qidyDDiRz51PaTT1uof4FV/WgxgYqsy1GM1HYsg14qb/kChrhCSmp6fd
bbbNonQTnx0T+mNiZ918MrrqufgOii78mhkczq3X1S6Mp26V82/Uy7I6WxDTiKZ5
Sa1gXkuPJ9t6EjK02/YuQbECAwEAAQ==
-----END PUBLIC KEY-----

```
- private key 
```
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
```

##### the site use jwt token,we have secret and public key we can make any token we want , sign in then login to get our token
![Screenshot_20230729_171907](https://github.com/kiro6/writeups-ctfs/assets/57776872/b25aae81-f569-4bbe-9889-4a190b2544e7)


##### update the token with our private and public key , make `id=1` and put `iss` in the header because the code check if `iss` was in the header
![Screenshot 2023-07-29 at 17-22-18 JWT IO](https://github.com/kiro6/writeups-ctfs/assets/57776872/d4e1b1eb-c7ac-4667-87bb-f878dea10d10)

##### send request with header `x-access-tokens`
![Screenshot_20230729_172705](https://github.com/kiro6/writeups-ctfs/assets/57776872/d9084458-c1da-47d2-83e2-b9c8d1b935ce)

##### and here is our flag
```
flag{d1d_y0u_r3ally_trav4Rse?}
```
