import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from lime.lime_tabular import LimeTabularExplainer
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\SK SAMIM ALI\Downloads\archive (1)\Lung_Cancer_Dataset_new.csv")
x = df[["AGE", "SMOKING", "YELLOW_FINGERS", "ANXIETY","CHRONIC DISEASE","CHEST PAIN","FATIGUE ","COUGHING"]].values
y = df["LUNG_CANCER"].values


# generate 2 class dataset
#X, y = make_classification(n_samples=1000, n_classes=2, random_state=1)
X= df.drop(columns= ['LUNG_CANCER'], axis=1)
y = df['LUNG_CANCER']

#print(X)
#print(y)

X = df.iloc[:,0:-1].values
y = df.iloc[:,-1].values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

# Train a RandomForest classifier
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# # Calculate mean of different fields
# mean_age = x[:, 0].mean()
# mean_smoking = x[:, 1].mean()
# mean_yellow_fingers = x[:, 2].mean()
# mean_anxiety = x[:, 3].mean()
# mean_chronic_disease=x[:,4].mean()
# mean_chest_pain=x[:,5].mean()
# mean_fatigue=x[:,6].mean()
# mean_coughing=x[:,7].mean()
# #mean_swalloing=x[:,8].mean()
# mean_LUNG_CANCER = y.mean()

# #calculate coefficient
# def coefficient(column,mean_column):
#     numerator = 0
#     denominator = 0
#     for i in range(len(x)):
#         numerator += (x[i, column] - mean_column) * (y[i] - mean_LUNG_CANCER)
#         denominator += (x[i, column] - mean_column) ** 2

#     b = numerator / denominator
#     return b

# b0=coefficient(0, mean_age)
# b1=coefficient(1, mean_smoking)
# b2=coefficient(2, mean_yellow_fingers)
# b3=coefficient(3, mean_anxiety)
# b4=coefficient(4, mean_chronic_disease)
# b5=coefficient(5, mean_chest_pain)
# b6=coefficient(6, mean_fatigue)
# b7=coefficient(7, mean_coughing)
# #b8=coefficient(8, mean_swalloing)

# print("Coefficient b0 (slope):", b0)
# print("Coefficient b1 (slope):", b1)
# print("Coefficient b2 (slope):", b2)
# print("Coefficient b3 (slope):", b3)
# print("Coefficient b4 (slope):", b4)
# print("Coefficient b6 (slope):", b6)
# print("Coefficient b6 (slope):", b7)
# #print("Coefficient b6 (slope):", b8)




# #calculating a
# a = mean_LUNG_CANCER - (b0 * mean_age) - (b1 * mean_smoking) - (b2 * mean_yellow_fingers) - (b3 * mean_anxiety) - (b4 *mean_chronic_disease )-(b5*mean_chest_pain)-(b6*mean_fatigue)-(b7*mean_coughing) #-(b8*mean_swalloing)
# print("Y-intercept (a):",a)

# # Predict lung cancer for each record
# predicted_lung_cancer = []
# for i in range(241,300):
#     age = x[i, 0]
#     smoking = x[i, 1]
#     yellow_fingers = x[i, 2]
#     anxiety = x[i, 3]
#     chronic_disease=x[i,4]
#     chest_pain=x[i,5]
#     fatigue=x[i,6]
#     coughing=x[i,7]
#     #swalloing=x[i,8]
#     predicted_y = a + (b0 * age) + (b1 * smoking) + (b2 * yellow_fingers) + (b3 * anxiety) + (b4*chronic_disease) + (b5*chest_pain) +(b6*fatigue)+(b7*coughing) #+(b8*swalloing)
#     y2=pow(2.718,predicted_y)/(1+pow(2.718,predicted_y))
#     predicted_lung_cancer.append(y2)

# y1_actual=[]
# for i in range (241,300):
#     y1_actual.append(y[i])


# for i in range(0,50):
#     print(y1_actual[i],predicted_lung_cancer[i])
# count=0
# for i in range (len(y1_actual)):
#     if (y1_actual[i]-predicted_lung_cancer[i])<=0.32    :
#         count+=1 
# accuracy=(count/len(y1_actual))*100
# print("Accuracy:",accuracy)


# Create a LIME explainer
explainer = LimeTabularExplainer(
    training_data=X_train,
    feature_names=X.feature_names,
    class_names=y.target_names,
    mode='classification'
)

# Select a sample instance from the test set to explain
instance_index = 1
instance = X_test[instance_index]

# Get the explanation for this instance
explanation = explainer.explain_instance(
    data_row=instance,
    predict_fn=model.predict_proba
)

# Print the explanation
print("Explanation for instance", instance_index)

# Plot the explanation
explanation.as_pyplot_figure()
plt.show()