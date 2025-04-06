import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\SK SAMIM ALI\Downloads\archive (1)\Lung_Cancer_Dataset.csv")
x = df[["ALLERGY ", "WHEEZING", "ALCOHOL CONSUMING", "COUGHING","SWALLOWING DIFFICULTY"]].values
y = df["LUNG_CANCER"].values

# Calculate mean of different fields
mean_allergy = x[:, 0].mean()
mean_wheezing = x[:, 1].mean()
mean_alcohol_consuming = x[:, 2].mean()
mean_coughing = x[:, 3].mean()
mean_swallowing_difficulty=x[:,4].mean()
mean_LUNG_CANCER = y.mean()

# Calculate coefficients b0
numerator = 0
denominator = 0
for i in range(len(x)):
    numerator += (x[i, 0] - mean_allergy) * (y[i] - mean_LUNG_CANCER)
    denominator += (x[i, 0] - mean_allergy) ** 2

b0 = numerator / denominator

print("Coefficient b0 (slope):", b0)

# Calculate coefficients b1
numerator = 0
denominator = 0
for i in range(len(x)):
    numerator += (x[i, 1] - mean_wheezing) * (y[i] - mean_LUNG_CANCER)
    denominator += (x[i, 1] - mean_wheezing) ** 2

b1 = numerator / denominator

print("Coefficient b1 (slope):", b1)


# Calculate coefficients b2
numerator = 0
denominator = 0
for i in range(len(x)):
    numerator += (x[i, 2] - mean_alcohol_consuming) * (y[i] - mean_LUNG_CANCER)
    denominator += (x[i, 2] - mean_alcohol_consuming) ** 2

b2 = numerator / denominator

print("Coefficient b2 (slope):", b2)


# Calculate coefficients b3
numerator = 0
denominator = 0
for i in range(len(x)):
    numerator += (x[i, 3] - mean_coughing) * (y[i] - mean_LUNG_CANCER)
    denominator += (x[i, 3] - mean_coughing) ** 2

b3 = numerator / denominator

print("Coefficient b3 (slope):", b3)

# Calculate coefficients b4
numerator = 0
denominator = 0
for i in range(len(x)):
    numerator += (x[i, 3] - mean_swallowing_difficulty) * (y[i] - mean_LUNG_CANCER)
    denominator += (x[i, 3] - mean_swallowing_difficulty) ** 2

b4 = numerator / denominator

print("Coefficient b4 (slope):", b4)

#calculating a
a = mean_LUNG_CANCER - (b0 * mean_allergy) - (b1 * mean_wheezing) - (b2 * mean_alcohol_consuming) - (b3 * mean_coughing)-(b4*mean_swallowing_difficulty)
print("Y-intercept (a):",a)

# Predict lung cancer for each record
predicted_lung_cancer = []
for i in range(241,300):
    allergy = x[i, 0]
    wheezing= x[i, 1]
    alcohol_consuming = x[i, 2]
    coughing = x[i, 3]
    swallowing_difficulty=x[i,4]
    

    predicted_y = a + (b0 * allergy) + (b1 * wheezing) + (b2 * alcohol_consuming) + (b3 * coughing) +(b4*swallowing_difficulty)
    y2=pow(2.718,predicted_y)/(1+pow(2.718,predicted_y)) #logistic regression
    predicted_lung_cancer.append(y2)

#print(predicted_lung_cancer)
y1_actual=[]
for i in range (241,300):
    y1_actual.append(y[i])
#print(y1_actual)
print("Actual values  :  Predicted values")
for i in range(0,50):
    print(y1_actual[i],"\t\t",predicted_lung_cancer[i])
count=0
for i in range (len(y1_actual)):
    if (y1_actual[i]-predicted_lung_cancer[i])<=0.32    :
        count+=1 
accuracy=(count/len(y1_actual))*100
print("Accuracy is : ",accuracy)