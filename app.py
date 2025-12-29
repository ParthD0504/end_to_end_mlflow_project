from flask import Flask, render_template, request
import os
import numpy as np

from ml_project.pipeline.prediction_pipeline import PredictionPipeline


app = Flask(__name__)
prediction_pipeline = None
model_load_error = None
try:
    prediction_pipeline = PredictionPipeline()
except Exception as e:  # pragma: no cover - defensive startup guard
    model_load_error = str(e)


@app.route("/", methods=["GET"])
def homePage():
    return render_template("index.html")

@app.route("/train", methods=["GET"])
def training():
    os.system("python main.py")
    return "Training successful!"


@app.route("/predict", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if model_load_error:
        return (
            render_template(
                "results.html", prediction=f"Model unavailable: {model_load_error}"
            ),
            503,
        )

    try:
        fixed_acidity = float(request.form["fixed_acidity"])
        volatile_acidity = float(request.form["volatile_acidity"])
        citric_acid = float(request.form["citric_acid"])
        residual_sugar = float(request.form["residual_sugar"])
        chlorides = float(request.form["chlorides"])
        free_sulfur_dioxide = float(request.form["free_sulfur_dioxide"])
        total_sulfur_dioxide = float(request.form["total_sulfur_dioxide"])
        density = float(request.form["density"])
        ph = float(request.form["pH"])
        sulphates = float(request.form["sulphates"])
        alcohol = float(request.form["alcohol"])

        data = np.array(
            [
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                ph,
                sulphates,
                alcohol,
            ]
        ).reshape(1, -1)

        predict = prediction_pipeline.predict(data)
        prediction_value = predict[0] if len(predict) else predict

        return render_template("results.html", prediction=str(prediction_value))
    except Exception as e:
        return render_template("results.html", prediction=f"Error: {e}"), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    