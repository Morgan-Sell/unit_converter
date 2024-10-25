from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from src.conversion_strategy import LengthConversionStrategy, UnitConverter
from forms import LengthForm

app = Flask(__name__, template_folder="../templates")
# required for Flask session handling
app.secret_key = "MY_SECRET_KEY"  # TODO: Update key
bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def home():
    form = LengthForm()

    if form.validate_on_submit():
        value = form.value.data
        from_unit = form.from_unit.data
        to_unit = form.to_unit.data

        strategy = LengthConversionStrategy()
        converter = UnitConverter(strategy=strategy)

        try:
            result = converter.convert(value, from_unit, to_unit)
            flash(f"Converted {value} {from_unit} to {result} {to_unit}", "success")
        except ValueError as e:
            flash(str(e), "danger")
            
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
