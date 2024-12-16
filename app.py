# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = joblib.load('heart_disease_model.pkl')

# Define the API route
@app.route('/')
def home():
    return "Heart Disease Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from user
        data = request.json  # Expecting JSON input

        # Extract features (make sure these match your training data)
        features = np.array([[
            data['age'], 
            data['sex'], 
            data['cp'], 
            data['trestbps'], 
            data['chol'], 
            data['thalach'],
            data['fbs'], 
            data['restecg'], 
            data['exang'], 
            data['oldpeak'], 
            data['slope'], 
            data['ca'], 
            data['thal']
        ]])

        # Make prediction
        prediction = model.predict(features)
        result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"

        # Return prediction result
        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

