import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv(r"C:\Users\SK SAMIM ALI\OneDrive\Documents\homeprice.csv")

# Extract area and price columns
area = df["area"].values            # df["age"]: This selects the "age" column from the DataFrame df. The result is a pandas Series containing the values of the "age" column. '''
price = df["price"].values          # .values: This converts the pandas Series into a numpy array containing the values of the "age" column. It's often done because numpy arrays are more efficient for numerical computations and can be directly used in mathematical operations. '''
print(area)
print(price)
# Calculate mean of area and price
mean_area = area.mean()
mean_price = price.mean()

# Calculate coefficients
numerator = 0
denominator = 0
for i in range(len(area)):
    numerator += (area[i] - mean_area) * (price[i] - mean_price)
    denominator += (area[i] - mean_area) ** 2

b = numerator / denominator
b1 = mean_price - (b * mean_area)

print("Coefficient b:", b)
print("Coefficient b1:", b1)

# Make predictions
predictions = [b * x + b1 for x in area]
print("Predictions:", predictions)

# Calculate accuracy
threshold = mean_price * 0.05
accurate_predictions = sum(abs(price[i] - predictions[i]) < threshold for i in range(len(price)))
accuracy = (accurate_predictions / len(predictions)) * 100
print("Accuracy:", accuracy)
