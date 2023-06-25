# Flight Delay Analysis

## Getting Started

### Necessary Packages

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

### Loading Dataset

    df = pd.read_csv('flight_delay.csv')

### Get to know Dataset
**df.shape**

    (484551, 29)

**df.head()**

       DayOfWeek        Date  DepTime  ArrTime  CRSArrTime UniqueCarrier   
    0          4  03-01-2022     1829     1959        1925            WN  \
    1          4  03-01-2022     1937     2037        1940            WN   
    2          4  03-01-2022     1644     1845        1725            WN   
    3          4  03-01-2022     1452     1640        1625            WN   
    4          4  03-01-2022     1323     1526        1510            WN   
    
                      Airline  FlightNum TailNum  ActualElapsedTime   
    0  Southwest Airlines Co.       3920  N464WN                 90  \
    1  Southwest Airlines Co.        509  N763SW                240   
    2  Southwest Airlines Co.       1333  N334SW                121   
    3  Southwest Airlines Co.        675  N286WN                228   
    4  Southwest Airlines Co.          4  N674AA                123   
    
       CRSElapsedTime  AirTime  ArrDelay  DepDelay Origin   
    0              90       77        34        34    IND  \
    1             250      230        57        67    IND   
    2             135      107        80        94    IND   
    3             240      213        15        27    IND   
    4             135      110        16        28    IND   
    
                              Org_Airport Dest   
    0  Indianapolis International Airport  BWI  \
    1  Indianapolis International Airport  LAS   
    2  Indianapolis International Airport  MCO   
    3  Indianapolis International Airport  PHX   
    4  Indianapolis International Airport  TPA   
    
                                     Dest_Airport  Distance  TaxiIn  TaxiOut   
    0  Baltimore-Washington International Airport       515       3       10  \
    1              McCarran International Airport      1591       3        7   
    2               Orlando International Airport       828       6        8   
    3    Phoenix Sky Harbor International Airport      1489       7        8   
    4                 Tampa International Airport       838       4        9   
    
       Cancelled CancellationCode  Diverted  CarrierDelay  WeatherDelay  NASDelay   
    0          0                N         0             2             0         0  \
    1          0                N         0            10             0         0   
    2          0                N         0             8             0         0   
    3          0                N         0             3             0         0   
    4          0                N         0             0             0         0   
    
       SecurityDelay  LateAircraftDelay  
    0              0                 32  
    1              0                 47  
    2              0                 72  
    3              0                 12  
    4              0                 16  
    
**df.info()**

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 484551 entries, 0 to 484550
    Data columns (total 29 columns):
     #   Column             Non-Null Count   Dtype 
    ---  ------             --------------   ----- 
     0   DayOfWeek          484551 non-null  int64 
     1   Date               484551 non-null  object
     2   DepTime            484551 non-null  int64 
     3   ArrTime            484551 non-null  int64 
     4   CRSArrTime         484551 non-null  int64 
     5   UniqueCarrier      484551 non-null  object
     6   Airline            484551 non-null  object
     7   FlightNum          484551 non-null  int64 
     8   TailNum            484551 non-null  object
     9   ActualElapsedTime  484551 non-null  int64 
     10  CRSElapsedTime     484551 non-null  int64 
     11  AirTime            484551 non-null  int64 
     12  ArrDelay           484551 non-null  int64 
     13  DepDelay           484551 non-null  int64 
     14  Origin             484551 non-null  object
     15  Org_Airport        483374 non-null  object
     16  Dest               484551 non-null  object
     17  Dest_Airport       483072 non-null  object
     18  Distance           484551 non-null  int64 
     19  TaxiIn             484551 non-null  int64 
     20  TaxiOut            484551 non-null  int64 
     21  Cancelled          484551 non-null  int64 
     22  CancellationCode   484551 non-null  object
     23  Diverted           484551 non-null  int64 
     24  CarrierDelay       484551 non-null  int64 
     25  WeatherDelay       484551 non-null  int64 
     26  NASDelay           484551 non-null  int64 
     27  SecurityDelay      484551 non-null  int64 
     28  LateAircraftDelay  484551 non-null  int64 
    dtypes: int64(20), object(9)
    memory usage: 107.2+ MB
    None

