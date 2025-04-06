import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from lime.lime_tabular import LimeTabularExplainer
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"C:\Users\SK SAMIM ALI\Downloads\LUNG Cancer Main Data Set.csv")
#print(df.info())

# Use all columns except the target as features (X)
X = df.drop(columns=["GENDER","LUNG_CANCER"]).values

# Use "LUNG_CANCER" as the target (y)
y = df["LUNG_CANCER"].values

# Initialize parameters for K-Fold Cross Validation
n_folds = 10
indices = np.arange(len(X))
# np.random.shuffle(indices)
fold_size = len(X) // n_folds

# Lists to store metrics for each fold
accuracies = []
sensitivities = []
specificities = []
precisions = []
recalls = []
f1_scores = []


# Perform 10-fold cross-validation
for i in range(n_folds):
    # Define test and train indices
    test_indices = indices[i * fold_size:(i + 1) * fold_size]
    train_indices = np.concatenate([indices[:i * fold_size], indices[(i + 1) * fold_size:]])

    # Split the data
    X_train, X_test = X[train_indices], X[test_indices]
    y_train, y_test = y[train_indices], y[test_indices]
    
    # Calculate means for the training data
    mean_values = X_train.mean(axis=0)
    mean_LUNG_CANCER = y_train.mean()

    # Calculate coefficients
    def coefficient(column, mean_column):
        numerator = 0
        denominator = 0
        for i in range(len(X_train)):
            numerator += (X_train[i, column] - mean_column) * (y_train[i] - mean_LUNG_CANCER)
            denominator += (X_train[i, column] - mean_column) ** 2
        return numerator / denominator

    # Calculate coefficients for each feature
    coefficients = [coefficient(i, mean_values[i]) for i in range(X_train.shape[1])]

    # Calculate Y-intercept
    a = mean_LUNG_CANCER - sum(coefficients[i] * mean_values[i] for i in range(len(coefficients)))

    # Predict lung cancer for the test set
    predicted_lung_cancer = []
    for i in range(len(X_test)):
        predicted_y = a + sum(coefficients[j] * X_test[i, j] for j in range(len(coefficients)))
        y2 = np.exp(predicted_y) / (1 + np.exp(predicted_y))
        predicted_lung_cancer.append(y2)

    # Calculate accuracy
    threshold = 0.64
    predicted_labels = [1 if prob >= threshold else 0 for prob in predicted_lung_cancer]
    accuracy = accuracy_score(y_test, predicted_labels)
    print(f"Accurracy: {accuracy*100:.2f} %")
    accuracies.append(accuracy)

    # Calculate Sensitivity and Specificity
    cm = confusion_matrix(y_test, predicted_labels)
    if cm.shape[0] == 2:  # Ensure that the confusion matrix is 2x2
        TN, FP, FN, TP = cm.ravel() if cm.shape == (2, 2) else (0, 0, 0, 0)
        sensitivity = TP / (TP + FN) if (TP + FN) != 0 else 0
        specificity = TN / (TN + FP) if (TN + FP) != 0 else 0
        precision = TP / (TP + FP) if (TP + FP) != 0 else 0
        recall = TP / (TP + FN) if (TP + FN) != 0 else 0
        f1_score = 2*(precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
    else:
        sensitivity = specificity = precision = recall = f1_score = 0

    print("Confusion Matrix: TP=",TP,"TN=",TN,"FP=",FP,"FN=",FN)    
    print(f"Sensitivity: {sensitivity*100:.2f} %")
    print(f"Specificity: {specificity*100:.2f} %")
    print(f"Precision: {precision*100:.2f} %")
    print(f"Recall: {recall*100:.2f} %")
    print(f"F1 Score: {f1_score*100:.2f} %")
    print("--------------------------------------------------------------")
    sensitivities.append(sensitivity)
    specificities.append(specificity)
    precisions.append(precision)
    recalls.append(recall)
    f1_scores.append(f1_score)


    # Create a LIME explainer
    explainer = LimeTabularExplainer(
    training_data=X_train,
    feature_names=df.columns.drop("LUNG_CANCER"),
    class_names=['No Lung Cancer', 'Lung Cancer'],
    mode='classification'
)

    # Select a sample instance from the test set to explain
    instance_index = 1
    instance = X_test[instance_index]

    # Wrapper function for prediction
    def custom_predict_fn(data):
        predictions = []
        for row in data:
            pred_y = a + sum(coefficients[j] * row[j] for j in range(len(coefficients)))
            y2 = np.exp(pred_y) / (1 + np.exp(pred_y))
            predictions.append([1 - y2, y2])  # Probability of [No Lung Cancer, Lung Cancer]
        return np.array(predictions)

    # Get the explanation for this instance
    explanation = explainer.explain_instance(
        data_row=instance,
        predict_fn=custom_predict_fn
    )

    # Print the explanation
    print("Explanation for instance", instance_index)

    # Plot the explanation
    explanation.as_pyplot_figure()
    plt.show()


# Average metrics across all folds
mean_accuracy = np.mean(accuracies)
mean_sensitivity = np.mean(sensitivities)
mean_specificity = np.mean(specificities)
mean_precision = np.mean(precisions)
mean_recall = np.mean(recalls)
mean_f1_score = np.mean(f1_scores)

print(f"Mean Accuracy: {mean_accuracy*100:.2f} %")
print(f"Mean Sensitivity: {mean_sensitivity*100:.2f} %")
print(f"Mean Specificity: {mean_specificity*100:.2f} %")
print(f"Mean Precision: {mean_precision*100:.2f} %")
print(f"Mean Recall: {mean_recall*100:.2f} %")
print(f"Mean F1 Score: {mean_f1_score*100:.2f} %")