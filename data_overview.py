# Student Performance Data Overview

import pandas as pd

# Sample structure (replace with real dataset later)
data = {
    "Gender": ["Male", "Female", "Female", "Male"],
    "Study_Hours": [2, 4, 3, 5],
    "Previous_Score": [65, 78, 72, 88],
    "Final_Result": ["Pass", "Pass", "Pass", "Pass"]
}

df = pd.DataFrame(data)

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nChecking missing values:")
print(df.isnull().sum())
