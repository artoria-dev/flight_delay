import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np




# import data
df = pd.read_csv('Flight_delay NEU.csv')

# pandas settings
pd.set_option('display.max_columns', 30)


def info():
    print(df.shape)
    print("--------------------")
    print(len(df), 'x', len(df.columns))
    print("--------------------")
    print("describe")
    print(df.describe())
    print("--------------------")
    print("info")
    print(df.info())
    print("--------------------")
    print("null values")
    print(df.isnull().sum())
    print("--------------------")
    print("columns")
    print(df.columns)


def delay():
    df_delay = pd.DataFrame({
        'ArrDelay': [df['ArrDelay'].min(), df['ArrDelay'].max(), df['ArrDelay'].mean()],
        'DepDelay': [df['DepDelay'].min(), df['DepDelay'].max(), df['DepDelay'].mean()],
        'CarrierDelay': [df['CarrierDelay'].min(), df['CarrierDelay'].max(), df['CarrierDelay'].mean()],
        'WeatherDelay': [df['WeatherDelay'].min(), df['WeatherDelay'].max(), df['WeatherDelay'].mean()],
        'NASDelay': [df['NASDelay'].min(), df['NASDelay'].max(), df['NASDelay'].mean()],
        'SecurityDelay': [df['SecurityDelay'].min(), df['SecurityDelay'].max(), df['SecurityDelay'].mean()],
        'LateAircraftDelay': [df['LateAircraftDelay'].min(), df['LateAircraftDelay'].max(),
                              df['LateAircraftDelay'].mean()]})
    df_delay.index = ['min', 'max', 'mean']
    print(df_delay)


def taxi_time():
    df_taxi = pd.DataFrame({'TaxiIn': [df['TaxiIn'].min(), df['TaxiIn'].max(), df['TaxiIn'].mean()],
                            'TaxiOut': [df['TaxiOut'].min(), df['TaxiOut'].max(), df['TaxiOut'].mean()]})
    df_taxi.index = ['min', 'max', 'mean']
    print(df_taxi)
    # -> 0.0 shouldnt be possible

    print('amt taxiIn = 0:', df['TaxiIn'].value_counts()[0.0])  # 26
    print('amt taxiOut = 0:', df['TaxiOut'].value_counts()[0.0])  # 8
    # -> 34 planes 'teleported' from the runway to the gate


def check_buggy_data():
    for i in range(len(df)):

        """for each entry, checks if ArrDelay is equal to the sum of all other delays"""
        if df['ArrDelay'][i] != df['CarrierDelay'][i] + df['WeatherDelay'][i] + df['NASDelay'][i] + df['SecurityDelay'][
            i] + df['LateAircraftDelay'][i]:
            print('ArrDelay != Sum(otherDelays) AT: ', i)

        """for each entry, checks if ActualElapsedTime-(TaxiIn+TaxiOut) is equal to AirTime"""
        if df['ActualElapsedTime'][i] - (df['TaxiIn'][i] + df['TaxiOut'][i]) != df['AirTime'][i]:
            print('ActualElapsedTime-(TaxiIn+TaxiOut) != AirTime AT:', i)


def useless_data():
    print(df['Cancelled'].sum())  # 0
    print(df['CancellationCode'].unique())  # N
    print(df['Diverted'].sum())  # 0
    # -> useless data


def tailnum_by_mean_by_count():
    df_tn = df.groupby('TailNum').agg({'ArrDelay': ['mean', 'count']})
    df_tn.columns = ['mean', 'count']
    print(df_tn)

    # ITS SCATTER TIME
    sns.scatterplot(x=df_tn['count'], y=df_tn['mean'])

    # mean for mean and mean for count
    plt.axhline(df_tn['mean'].mean(), color='red', linestyle='--')
    plt.axvline(df_tn['count'].mean(), color='green', linestyle='--')
    plt.text(290, df_tn['mean'].mean() + 5, 'mean of mean', color='red', weight='bold')
    plt.text(df_tn['count'].mean() + 5, 100, 'mean of count', color='green', weight='bold', rotation=90)

    # average max and min delay
    plt.axhline(df_tn['mean'].mean() + df_tn['mean'].std(), color='red', linestyle='--')
    plt.axhline(df_tn['mean'].mean() - df_tn['mean'].std(), color='red', linestyle='--')
    plt.text(290, df_tn['mean'].mean() + df_tn['mean'].std() + 5, 'mean+std', color='red', weight='bold')
    plt.text(290, df_tn['mean'].mean() - df_tn['mean'].std() + 5, 'mean-std', color='red', weight='bold')

    # average max and min count
    plt.axvline(df_tn['count'].mean() + df_tn['count'].std(), color='green', linestyle='--')
    plt.axvline(df_tn['count'].mean() - df_tn['count'].std(), color='green', linestyle='--')
    plt.text(df_tn['count'].mean() + df_tn['count'].std() + 5, 100, 'mean+std', color='green', weight='bold',
             rotation=90)
    plt.text(df_tn['count'].mean() - df_tn['count'].std() + 5, 100, 'mean-std', color='green', weight='bold',
             rotation=90)

    # top right corner text
    plt.text(250, 265, 'mean of mean: ' + str(round(df_tn['mean'].mean(), 2)), color='red')
    plt.text(250, 250, 'std of mean: ' + str(round(df_tn['mean'].std(), 2)), color='red')
    plt.text(250, 225, 'mean of count: ' + str(round(df_tn['count'].mean(), 2)), color='green')
    plt.text(250, 210, 'std of count: ' + str(round(df_tn['count'].std(), 2)), color='green')

    plt.title('TailNum by mean by count')

    plt.show()


