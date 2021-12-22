from flask import Flask
from flask import render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_string"

class MyForm(FlaskForm):
    user_field = StringField("Enter username:", validators=[DataRequired()])
    pass_field = StringField("Enter password:", validators=[DataRequired()])
    subb = SubmitField()

@app.route('/', methods=["GET", "POST"])
def home():
    my_form = MyForm()
    if my_form.validate_on_submit():
        password = MyForm.pass_field.StringField
        username = MyForm.user_field.StringField
        return redirect(url_for("plans.html"))

# app.route('plans', methods=["GET", "POST"])
# def plans():
#     return render_template("plans.html")

if __name__ =='__main__':
    app.run(debug=True)

app.config["TEMPLATES_AUTO_RELOAD"] = True

