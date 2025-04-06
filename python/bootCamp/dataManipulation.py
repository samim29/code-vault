import pandas as pd
dataframe=pd.read_csv(r"C:\Users\SK SAMIM ALI\Downloads\archive (1)\Lung_Cancer_Dataset.csv")
#pd.read_csv("C:\\Users\\SK SAMIM ALI\\Downloads\\archive (1)\\Lung_Cancer_Dataset.csv") #no need to use r as back slashes the escape charecter .

print(dataframe) #[309 rows x 16 columns]
 
print(dataframe.drop_duplicates()) #removed the duplicates but the main csv file haven't changed yet.[276 rows x 16 columns]
print(dataframe) #will print the old csv file [309 rows x 16 columns]
dataframe=dataframe.drop_duplicates()
print(dataframe) #now the main dataframe has changed
# another method without assigning it into dataframe again
dataframe.drop_duplicates(inplace=True)
print(dataframe)

print(dataframe.head())
print(dataframe.tail())
print(dataframe.head(7)) #print first 7 rows

#filtering columns
print(dataframe["GENDER"])  #single columns
print(dataframe[["GENDER","CHEST PAIN","LUNG_CANCER"]]) #multiple columns

print(dataframe["CHEST PAIN"].mean()) #finding average

print(dataframe.groupby("GENDER")["CHEST PAIN"].mean())