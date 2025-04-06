import pandas as pd
import numpy as np

df= pd.read_csv(r"C:\Users\SK SAMIM ALI\Downloads\archive\diabetes_prediction_dataset.csv")
age=df["age"].values
blood_glucose_level=df["blood_glucose_level"].values

print(age)
print(blood_glucose_level)

mean_age = age.mean()
mean_blood_glucose_level = blood_glucose_level.mean()

# Calculate coefficients
numerator = 0
denominator = 0
for i in range(len(age)):
    numerator += (age[i] - mean_age) * (blood_glucose_level[i] - mean_blood_glucose_level)
    denominator += (age[i] - mean_age) ** 2

b = numerator / denominator
b1 = mean_blood_glucose_level- (b * mean_age)

print("Coefficient b:", b)
print("Coefficient b1:", b1)

# Make predictions
predictions = [b * x + b1 for x in age]
# print("Predictions:", predictions)

# Calculate accuracy
threshold = mean_blood_glucose_level * 0.50
accurate_predictions = sum(abs(blood_glucose_level[i] - predictions[i]) < threshold for i in range(len(blood_glucose_level)))
accuracy = (accurate_predictions / len(predictions)) * 100
print("Accuracy:", accuracy)
