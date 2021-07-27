import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# call file function


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# call file
path = '/Users/nathanoliver/Desktop/Python/ERCOT_Deep_Freeze/csv/electricity_ERCOT_generation_and_interchange.csv'
df = call_file(path)

df['time'] = pd.to_datetime(df['time'])

print(df.dtypes)

df = df[df['time'] >= '2021-02-01']
df = df[df['time'] < '2021-03-01']

df['total_generation_mwh'] = df['coal_mwh'] + df['wind_mwh'] + df['solar_mwh'] + \
    df['other_mwh'] + df['nuclear_mwh'] + \
    df['natural_gas_mwh'] + df['hydro_mwh']

df['total_ties_mwh'] = df['swpp_mwh'] + df['cen_mwh']

fig, ax = plt.subplots(sharex=True, figsize=(15, 5))

ax.plot(df['time'], df['total_ties_mwh'] +
        df['total_generation_mwh'], color='red')
ax.plot(df['time'], df['total_generation_mwh'], color='black')
# ax.plot(df['time'], df['total_ties_mwh'])

ax.text(datetime(2021, 2, 14, 0), 67000, 'Net Generation\n+\nDC Tie Inflow',
        color='red', weight='bold', size=10, ha="center", va="center")

ax.text(datetime(2021, 2, 14, 0), 52000, 'Net Generation',
        color='black', weight='bold', size=10, ha="center", va="center")

ax.set_xticks(np.arange(datetime(2021, 2, 7), datetime(
    2021, 2, 26), timedelta(days=1)))
ax.set_xticklabels(['              Feb 7',
                    '            Feb 8',
                    '             Feb 9',
                    '                        Feb 10',
                    '                        Feb 11',
                    '                        Feb 12',
                    '                        Feb 13',
                    '                        Feb 14',
                    '                        Feb 15',
                    '                        Feb 16',
                    '                        Feb 17',
                    '                        Feb 18',
                    '                        Feb 19',
                    '                        Feb 20'])

ax.set_xlim([datetime(2021, 2, 10), datetime(
    2021, 2, 21)])
ax.set_ylim([30000, 70000])

title = 'Electricity Flow during 2021 Texas Power Crisis'

y_label = 'Average Hourly Power Flow\n(MW)'

ax.set_title(label=title, size=18)

ax.set_ylabel(y_label, fontsize=14)

ax.fill_between(np.arange(datetime(2021, 2, 10), datetime(
    2021, 2, 13), timedelta(days=1)), 1000, 100000, alpha=0.2, color='grey')

ax.fill_between(np.arange(datetime(2021, 2, 13), datetime(
    2021, 2, 19), timedelta(days=1)), 1000, 100000, alpha=0.2, color='green')

ax.fill_between(np.arange(datetime(2021, 2, 15), datetime(
    2021, 2, 22), timedelta(days=1)), 1000, 100000, alpha=0.2, color='purple')

ax.text(datetime(2021, 2, 11), 35000, 'Feb 10-11\nWinter Storm',
        color='black', weight='bold', size=8, ha="center", va="center")

ax.text(datetime(2021, 2, 15, 0), 35000, 'Feb 13-17\nWinter Storm Uri',
        color='black', weight='bold', size=8, ha="center", va="center")

ax.text(datetime(2021, 2, 18, 0), 35000, 'Feb 15-20\nWinter Storm Viola',
        color='black', weight='bold', size=8, ha="center", va="center")


plt.show()
