import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# call file function


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# call file
path = '/Users/nathanoliver/Desktop/Python/ERCOT_Deep_Freeze/csv/electricity_ERCOT.csv'
df = call_file(path)


df = df.replace(' -0500', '', regex=True)
df = df.replace(' -0600', '', regex=True)

years = ['2001', '2002', '2003', '2004', '2005', '2006',
         '2007', '2008', '2009', '2010', '2011', '2012']

# df['time'] = df['time'].replace(year, '', regex=True)

print(df.head())

for i in range(len(df)):
    n = df.loc[i, 'time']
    s = n[4]

    if s == '/':
        df.loc[i, 'time'] = n[2:]
        df.loc[i, 'time'] = pd.to_datetime(
            df.loc[i, 'time'], format='%m/%d/%y %H:%M')

    else:

        df.loc[i, 'time'] = pd.to_datetime(
            df.loc[i, 'time'], format='%m/%d/%y %H:%M')


print(df.columns)
print(df.dtypes)

path_new = '/Users/nathanoliver/Desktop/Python/ERCOT_Deep_Freeze/csv/electricity_ERCOT_new.csv'

df.to_csv(path_new)