**df.describe()**

               DayOfWeek        DepTime        ArrTime     CRSArrTime   
    count  484551.000000  484551.000000  484551.000000  484551.000000  \
    mean        3.991605    1564.477865    1617.784438    1652.129929   
    std         1.971466     452.235219     583.637660     466.096216   
    min         1.000000       1.000000       1.000000       1.000000   
    25%         2.000000    1234.000000    1327.000000    1339.000000   
    50%         4.000000    1620.000000    1737.000000    1723.000000   
    75%         6.000000    1928.000000    2049.000000    2025.000000   
    max         7.000000    2400.000000    2400.000000    2359.000000   
    
               FlightNum  ActualElapsedTime  CRSElapsedTime        AirTime   
    count  484551.000000      484551.000000   484551.000000  484551.000000  \
    mean     2139.207386         134.810422      131.400761     108.877134   
    std      1812.677071          74.070374       71.542531      70.113513   
    min         1.000000          15.000000      -21.000000       0.000000   
    25%       629.000000          80.000000       79.000000      57.000000   
    50%      1514.000000         116.000000      114.000000      90.000000   
    75%      3683.000000         168.000000      162.000000     139.000000   
    max      8403.000000         727.000000      602.000000     609.000000   
    
                ArrDelay       DepDelay       Distance         TaxiIn   
    count  484551.000000  484551.000000  484551.000000  484551.000000  \
    mean       60.907764      57.498086     752.142689       6.782413   
    std        56.975420      55.991012     571.631124       5.555816   
    min        15.000000       6.000000      31.000000       0.000000   
    25%        25.000000      23.000000     331.000000       4.000000   
    50%        42.000000      40.000000     599.000000       5.000000   
    75%        76.000000      72.000000     992.000000       8.000000   
    max      1707.000000    1710.000000    4502.000000     207.000000   
    
                 TaxiOut  Cancelled  Diverted   CarrierDelay   WeatherDelay   
    count  484551.000000   484551.0  484551.0  484551.000000  484551.000000  \
    mean       19.150876        0.0       0.0      17.419440       3.153284   
    std        15.309747        0.0       0.0      39.417893      19.503657   
    min         0.000000        0.0       0.0       0.000000       0.000000   
    25%        11.000000        0.0       0.0       0.000000       0.000000   
    50%        15.000000        0.0       0.0       2.000000       0.000000   
    75%        22.000000        0.0       0.0      19.000000       0.000000   
    max       383.000000        0.0       0.0    1707.000000    1148.000000   
    
                NASDelay  SecurityDelay  LateAircraftDelay  
    count  484551.000000  484551.000000      484551.000000  
    mean       13.599421       0.082033          26.653587  
    std        31.454655       1.884774          40.535994  
    min         0.000000       0.000000           0.000000  
    25%         0.000000       0.000000           0.000000  
    50%         1.000000       0.000000          13.000000  
    75%        13.000000       0.000000          36.000000  
    max      1357.000000     392.000000        1254.000000  

**df.columns**

    Index(['DayOfWeek', 'Date', 'DepTime', 'ArrTime', 'CRSArrTime',
       'UniqueCarrier', 'Airline', 'FlightNum', 'TailNum', 'ActualElapsedTime',
       'CRSElapsedTime', 'AirTime', 'ArrDelay', 'DepDelay', 'Origin',
       'Org_Airport', 'Dest', 'Dest_Airport', 'Distance', 'TaxiIn', 'TaxiOut',
       'Cancelled', 'CancellationCode', 'Diverted', 'CarrierDelay',
       'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay'],
      dtype='object')

## Data Cleaning

**df.isnull().sum()**

    DayOfWeek               0
    Date                    0
    DepTime                 0
    ArrTime                 0
    CRSArrTime              0
    UniqueCarrier           0
    Airline                 0
    FlightNum               0
    TailNum                 0
    ActualElapsedTime       0
    CRSElapsedTime          0
    AirTime                 0
    ArrDelay                0
    DepDelay                0
    Origin                  0
    Org_Airport          1177
    Dest                    0
    Dest_Airport         1479
    Distance                0
    TaxiIn                  0
    TaxiOut                 0
    Cancelled               0
    CancellationCode        0
    Diverted                0
    CarrierDelay            0
    WeatherDelay            0
    NASDelay                0
    SecurityDelay           0
    LateAircraftDelay       0
    dtype: int64

**df['Cancelled'].sum()**

    0

**df['Diverted'].sum()**

    0

**df['CancellationCode'].unique()**

    N

