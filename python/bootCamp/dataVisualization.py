import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(r"D:\archive (2)\adult.csv")
print(df)

df_object=df.select_dtypes("object") #selects only the categorical columns      
#print(df_object)                                       


#sns.countplot(df_object['workclass'])
#sns.countplot(df_object['workclass'])
#plt.show()
sns.countplot(df_object,x='workclass')
plt.show(sns.countplot(df_object,x='workclass'))