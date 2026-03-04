import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

#  Load Dataset
# Agar tumhare repo me CSV file hai to uska naam yaha likho
data = pd.read_csv("student-mat.csv")  # file name change karo agar different hai

#  Encode Categorical Columns
label_encoders = {}

for column in data.columns:
    if data[column].dtype == 'object':
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

#Define Features and Target
# Assume final grade (G3) is target
X = data.drop("G3", axis=1)
y = data["G3"]

#  Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#  Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

#  Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Save Model
joblib.dump(model, "student_performance_model.pkl")
print("Model saved successfully!")
