import pandas as pd
import re
df = pd.read_csv('data.csv')
#df_xlsx = pd.read_excel('data.xlsx')
# df_txt=pd.read_csv('data.txt',delimiter="\t")
# print(df_txt)
# print(df_xlsx)
# print(df.head(3)) # print top 3 rows
# print(df.tail(3))  # print bottom 3 rows
# read headers :
df.columns
# read each/specific column e.g get Name
df['Name']
# read multiple columns
df[['Name', 'Type 1', 'Type 2']]
# read rows e.g row 1 to 4
df.iloc[1:4]
# read specific data from row/column e.g data from 3rd row column 2
df.iloc[2, 1]
# look for value base on value not index , e.g find all the rows with Type 1=Fire
#print(df.loc[df["Type 1"] == "Fire"])
#print(df.loc[((df["Type 1"] == "Fire") & (df["Type 2"]=="Posion"))])
# Generate descriptive statistics
df.describe()
# sorted the value
df.sort_values(['Name', 'HP'], ascending=[1, 0])
# make changes e.g add new column
# df['total'] = df['HP']+df['Attack']+df['Defense'] + \
#     df['Sp. Atk']+df['Sp. Def']+df['Speed']
# altrenative
df['total'] = df.iloc[:, 4:10].sum(axis=1)
# print(df.head(1))
# df = df.drop(columns='total')
# print(df.head(2))
# change columns
col = list(df.columns)
df = df[col[0:4]+[col[-1]]+col[4:12]]
# print(df.head(1))
df.to_csv('modified.csv')
# filter data
new_df = df.loc[(df["Type 1"] == "Grass") & (
    df["Type 2"] == "Poison") & (df['HP'] > 70)]
# print(new_df.reset_index(drop=True))
new_df.to_csv('filter_data.csv')
# filter textual
df.loc[df['Name'].str.contains('Mega')]
df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]
# aggregate stat
df.groupby(['Type 1']).mean().sort_values('Defense', ascending=True)
df.groupby(['Type 1']).count()
df['count'] = 1
df.groupby(['Type 1']).count()['count']
