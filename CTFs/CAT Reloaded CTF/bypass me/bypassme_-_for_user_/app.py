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
            file_name = os.path.join("notes", re.sub("[{}]", "", include))
            print(file_name)
            print("filename: ",file_name)
            try:
                with open(file_name, "rb") as file:
                        note = note.replace(include, f"<img src=\"data:image/png;base64,{base64.b64encode(file.read()).decode('latin1')}\" width=\"25\" height=\"25\" />")
            except FileNotFoundError:
                 return "Sorry, No note found by this name", 404
        return note
if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=7080)
