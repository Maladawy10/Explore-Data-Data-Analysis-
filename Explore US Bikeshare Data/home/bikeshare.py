import time
import pandas as pd
import numpy as np
import datetime
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    global m
    m=False
    global d
    d=False
    global city 
    global month
    global day
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input('Choose your city (chicago, new york city, washington): ')
        if (city!='chicago' and city!='new york city' and city!='washington'):
            print('Enter string value from the choices provided.')
            continue
        choice = input('Choose filter by month or day or both or not at all (month, day, both, all): ')
        if (choice!='month' and choice!='day' and choice!='both' and choice!='all'):
            print('Enter string value from the choices provided.')
            continue
        if (choice == 'month'):
            month = input('Choose your month (january, february, march, april, may, june, july, august, september, october, november, december): ')
            if (month!='january' and month!='february' and month!='march' and month!='april'and month!='may'and month!='june'and month!='july'and                         month!='august'and month!='september' and month!='october' and month!='november' and month!='december'):
                print('Enter string value from the choices provided.')
                continue
            m=True
        elif (choice == 'day'):
            day = input('Choose your day (saturday, sunday, monday, tuesday, wednesday, thursday, friday): ')
            if (day!='saturday' and day!='sunday' and day!='monday' and day!='tuesday'and day!='wednesday'and day!='thursday'and day!='friday'):
                print('Enter string value from the choices provided.')
                continue
            d=True
        elif (choice == 'both'):
            month = input('Choose your month (january, february, march, april, may, june, july, august, september, october, november, december): ')
            if (month!='january' and month!='february' and month!='march' and month!='april'and month!='may'and month!='june'and month!='july'and                          month!='august'and month!='september' and month!='october' and month!='november' and month!='december'):
                    print('Enter string value from the choices provided.')
                    continue
            day = input('Choose your day (saturday, sunday, monday, tuesday, wednesday, thursday, friday): ')
            if (day!='saturday' and day!='sunday' and day!='monday' and day!='tuesday'and day!='wednesday'and day!='thursday'and day!='friday'):
                print('Enter string value from the choices provided.')
                continue
            m=True
            d=True
        elif (choice == 'all'):
            day='all'
            month ='all'
        if (not m):
            month ='all'
        if (not d):
            day='all'
        break

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    filterdata()
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    datetime_object = datetime.datetime.strptime(str(popular_month), "%m")
    full_month_name = datetime_object.strftime("%B")
    if(not m):
        print('the most common month: ',full_month_name)
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    if(not d):
        print('the most common day of week: ',popular_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('the most common start hour: ',popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    filterdata()
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_st_station = df['Start Station'].mode()[0]
    print('most commonly used start station: ',popular_st_station)
    # TO DO: display most commonly used end station
    popular_en_station = df['End Station'].mode()[0]
    print('most commonly used end station: ',popular_en_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_sten_station =(df['Start Station'] + ' , ' + df['End Station']).mode()[0]
    print('most frequent combination of start station and end station trip: ',popular_sten_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    filterdata()
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['diff']=  df['End Time'] - df['Start Time']
    # TO DO: display total travel time
    print('total travel time: ',df['diff'].sum())
    # TO DO: display mean travel time
    print('Average travel time: {} in minutes: {}'.format(df['diff'].mean(),(df['diff'].sum()/df['diff'].count())/60000000000))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    filterdata()
    start_time = time.time()

    # TO DO: Display counts of user types
    print('No. of each user type:\n----------------------\n',df['User Type'].value_counts())
    # TO DO: Display counts of gender
    if(city!='washington'):
        print('No. of each gender:\n----------------------\n',df['Gender'].value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        ey=df.sort_values('Birth Year').iloc[0]
        ry=df.sort_values('Birth Year').iloc[df['Birth Year'].count()-1]
        print('\nThe earliest year of birth: {}, The most recent year of birth: {}, The most common year of birth: {}.'.format(int(ey['Birth Year']),int(ry['Birth Year']),int(df['Birth Year'].mode()[0])))
    else:
        print('\nThere is not available data about gender and year of birth in this state.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
#determine data filtered by what
def filterdata():
    if(m and d):
        print('Data filtered by: both (month: {}, day: {})\n'.format(month,day))
    elif(m):
        print('Data filtered by: month--> {}\n'.format(month))
    elif(d):
        print('Data filtered by: day--> {}\n'.format(day))
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        #printing data from data frame 
        i=0
        while True:
            show_date=input('\nWould you like to show data? Enter yes or no.\n')
            if show_date.lower() == 'yes':
                print(df.iloc[i:i+5])
                i+=5
                continue
            break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
