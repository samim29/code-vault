import pandas as pd
df=pd.read_csv(r"C:\Users\SK SAMIM ALI\Downloads\archive (2)\adult.csv")

print(df.shape) #no of rows and columns (32561, 15)
print(df.shape[0]) #no of rows
print(df.shape[1]) #no of columns

df.drop_duplicates(inplace=True)

print(df.isna()) #null value of empty values
print(df.isna().sum()) #all the columns having and how many null values the have
print(df.isna().sum().sum()) # total number of null values in whole data set  
print(df.describe())
print(df.info())
print(df)
