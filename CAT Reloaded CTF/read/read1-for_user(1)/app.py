from flask import Flask,request
import os

flag = os.environ.get('flag')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

blocked=["proc","self"]

@app.route('/readfile')
def readfile():
    if not request.args.get('file'):
        return "Please enter ?file parameter."
    
    file = request.args.get('file').encode('utf-8')
    print(file)
    
    print(file.decode('utf-8'))
    if any([b in file.decode("utf-8") for b in blocked]):
        return "Blocked, why not try to read note.txt?"

    try:

        file_path = os.path.join("safe/", file.decode('utf-8'))
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception :
        return f"An error occurred"
        

if __name__ == '__main__':
    app.run(host='0.0.0.0')