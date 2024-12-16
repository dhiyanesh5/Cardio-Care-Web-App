from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Load the trained model
model = pickle.load(open("heart_disease_model.pkl", "rb"))

@app.route("/")
def home():
    return "Heart Disease Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse incoming JSON data
        data = request.get_json()
        features = np.array([list(data.values())])
        
        # Predict using the loaded model
        prediction = model.predict(features)
        result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"
        
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
