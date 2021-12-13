from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired




app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")
    if len(request.form) > 0:
        username = request.form["name"]
        password = request.form["password"]


app.route('plans', methods=["GET", "POST"])
def plans():
    return render_template("plans.html")



if __name__ =='__main__':
    app.run(debug=True)

app.config["TEMPLATES_AUTO_RELOAD"] = True

