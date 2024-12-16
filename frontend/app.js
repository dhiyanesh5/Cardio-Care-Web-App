document.getElementById('predictionForm').addEventListener('submit', function (event) {
    event.preventDefault();  // Prevent the form from submitting the usual way

    // Get form data
    const data = {
        age: parseInt(document.getElementById('age').value),
        sex: parseInt(document.getElementById('sex').value),
        cp: parseInt(document.getElementById('cp').value),
        trestbps: parseInt(document.getElementById('trestbps').value),
        chol: parseInt(document.getElementById('chol').value),
        thalach: parseInt(document.getElementById('thalach').value),
        fbs: parseInt(document.getElementById('fbs').value),
        restecg: parseInt(document.getElementById('restecg').value),
        exang: parseInt(document.getElementById('exang').value),
        oldpeak: parseFloat(document.getElementById('oldpeak').value),
        slope: parseInt(document.getElementById('slope').value),
        ca: parseInt(document.getElementById('ca').value),
        thal: parseInt(document.getElementById('thal').value)
    };

    // Make sure to replace the below URL with your actual backend API URL
    const apiUrl = 'https://your-backend-link.com/predict'; // Replace with actual URL

    async function predictHeartDisease(data) {
    try {
        const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        });

        const result = await response.json();
        if (response.ok) {
        displayPrediction(result); // Handle result and display it
        } else {
        throw new Error(result.error || 'Prediction failed');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error predicting the result');
    }
    }

});
