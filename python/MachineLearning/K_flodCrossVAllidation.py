import pandas as pd
from sklearn.model_selection import KFold #This line of code imports the KFold class from the sklearn.model_selection module in scikit-learn.

df = pd.read_csv(r"C:\Users\SK SAMIM ALI\Downloads\archive\diabetes_prediction_dataset.csv",nrows=500) #nrows is a parameter in the pd.read_csv() function in pandas, which specifies the number of rows of the file to read.

age = df["age"].values
blood_glucose_level = df["blood_glucose_level"].values

# Define the number of folds
k_folds = 10

# Initialize KFold cross-validator
kf = KFold(n_splits=k_folds) #This line of code initializes a k-fold cross-validator object using the KFold class from scikit-learn.

accuracies = []

for train_index, test_index in kf.split(age):
    # Split data into training and test sets
    age_train, age_test = age[train_index], age[test_index]
    blood_glucose_level_train, blood_glucose_level_test = blood_glucose_level[train_index], blood_glucose_level[test_index]
    
    # Calculate coefficients on training set
    mean_age_train = age_train.mean()
    mean_blood_glucose_level_train = blood_glucose_level_train.mean()
    
    numerator = 0
    denominator = 0
    for i in range(len(age_train)):
        numerator += (age_train[i] - mean_age_train) * (blood_glucose_level_train[i] - mean_blood_glucose_level_train)
        denominator += (age_train[i] - mean_age_train) ** 2
    
    b = numerator / denominator
    b1 = mean_blood_glucose_level_train - (b * mean_age_train)
    
    # Make predictions on test set
    predictions = [b * x + b1 for x in age_test]
    
    # Calculate accuracy
    threshold = mean_blood_glucose_level_train * 0.50
    accurate_predictions = sum(abs(blood_glucose_level_test[i] - predictions[i]) < threshold for i in range(len(blood_glucose_level_test)))
    accuracy = (accurate_predictions / len(predictions)) * 100
    accuracies.append(accuracy)

# Calculate the average accuracy across all folds
print(accuracies)
average_accuracy = sum(accuracies) / len(accuracies)
print("Average Accuracy:", average_accuracy)
