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


# df1 = df1[df1['Balancing Authority'] == 'ERCO']

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(15, 8))

print(df1.dtypes)

ax1.plot(df3['Local Time at End of Hour'], df3['Interchange (MW)'] * -1)
ax2.plot(df2['Local Time at End of Hour'], df2['Interchange (MW)'] * -1)


ax1.fill_between(np.arange(datetime(2021, 2, 10), datetime(
    2021, 2, 13), timedelta(days=1)), 1000, -1000, alpha=0.2, color='grey')

ax1.fill_between(np.arange(datetime(2021, 2, 13), datetime(
    2021, 2, 19), timedelta(days=1)), 1000, -1000, alpha=0.2, color='green')

ax1.fill_between(np.arange(datetime(2021, 2, 15), datetime(
    2021, 2, 22), timedelta(days=1)), 1000, -1000, alpha=0.2, color='purple')

ax2.fill_between(np.arange(datetime(2021, 2, 10), datetime(
    2021, 2, 13), timedelta(days=1)), 1000, -1000, alpha=0.2, color='grey')

ax2.fill_between(np.arange(datetime(2021, 2, 13), datetime(
    2021, 2, 19), timedelta(days=1)), 1000, -1000, alpha=0.2, color='green')

ax2.fill_between(np.arange(datetime(2021, 2, 15), datetime(
    2021, 2, 22), timedelta(days=1)), 1000, -1000, alpha=0.2, color='purple')

ax2.set_xticks(np.arange(datetime(2021, 2, 7), datetime(
    2021, 2, 26), timedelta(days=1)))
ax2.set_xticklabels(['              Feb 7',
                     '            Feb 8',
                     '             Feb 9',
                     '             Feb 10',
                     '             Feb 11',
                     '            Feb 12',
                     '            Feb 13',
                     '             Feb 14',
                     '            Feb 15',
                     '            Feb 16',
                     '             Feb 17',
                     '             Feb 18',
                     '             Feb 19',
                     '             Feb 20',
                     '             Feb 21',
                     '             Feb 22',
                     '             Feb 23',
                     '             Feb 24',
                     '             Feb 25',
                     '             Feb 26'])

ax1.set_xlim([datetime(2021, 2, 7), datetime(
    2021, 2, 26)])
ax2.set_ylim([-500, 500])
ax1.set_ylim([-1000, 1000])


title1 = 'HVDC Interconnection Electricity Flow during 2021 Texas Power Crisis\n\nElectricity Flow from SPP to ERCOT'
title2 = 'Electricity Flow from CENACE to ERCOT'

ax1.set_title(label=title1, size=18)
ax2.set_title(label=title2, size=18)

y_label = 'Average Hourly Power Flow\n(MW)'

ax1.set_ylabel(y_label, fontsize=14)
ax2.set_ylabel(y_label, fontsize=14)


# ax1.set_facecolor('#ECECEC')

# plt.xticks(fontsize=l_size)
# plt.yticks(fontsize=l_size)

ax1.axhline(y=820, xmin=0, xmax=10,
            linewidth=1, color='red', linestyle='--')
ax1.axhline(y=-820, xmin=0, xmax=10,
            linewidth=1, color='red', linestyle='--')

ax2.axhline(y=436, xmin=0, xmax=10,
            linewidth=1, color='red', linestyle='--')
ax2.axhline(y=-436, xmin=0, xmax=10,
            linewidth=1, color='red', linestyle='--')

ax1.axhline(y=0, xmin=0, xmax=1,
            linewidth=1, color='black', linestyle='--')
ax2.axhline(y=0, xmin=0, xmax=10,
            linewidth=1, color='black', linestyle='--')

ax1.text(datetime(2021, 2, 23, 12), 600, '820 MW\nDC Interconnections\nTotal Rated Capacity',
         color='red', weight='bold', size=10, ha="center", va="center")
ax2.text(datetime(2021, 2, 23, 12), 330, '436 MW\nDC Interconnections\nTotal Rated Capacity',
         color='red', weight='bold', size=10, ha="center", va="center")


ax1.text(datetime(2021, 2, 11), -400, 'Feb 10-11\nWinter Storm',
         color='black', weight='bold', size=8, ha="center", va="center")

ax1.text(datetime(2021, 2, 15, 0), -400, 'Feb 13-17\nWinter Storm Uri',
         color='black', weight='bold', size=8, ha="center", va="center")

ax1.text(datetime(2021, 2, 18, 0), -400, 'Feb 15-20\nWinter Storm Viola',
         color='black', weight='bold', size=8, ha="center", va="center")

ax2.text(datetime(2021, 2, 11), -200, 'Feb 10-11\nWinter Storm',
         color='black', weight='bold', size=8, ha="center", va="center")

ax2.text(datetime(2021, 2, 15, 0), -200, 'Feb 13-17\nWinter Storm Uri',
         color='black', weight='bold', size=8, ha="center", va="center")

ax2.text(datetime(2021, 2, 18, 0), -200, 'Feb 15-20\nWinter Storm Viola',
         color='black', weight='bold', size=8, ha="center", va="center")


plt.show()


# lw = 3
# source = 'Source: EIA'
# # * purchase price is assumed to be delivered coal cost minus transportation cost

# m_size = 15
# l_size = 12

# colors = ['#e15759', '#f28e2b', '#edc948',
#           '#59a14f', '#76b7b2', '#4e79a7', '#b07aa1']

# # plot figure
# fig, ax = plt.subplots(sharex=True, figsize=(12, 6))

# ax.plot(df.loc[:, 'delivered'], color='black', linewidth=lw)
# ax.plot(df.loc[:, 'transportation'], color=colors[0], linewidth=lw)
# ax.plot(df.loc[:, 'delivered'] - df.loc[:, 'transportation'],
#         color=colors[1], linewidth=lw)

# ax.set_title('US Coal Prices Delivered to Power Sector\n', fontsize=20)
# ax.set_ylabel('USD per Short Ton\n', fontsize=m_size)


# plt.text(0.1045, 0.01, source, fontsize=l_size,
#          transform=plt.gcf().transFigure)
# plt.text(0.44, 0.78, 'Delivered Coal Price', fontsize=m_size,
#          transform=plt.gcf().transFigure)
# plt.text(0.465, 0.53, 'Purchase Price',
#          fontsize=m_size, color=colors[1], transform=plt.gcf().transFigure)
# # plt.text(0.59, 0.54, '*',
# #          fontsize=m_size, color=colors[1], transform=plt.gcf().transFigure)
# plt.text(0.442, 0.38, 'Transportation Cost',
#          fontsize=m_size, color=colors[0], transform=plt.gcf().transFigure)

# plt.show()
