# **CardioCareML: Heart Disease Prediction Web App**

## **Project Overview**
CardioCareML is a machine learning-based web application designed to predict the likelihood of heart disease in individuals based on various health parameters. The application utilizes a Random Forest model, trained on a dataset of heart disease patient information, to provide accurate predictions. The backend is built using Flask, while the frontend is developed using HTML, CSS, and JavaScript.

## **Technologies Used**

- **Backend**: 
  - Python
  - Flask
  - Scikit-learn
  - Pickle for model serialization
- **Frontend**: 
  - HTML, CSS
  - JavaScript (Fetch API for handling requests)
- **Deployment**:
  - Backend hosted on [Render](https://render.com)
  - Frontend hosted on [Netlify](https://www.netlify.com)
  - GitHub for version control

## **How it Works**
1. **User Input**: The user provides health-related information through an intuitive form in the frontend, including parameters such as age, sex, cholesterol level, and more.
2. **API Request**: Upon form submission, the data is sent as a POST request to the backend API.
3. **Prediction**: The backend processes the data using a pre-trained Random Forest model and sends back the prediction (whether the user is at risk of heart disease).
4. **Results Display**: The prediction result is displayed on the frontend, color-coded (green for "No Heart Disease" and red for "Heart Disease Detected").

## **Features**
- Predicts the likelihood of heart disease based on user input.
- Interactive and responsive frontend design.
- Hosted on free platforms like Render (backend) and Netlify (frontend).

## **Setup Instructions**

### **Backend Setup**
1. Clone the repository.
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend API:
   ```bash
   python app.py
   ```
   The backend will be accessible at `http://127.0.0.1:5000`.

### **Frontend Setup**
1. Clone the repository.
2. Open the `index.html` file in any web browser to view and interact with the web application.

### **Deploying the Application**
- The backend API is hosted on [Render](https://render.com), and the frontend is hosted on [Netlify](https://www.netlify.com).

## **Contributors**
- **Dhiyanesh**: Developer
- **Mithuna**: Developer

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

