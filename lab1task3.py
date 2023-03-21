import pandas as pd

df_ma = pd.read_csv(r'D:\MA.csv', index_col = 'Дата')
df_v = pd.read_csv(r'D:\V.csv', index_col = 'Дата')
#print(df_v)
#print(df_ma)

for i in range(len(df_ma)):
    for col in df_ma.columns:
        if col == 'Объём' or col == 'Изм. %':
            df_ma[col][i] = df_ma[col][i][:-1].replace('.','').replace(',','.')
            df_v[col][i] = df_v[col][i][:-1].replace('.','').replace(',','.')
        else:
            df_ma[col][i] = df_ma[col][i].replace('.','').replace(',','.')
            df_v[col][i] = df_v[col][i].replace('.','').replace(',','.')
df_ma = df_ma.apply(pd.to_numeric)
df_v = df_v.apply(pd.to_numeric)


#print(df_v.corrwith(df_ma))

print(df_v.loc['30.12.2021'] )
df_v.loc['30.12.2021'] = None
#print(df_v)
print("_______________")
import numpy as np
from scipy.stats.mstats import winsorize
for col in df_v.columns:
    missing_value = winsorize(np.ma.masked_invalid(df_v[col]), limits=(0.25, 0.25))[3]
    print(f'{col} : {missing_value}')

print("_______________")

for col in df_v.columns:
    missing_value = df_v[col].interpolate()[3]
    print(f'{col} : {missing_value}')

print("_______________")

for col in df_v.columns:
    missing_value = (df_ma.loc['30.12.2021'][col]/df_ma.loc['31.12.2021'][col])*df_v.loc['31.12.2021'][col]
    print(f'{col} : {missing_value}')