import pandas as pd

# import data
df = pd.read_csv('Flight_delay NEU.csv')

# pandas settings
pd.set_option('display.max_columns', 30)


def info():
    print(len(df), 'x', len(df.columns))  # 100000 29
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


def check_buggy_data():
    for i in range(len(df)):
        if df['ArrDelay'][i] != df['CarrierDelay'][i] + df['WeatherDelay'][i] + df['NASDelay'][i] + df['SecurityDelay'][i] + df['LateAircraftDelay'][i]:
            print('Error at row', i)


def test():
    pass

def main():
    # info()
    # delay()
    # check_buggy_data()
    test()


if __name__ == '__main__':
    main()
