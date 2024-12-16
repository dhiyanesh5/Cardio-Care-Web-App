async function predictDisease() {
    const formData = {
        age: parseInt(document.getElementById("age").value),
        sex: parseInt(document.getElementById("sex").value),
        cp: parseInt(document.getElementById("cp").value),
        trestbps: parseInt(document.getElementById("trestbps").value),
        chol: parseInt(document.getElementById("chol").value),
        thalach: parseInt(document.getElementById("thalach").value),
        fbs: parseInt(document.getElementById("fbs").value),
        restecg: parseInt(document.getElementById("restecg").value),
        exang: parseInt(document.getElementById("exang").value),
        oldpeak: parseFloat(document.getElementById("oldpeak").value),
        slope: parseInt(document.getElementById("slope").value),
        ca: parseInt(document.getElementById("ca").value),
        thal: parseInt(document.getElementById("thal").value)
    };

    const apiUrl = "https://cardiocare-1j5t.onrender.com/predict";

    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById("result").innerText = `Prediction: ${result.prediction}`;
        } else {
            document.getElementById("result").innerText = `Error: ${result.error || "Something went wrong!"}`;
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Error predicting the result. Please check the API!";
    }
}
