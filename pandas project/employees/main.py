import pandas as pd

df=pd.read_excel("C:\\Users\\bhanu\\OneDrive\\Desktop\\projects\\employee_dataset.xlsx")

df=df.drop_duplicates()

num_cols=['Age','Years_of_Experience','Annual_Salary ($)','Performance_Score','Annual_Bonus ($)']
for col in num_cols:
    df[col]=df[col].fillna(df[col].median())

cat_cols=['Gender','Department','Education_Level','Employment_Status','City']
for col in cat_cols:
    df[col]=df[col].fillna('Unknown')

df['Age']=df['Age'].astype(int) 
df['Years_of_Experience']=df['Years_of_Experience'].astype(int)


df.to_excel("employee_dataset_cleaned.xlsx", index=False)

