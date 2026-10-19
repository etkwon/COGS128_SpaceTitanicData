
import pandas as pd
df = pd.read_csv('P1_Spaceship.csv')

print(df.isna().sum())

df = df.drop_duplicates()

#df_dest_transp = df.dropna(subset = [ "Destination", "Transported"])

#print(df_dest_transp.isna().sum())

#ct = pd.crosstab(df_dest_transp['Destination'], df_dest_transp['Transported'])
#print(ct)

df_cabin = df.dropna(subset = ["CABIN_DECK", "CABIN_SIDE"])

print(df_cabin.isna().sum())

ct2 = pd.crosstab(df_cabin['CABIN_DECK'], df_cabin['CABIN_SIDE'])
print(ct2)