**Checking taxi times**

    df_taxi = pd.DataFrame({'TaxiIn': [df['TaxiIn'].min(), df['TaxiIn'].max(), df['TaxiIn'].mean()], 'TaxiOut': [df['TaxiOut'].min(), df['TaxiOut'].max(), df['TaxiOut'].mean()]})
    df_taxi.index = ['min', 'max', 'mean']
    print(df_taxi)

    print('amt taxiIn = 0:', df['TaxiIn'].value_counts()[0.0])  # 26
    print('amt taxiOut = 0:', df['TaxiOut'].value_counts()[0.0])  # 8

|         | TaxiIn     | TaxiOut    |
|---------|------------|------------|
| min     | 0.000000   | 0.000000   |
| max     | 207.000000 | 383.000000 |
| mean    | 6.782413   | 19.150876  |
| amt = 0 | 26         | 8          |

According to this, there are 34 (26 + 8) occurrences where the taxi time is 0.
TaxiIn-time defines period between wheels-on and gate arrival, TaxiOut-time defines period between gate departure and wheels-off as of [EUROCONTROLs definition from 2017](https://www.eurocontrol.int/sites/default/files/publication/files/airport-cdm-manual-2017.PDF).
Therefore, a taxi time from 0 should **not** be possible.

## Checking for buggy data

    for i in range(len(df)):

        """for each entry, checks if ArrDelay is equal to the sum of all other delays"""
        if df['ArrDelay'][i] != df['CarrierDelay'][i] + df['WeatherDelay'][i] + df['NASDelay'][i] + df['SecurityDelay'][i] + df['LateAircraftDelay'][i]:
            print('ArrDelay != Sum(otherDelays) AT: ', i)

        """for each entry, checks if ActualElapsedTime-(TaxiIn+TaxiOut) is equal to AirTime"""
        if df['ActualElapsedTime'][i] - (df['TaxiIn'][i] + df['TaxiOut'][i]) != df['AirTime'][i]:
            print('ActualElapsedTime-(TaxiIn+TaxiOut) != AirTime AT:', i)

    #/> Process finished with exit code 0

## Exploratory Data Analysis

### Analyze the distribution of flight delays

**Histogram of flight delays**

![](/pics/CG_histogram.png)

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

**Histogram of flight delays without extremes**

![](/pics/CG_histogram_removed_extremes.png)

    plt.hist(df['ArrDelay'], bins=50, edgecolor='k', range=[0, 500])
    plt.xlabel('Flight Delay (minutes)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Flight Delays - Removed Extremes')

    # resizing
    fig = plt.gcf()
    fig.set_size_inches(8, 6)

    plt.show()

**Delay Heatmap**

![](/pics/delay-heatmap.png)

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


### Explore relationships with categorical variables

**Delay by carrier**

![](/pics/delay-by-carrier.png)

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

**Delay per plane**

![](/pics/tailnum-by-mean-by-count.png)

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
    plt.text(df_tn['count'].mean() + df_tn['count'].std() + 5, 100, 'mean+std', color='green', weight='bold',rotation=90)
    plt.text(df_tn['count'].mean() - df_tn['count'].std() + 5, 100, 'mean-std', color='green', weight='bold',rotation=90)

    # top right corner text
    plt.text(250, 265, 'mean of mean: ' + str(round(df_tn['mean'].mean(), 2)), color='red')
    plt.text(250, 250, 'std of mean: ' + str(round(df_tn['mean'].std(), 2)), color='red')
    plt.text(250, 225, 'mean of count: ' + str(round(df_tn['count'].mean(), 2)), color='green')
    plt.text(250, 210, 'std of count: ' + str(round(df_tn['count'].std(), 2)), color='green')
    
    plt.title('TailNum by mean by count')

    plt.show()

**Delay per plane - outliers removed**

![](/pics/tailnum-by-mean-by-count-removed-extremes.png)

    # same as above, but count<11 removed for better visibility
    df_tn = df.groupby('TailNum').agg({'ArrDelay': ['mean', 'count']})
    df_tn.columns = ['mean', 'count']
    df_tn = df_tn[df_tn['count'] > 11]

    # ITS SCATTER TIME (again)
    sns.scatterplot(x=df_tn['count'], y=df_tn['mean'])

    # mean for mean and mean for count
    plt.axhline(df_tn['mean'].mean(), color='red', linestyle='--')
    plt.axvline(df_tn['count'].mean(), color='green', linestyle='--')
    plt.text(290, df_tn['mean'].mean()+5, 'mean of mean', color='red', weight='bold')
    plt.text(df_tn['count'].mean()+5, 100, 'mean of count', color='green', weight='bold', rotation=90)

    # average max and min delay
    plt.axhline(df_tn['mean'].mean()+df_tn['mean'].std(), color='red', linestyle='--')
    plt.axhline(df_tn['mean'].mean()-df_tn['mean'].std(), color='red', linestyle='--')
    plt.text(290, df_tn['mean'].mean()+df_tn['mean'].std()+5, 'mean+std', color='red', weight='bold')
    plt.text(290, df_tn['mean'].mean()-df_tn['mean'].std()+5, 'mean-std', color='red', weight='bold')

    # average max and min count
    plt.axvline(df_tn['count'].mean()+df_tn['count'].std(), color='green', linestyle='--')
    plt.axvline(df_tn['count'].mean()-df_tn['count'].std(), color='green', linestyle='--')
    plt.text(df_tn['count'].mean()+df_tn['count'].std()+5, 100, 'mean+std', color='green', weight='bold', rotation=90)
    plt.text(df_tn['count'].mean()-df_tn['count'].std()+5, 100, 'mean-std', color='green', weight='bold', rotation=90)

    # top right corner text
    plt.text(250, 130, 'mean of mean: ' + str(round(df_tn['mean'].mean(), 2)), color='red')
    plt.text(250, 125, 'std of mean: ' + str(round(df_tn['mean'].std(), 2)), color='red')
    plt.text(250, 115, 'mean of count: ' + str(round(df_tn['count'].mean(), 2)), color='green')
    plt.text(250, 110, 'std of count: ' + str(round(df_tn['count'].std(), 2)), color='green')

    plt.title('TailNum by mean by count (count>11)')

    plt.show()


### Analyze temporal patterns

**Daytime influence**

![](/pics/time-of-day-by-day-of-week.png)

    df_time = df.groupby(['DayOfWeek', 'DepTime']).agg({'ArrDelay': ['mean']})
    df_time.columns = ['mean']
    df_time = df_time.reindex(pd.MultiIndex.from_product([df_time.index.levels[0], range(100, 2500, 100)]))
    sns.heatmap(df_time['mean'].unstack(), cmap='coolwarm')
    xticks = [str(i)[:-2] + ':' + str(i)[-2:] for i in range(100, 2500, 100)]
    plt.xticks(range(24), xticks, rotation=45)
    yticks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    plt.yticks(range(7), yticks, rotation=45)
    plt.xlabel('Departure Time')
    plt.ylabel('Day of Week')
    plt.title('Mean of ArrDelay by Departure Time and Day of Week')
    fig = plt.gcf()
    fig.set_size_inches(12, 6)
    plt.show()

**Daytime influence - outliers removed**

![](/pics/time-of-day-by-day-of-week-extremes-only.png)

    df_tmp = df[(df['DepTime'] >= 2100) | (df['DepTime'] <= 600)]
    df_time = df_tmp.groupby(['DayOfWeek', 'DepTime']).agg({'ArrDelay': ['mean']})
    df_time.columns = ['mean']
    df_time = df_time.reindex(pd.MultiIndex.from_product([df_time.index.levels[0], [2100, 2200, 2300, 2400, 100, 200, 300, 400, 500, 600]]))
    sns.heatmap(df_time['mean'].unstack(), cmap='coolwarm')
    yticks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    plt.yticks(range(7), yticks, rotation=45)
    xticks = ['1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '21:00', '22:00', '23:00', '24:00']
    plt.xticks(range(10), xticks, rotation=45)
    plt.xlabel('Departure Time')
    plt.ylabel('Day of Week')
    plt.title('Mean of ArrDelay by Departure Time and Day of Week')
    fig = plt.gcf()
    fig.set_size_inches(12, 6)
    plt.show()


### Consider external factors

**Weather influence**

    print('day:', df['Date'].apply(lambda x: x[:2]).unique())
    print('month:', df['Date'].apply(lambda x: x[3:5]).unique())
    print('year:', df['Date'].apply(lambda x: x[6:]).unique())

    day ['03' '04' '05' '06' '07' '08' '09' '10' '11' '12' '13' '14' '15' '16' '17' '18' '19' '20' '21' '22' '23' '24' '25' '26' '27' '28' '29' '30' '31' '01' '02']
    month ['01' '02' '03' '04' '05' '06']
    year ['2022']

    -> Data is from January to June 2022

Sadly NOAA data is hard to access as a whole summary for the entire US is not available. I am too lazy to manually get each states/airports weather data.

