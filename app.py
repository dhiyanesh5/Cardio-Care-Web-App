from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

model = joblib.load("heart_disease_model.pkl")
feature_names = joblib.load("feature_names.pkl")  

@app.route("/")
def home():
    return "Heart Disease Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        features = np.array([[data[name] for name in feature_names]])

        prediction = model.predict(features)
        result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"
        
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
