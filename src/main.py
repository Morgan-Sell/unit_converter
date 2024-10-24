from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from forms import LengthForm

app = Flask(__name__, template_folder="../templates")
app.secret_key = "MY_SECRET_KEY"  # TODO: Update key
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    form = LengthForm()
    return render_template("index.html", form=form)



if __name__ == "__main__":
    app.run(debug=True, port=5001)