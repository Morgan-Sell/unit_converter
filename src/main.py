from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5

from forms import LengthForm
from src.conversion_strategy import LengthConversionStrategy, UnitConverter
from src.operations import calc_conversion_based_on_form_inputs

app = Flask(__name__, static_folder="../static", template_folder="../templates")
# required for Flask session handling
app.secret_key = "MY_SECRET_KEY"  # TODO: Update key
bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def home():
    form = LengthForm()
    result = None

    if form.validate_on_submit():
        strategy = LengthConversionStrategy()
        result = calc_conversion_based_on_form_inputs(form, strategy)

    return render_template("index.html", form=form, result=result)


@app.route("/length", methods=["GET", "POST"])
def length():
    form = LengthForm()
    result = None

    if form.validate_on_submi():
        value = form.value.data
        from_unit = form.from_unit.data
        to_unit = form.to_unit.data

        strategy = LengthConversionStrategy()
        converter = UnitConverter(strategy=strategy)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
