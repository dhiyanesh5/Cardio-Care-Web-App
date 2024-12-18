import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


data = pd.read_csv('heart_disease_data.csv') 
X = data.drop('output', axis=1)  
y = data['output']  

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

model = RandomForestClassifier(random_state=42)
model.fit(X_train_std, y_train)


y_pred = model.predict(X_test_std)
print("Accuracy on test data:", accuracy_score(y_test, y_pred))


joblib.dump(model, 'heart_disease_model.pkl')  
print("Model saved as heart_disease_model.pkl")


joblib.dump(X.columns.tolist(), 'feature_names.pkl')  
print("Feature names saved as feature_names.pkl")
