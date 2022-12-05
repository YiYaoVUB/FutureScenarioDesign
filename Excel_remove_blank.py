import pandas as pd
import os

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f.endswith('.csv'):
                fullname = os.path.join(root, f)
                yield fullname

base = 'C:\Research2\ISIMIP3a\out_file_1991_2010\\'
for name in findAllFile(base):
    output = name + '_noblank.csv'
    df = pd.read_csv(name)
    # d = df[['iso3', 'mean', 'count']]       #may need to be changed
    # d.dropna(subset=['mean', 'count'], inplace=True)
    d = df[['iso3', 'mean']]
    d.dropna(subset=['mean'], inplace=True)
    d.dropna(subset=['iso3'], inplace=True)
    #print(df.index[[197]])
    #d.drop(df.index[[197]], axis = 0, inplace=True)
    d.to_csv(output, index= False)
    print('test')


