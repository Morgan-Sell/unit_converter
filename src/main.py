from flask import Flask, render_template
from flask_bootstrap import Bootstrap5



app = flask(__name__)
app.secret_key = "MY_SECRET_KEY" # TODO: Update key
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")