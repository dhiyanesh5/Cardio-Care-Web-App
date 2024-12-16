import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv('heart_disease_data.csv')  # Ensure this is your actual file name
X = data.drop('output', axis=1)  # Drop the target column ('output')
y = data['output']  # Target column

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate accuracy
y_pred = model.predict(X_test)
print("Accuracy on test data:", accuracy_score(y_test, y_pred))

# Save the trained model
joblib.dump(model, 'heart_disease_model.pkl')  # Save model
print("Model saved as heart_disease_model.pkl")

# Save feature names for reference
joblib.dump(X.columns.tolist(), 'feature_names.pkl')  # Save column names
print("Feature names saved as feature_names.pkl")
