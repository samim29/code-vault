import pandas as pd
df = pd.read_csv(r"C:\Users\SK SAMIM ALI\Downloads\archive (1)\Lung_Cancer_Dataset_new.csv")
x = df[["AGE", "SMOKING", "YELLOW_FINGERS", "ANXIETY","CHRONIC DISEASE","CHEST PAIN","FATIGUE ","COUGHING"]].values
y = df["LUNG_CANCER"].values

# Calculate mean of different fields
mean_age = x[:, 0].mean()
mean_smoking = x[:, 1].mean()
mean_yellow_fingers = x[:, 2].mean()
mean_anxiety = x[:, 3].mean()
mean_chronic_disease=x[:,4].mean()
mean_chest_pain=x[:,5].mean()
mean_fatigue=x[:,6].mean()
mean_coughing=x[:,7].mean()
mean_LUNG_CANCER = y.mean()

#function to calculate coefficient
def coefficient(column,mean_column):
    numerator = 0
    denominator = 0
    for i in range(len(x)):
        numerator += (x[i, column] - mean_column) * (y[i] - mean_LUNG_CANCER)
        denominator += (x[i, column] - mean_column) ** 2

    b = numerator / denominator
    return b

#calculating coefficients
b0=coefficient(0, mean_age)
b1=coefficient(1, mean_smoking)
b2=coefficient(2, mean_yellow_fingers)
b3=coefficient(3, mean_anxiety)
b4=coefficient(4, mean_chronic_disease)
b5=coefficient(5, mean_chest_pain)
b6=coefficient(6, mean_fatigue)
b7=coefficient(7, mean_coughing)

#printing coefficients
print("Coefficient b0 (slope):", b0)
print("Coefficient b1 (slope):", b1)
print("Coefficient b2 (slope):", b2)
print("Coefficient b3 (slope):", b3)
print("Coefficient b4 (slope):", b4)
print("Coefficient b6 (slope):", b6)
print("Coefficient b6 (slope):", b7)



#calculating a
a = mean_LUNG_CANCER - (b0 * mean_age) - (b1 * mean_smoking) - (b2 * mean_yellow_fingers) - (b3 * mean_anxiety) - (b4 *mean_chronic_disease )-(b5*mean_chest_pain)-(b6*mean_fatigue)-(b7*mean_coughing) 
print("Y-intercept (a):",a)

# Predict lung cancer for each record
predicted_lung_cancer = []
for i in range(241,300):
    age = x[i, 0]
    smoking = x[i, 1]
    yellow_fingers = x[i, 2]
    anxiety = x[i, 3]
    chronic_disease=x[i,4]
    chest_pain=x[i,5]
    fatigue=x[i,6]
    coughing=x[i,7]
    
    predicted_y = a + (b0 * age) + (b1 * smoking) + (b2 * yellow_fingers) + (b3 * anxiety) + (b4*chronic_disease) + (b5*chest_pain) +(b6*fatigue)+(b7*coughing) 
    y2=pow(2.718,predicted_y)/(1+pow(2.718,predicted_y))
    predicted_lung_cancer.append(y2)

y1_actual=[]
for i in range (241,300):
    y1_actual.append(y[i])


for i in range(0,50):
    print(y1_actual[i],predicted_lung_cancer[i])
count=0
for i in range (len(y1_actual)):
    if (y1_actual[i]-predicted_lung_cancer[i])<=0.32    :
        count+=1 
accuracy=(count/len(y1_actual))*100
print("Accuracy:",accuracy)