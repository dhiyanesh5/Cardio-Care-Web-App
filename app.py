from flask import Flask, send_from_directory, jsonify, request
import numpy as np
import pickle
from flask_cors import CORS




app = Flask(__name__, static_folder="frontend")  # Set the 'frontend' folder as static folder
CORS(app)
# Load the trained model
model = pickle.load(open('heart_disease_model.pkl', 'rb'))  # Make sure to replace this path with your model path//

@app.route('/')
def home():
    # Serve the index.html file from the 'frontend' folder
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input data from the POST request
        data = request.get_json()

        # Extract patient parameters from the request
        parameters = [
            data['age'],
            data['sex'],
            data['cp'],
            data['trestbps'],
            data['chol'],
            data['fbs'],
            data['restecg'],
            data['thalach'],
            data['exang'],
            data['oldpeak'],
            data['slope'],
            data['ca'],
            data['thal']
        ]

        # Convert the parameters to a numpy array and reshape it for prediction
        features = np.array(parameters).reshape(1, -1)

        # Predict using the loaded model
        prediction = model.predict(features)

        # Send the result back to the frontend
        if prediction == 1:
            return jsonify({"prediction": "Heart Disease Detected"})
        else:
            return jsonify({"prediction": "No Heart Disease Detected"})

    except Exception as e:
        return jsonify({"error": f"Error predicting the result: {str(e)}"}), 400

if __name__ == "__main__":
    app.run(debug=True)