def tailnum_by_mean_by_count_removed_extremes():
    # same as above, but count<11 removed for better visibility
    df_tn = df.groupby('TailNum').agg({'ArrDelay': ['mean', 'count']})
    df_tn.columns = ['mean', 'count']
    df_tn = df_tn[df_tn['count'] > 11]

    # ITS SCATTER TIME (again)
    sns.scatterplot(x=df_tn['count'], y=df_tn['mean'])

    # mean for mean and mean for count
    plt.axhline(df_tn['mean'].mean(), color='red', linestyle='--')
    plt.axvline(df_tn['count'].mean(), color='green', linestyle='--')
    plt.text(290, df_tn['mean'].mean() + 5, 'mean of mean', color='red', weight='bold')
    plt.text(df_tn['count'].mean() + 5, 100, 'mean of count', color='green', weight='bold', rotation=90)

    # average max and min delay
    plt.axhline(df_tn['mean'].mean() + df_tn['mean'].std(), color='red', linestyle='--')
    plt.axhline(df_tn['mean'].mean() - df_tn['mean'].std(), color='red', linestyle='--')
    plt.text(290, df_tn['mean'].mean() + df_tn['mean'].std() + 5, 'mean+std', color='red', weight='bold')
    plt.text(290, df_tn['mean'].mean() - df_tn['mean'].std() + 5, 'mean-std', color='red', weight='bold')

    # average max and min count
    plt.axvline(df_tn['count'].mean() + df_tn['count'].std(), color='green', linestyle='--')
    plt.axvline(df_tn['count'].mean() - df_tn['count'].std(), color='green', linestyle='--')
    plt.text(df_tn['count'].mean() + df_tn['count'].std() + 5, 100, 'mean+std', color='green', weight='bold',
             rotation=90)
    plt.text(df_tn['count'].mean() - df_tn['count'].std() + 5, 100, 'mean-std', color='green', weight='bold',
             rotation=90)

    # top right corner text
    plt.text(250, 130, 'mean of mean: ' + str(round(df_tn['mean'].mean(), 2)), color='red')
    plt.text(250, 125, 'std of mean: ' + str(round(df_tn['mean'].std(), 2)), color='red')
    plt.text(250, 115, 'mean of count: ' + str(round(df_tn['count'].mean(), 2)), color='green')
    plt.text(250, 110, 'std of count: ' + str(round(df_tn['count'].std(), 2)), color='green')

    plt.title('TailNum by mean by count (count>11)')

    plt.show()


def airports():
    """Group by Origin and calculate mean and count of ArrDelay"""
    df_airports = df.groupby('Origin').agg({'ArrDelay': ['mean', 'count']})
    df_airports.columns = ['mean', 'count']
    print(df_airports)
    print(len(df_airports))  # 274


def delay_in_deph():
    df_delay = df[['ArrDelay', 'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']]
    corr = df_delay.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.tight_layout()
    plt.title('Correlation between delays')

    # resizing
    fig = plt.gcf()
    fig.set_size_inches(8, 6)

    plt.show()


