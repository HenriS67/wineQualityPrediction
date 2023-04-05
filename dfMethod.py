import pandas as pd

#renvoie les couples (ligne,colonne,valeur) tel que min<valeur<max dans df
def dfSeuilValue(min,df):
    for i in range(len(df)):
        for j in range(len(df.columns)):
                if(abs(df.iloc[i][j])>=min and i!=j):
                    print(df.columns[i],df.columns[j],df.iloc[i][j])
