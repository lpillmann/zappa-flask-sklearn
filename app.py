"""
A Flask app to return the prediction result using
a VERY simple ML model

Code to generate the model:
    import numpy as np
    from sklearn import linear_model
    from joblib import dump, load
    reg = linear_model.LinearRegression()
    reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
    dump(reg, 'model/regressor.joblib')
"""

from flask import Flask, request
import joblib
import numpy as np

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# Example call /predict?x=1&y=2
@app.route("/predict")
def predict():
    # Loads model
    reg = joblib.load('model/regressor.joblib')
    # Formats input
    v = np.array([
        int(request.args.get('x')), 
        int(request.args.get('y'))]) \
        .reshape(1,-1)
    # Uses model to predict
    pred = reg.predict(v)

    return "Predicted value is {}".format(pred[0])
