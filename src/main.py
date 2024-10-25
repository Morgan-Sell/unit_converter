from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5

from forms import LengthForm
from src.conversion_strategy import LengthConversionStrategy, UnitConverter

app = Flask(__name__, static_folder="../static", template_folder="../templates")
# required for Flask session handling
app.secret_key = "MY_SECRET_KEY"  # TODO: Update key
bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def home():
    form = LengthForm()
    result = None

    if form.validate_on_submit():
        value = form.value.data
        from_unit = form.from_unit.data
        to_unit = form.to_unit.data

        strategy = LengthConversionStrategy()
        converter = UnitConverter(strategy=strategy)

        try:
            result = converter.convert(value, from_unit, to_unit)
        except ValueError as e:
            flash(str(e), "danger")

    return render_template("index.html", form=form, result=result)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
