import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# call file function


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# call file
path1 = '/Users/nathanoliver/Desktop/Python/ERCOT_Deep_Freeze/csv/EIA930_INTERCHANGE_2021_Jan_Jun.csv'
df1 = call_file(path1)


print(df1.columns)
print(df1.dtypes)

# df1 = df1.replace(',', '', regex=True)
pd.to_numeric(df1['Interchange (MW)'])
df1['Local Time at End of Hour'] = pd.to_datetime(
    df1['Local Time at End of Hour'])
df1['UTC Time at End of Hour'] = pd.to_datetime(df1['UTC Time at End of Hour'])
df1['Data Date'] = pd.to_datetime(df1['Data Date'])

print(df1.dtypes)

print(df1.loc[0, 'Data Date'])

# df1 = df1[df1['Balancing Authority'] == 'ERCO']
df1 = df1[df1['Balancing Authority'] == 'ERCO']
print(df1['Balancing Authority'].unique())

print(df1['Directly Interconnected Balancing Authority'].unique())
df1 = df1[df1['Data Date'] >= '2021-02-01']
df1 = df1[df1['Data Date'] < '2021-03-01']
df2 = df1[df1['Directly Interconnected Balancing Authority'] == 'CEN']
df3 = df1[df1['Directly Interconnected Balancing Authority'] == 'SWPP']

path_new1 = '/Users/nathanoliver/Desktop/Python/ERCOT_Deep_Freeze/csv/electricity_ERCOT_DC_ties_February_CEN.csv'
path_new2 = '/Users/nathanoliver/Desktop/Python/ERCOT_Deep_Freeze/csv/electricity_ERCOT_DC_ties_February_SWPP.csv'

df2.to_csv(path_new1)
df3.to_csv(path_new2)
