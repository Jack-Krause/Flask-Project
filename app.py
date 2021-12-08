from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm


app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")
    if len(request.form) > 0:
        username = request.form["name"]
        password = request.form["password"]

if __name__ =='__main__':
    app.run(debug=True)

app.config["TEMPLATES_AUTO_RELOAD"] = True

