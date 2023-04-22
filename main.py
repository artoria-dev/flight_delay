import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import data
df = pd.read_csv('Flight_delay NEU.csv')

# pandas settings
pd.set_option('display.max_columns', 30)


def info():
    print(len(df), 'x', len(df.columns))
    print(df.describe())
    print(df.info())
    print(df.isnull().sum())


def delay():
    df_delay = pd.DataFrame({'ArrDelay': [df['ArrDelay'].min(), df['ArrDelay'].max(), df['ArrDelay'].mean()],
                             'DepDelay': [df['DepDelay'].min(), df['DepDelay'].max(), df['DepDelay'].mean()],
                             'CarrierDelay': [df['CarrierDelay'].min(), df['CarrierDelay'].max(),
                                              df['CarrierDelay'].mean()],
                             'WeatherDelay': [df['WeatherDelay'].min(), df['WeatherDelay'].max(),
                                              df['WeatherDelay'].mean()],
                             'NASDelay': [df['NASDelay'].min(), df['NASDelay'].max(), df['NASDelay'].mean()],
                             'SecurityDelay': [df['SecurityDelay'].min(), df['SecurityDelay'].max(),
                                               df['SecurityDelay'].mean()],
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

    print(df['TaxiIn'].value_counts()[0.0])  # 26
    print(df['TaxiOut'].value_counts()[0.0])  # 8
    # -> 34 planes 'teleported' from the runway to the gate


def check_buggy_data():
    for i in range(len(df)):
        if df['ArrDelay'][i] != df['CarrierDelay'][i] + df['WeatherDelay'][i] + df['NASDelay'][i] + df['SecurityDelay'][
            i] + df['LateAircraftDelay'][i]:
            print('Error at row', i)


def useless_data():
    print(df['Cancelled'].sum())  # 0
    print(df['CancellationCode'].unique())  # N
    print(df['Diverted'].sum())  # 0
    # -> useless data


def tailnum_by_mean_by_count():
    """Group by TailNum and calculate mean and count of ArrDelay"""
    df_tn = df.groupby('TailNum').agg({'ArrDelay': ['mean', 'count']})
    df_tn.columns = ['mean', 'count']
    print(df_tn)


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
    # airports()
    delay_in_deph()
    # test()


if __name__ == '__main__':
    main()