def delay_by_carrier():
    df_carrier = df.groupby('UniqueCarrier').agg({'ArrDelay': ['mean', 'count']})
    df_carrier.columns = ['mean', 'count']
    print(df_carrier)
    df_carrier = df_carrier.sort_values(by='mean')

    fig, ax1 = plt.subplots()
    ax1.bar(df_carrier.index, df_carrier['mean'], color='darkblue')
    ax1.set_ylabel('Mean ArrDelay in m', rotation=90, color='darkblue')
    ax2 = ax1.twinx()
    ax2.plot(df_carrier.index, df_carrier['count'], color='red')
    ax2.set_ylabel('Count of delayed flights', rotation=270, color='red', labelpad=15)
    plt.title('Mean of ArrDelay and count of flights by carrier')

    plt.subplots_adjust(right=0.8)

    plt.show()


def time_of_day_by_day_of_week():
    df_time = df.groupby(['DayOfWeek', 'DepTime']).agg({'ArrDelay': ['mean']})
    df_time.columns = ['mean']
    df_time = df_time.reindex(pd.MultiIndex.from_product([df_time.index.levels[0], range(100, 2500, 100)]))
    # df_time = df_time.fillna(df_time.mean())
    sns.heatmap(df_time['mean'].unstack(), cmap='coolwarm')
    # replace xticks with time
    xticks = [str(i)[:-2] + ':' + str(i)[-2:] for i in range(100, 2500, 100)]
    plt.xticks(range(24), xticks, rotation=45)
    # replace yticks with day of week
    yticks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    plt.yticks(range(7), yticks, rotation=45)
    plt.xlabel('Departure Time')
    plt.ylabel('Day of Week')
    plt.title('Mean of ArrDelay by Departure Time and Day of Week')
    # resizing
    fig = plt.gcf()
    fig.set_size_inches(10, 6)
    plt.show()


def time_of_day_by_day_of_week_extremes_only():
    df_tmp = df[(df['DepTime'] >= 2100) | (df['DepTime'] <= 600)]
    df_time = df_tmp.groupby(['DayOfWeek', 'DepTime']).agg({'ArrDelay': ['mean']})
    df_time.columns = ['mean']
    df_time = df_time.reindex(
        pd.MultiIndex.from_product([df_time.index.levels[0], [2100, 2200, 2300, 2400, 100, 200, 300, 400, 500, 600]]))
    sns.heatmap(df_time['mean'].unstack(), cmap='coolwarm')
    yticks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    plt.yticks(range(7), yticks, rotation=45)
    xticks = ['1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '21:00', '22:00', '23:00', '24:00']
    plt.xticks(range(10), xticks, rotation=45)
    plt.xlabel('Departure Time')
    plt.ylabel('Day of Week')
    plt.title('Mean of ArrDelay by Departure Time and Day of Week')
    # resizing
    fig = plt.gcf()
    fig.set_size_inches(10, 6)
    plt.show()


def avg_delay_per_flight_per_carrier():
    delay_totals = df.groupby('UniqueCarrier')['ArrDelay'].agg(['sum', 'count'])
    delay_totals['avg_delay_per_flight'] = delay_totals['sum'] / delay_totals['count']
    delay_totals = delay_totals.sort_values(by='avg_delay_per_flight', ascending=False)
    print(delay_totals)


def missing_airport_names():
    print(df['Org_Airport'].isnull().sum())  # 1177
    print(df['Dest_Airport'].isnull().sum())  # 1479


def CG_histogram():
    plt.hist(df['ArrDelay'], bins=50, edgecolor='k')
    plt.xlabel('Flight Delay (minutes)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Flight Delays')

    # display max delay line
    max_delay = df['ArrDelay'].max()
    plt.axvline(max_delay, color='r', linestyle='dashed', linewidth=1)
    plt.text(max_delay - 250, 200000, 'Max Delay', rotation=45)

    # resizing
    fig = plt.gcf()
    fig.set_size_inches(8, 6)

    plt.show()


def CG_histogram_removed_extremes():
    plt.hist(df['ArrDelay'], bins=50, edgecolor='k', range=[0, 500])
    plt.xlabel('Flight Delay (minutes)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Flight Delays - Removed Extremes')

    # resizing
    fig = plt.gcf()
    fig.set_size_inches(8, 6)

    plt.show()


def test():
    pass



def main():
    # info()
    # delay()
    # taxi_time()
    # check_buggy_data()
    # cancellation()
    # useless_data()
    # tailnum_by_mean_by_count()
    # tailnum_by_mean_by_count_removed_extremes()
    # airports()
    # delay_in_deph()
    # delay_by_carrier()
    # time_of_day_by_day_of_week()
    time_of_day_by_day_of_week_extremes_only()
    # avg_delay_per_flight_per_carrier()
    # missing_airport_names()

    # CG_histogram()
    # CG_histogram_removed_extremes()

    # test()


if __name__ == '__main__':
    main()
