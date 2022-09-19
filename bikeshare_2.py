import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_month():
    """Returns the user's chosen month filter."""
    while True:
        month = input('Which month - January, February, March, April, May, or June?').lower()
        if month.title() in ['January', 'February', 'March', 'April', 'May', 'June']:
            return month
        else:
            print('invalid input!!')
def get_day():
    """Returns the user's chosen day filter."""
    while True:
        day = input('Which day?').lower()
        if day.title() in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            return day
        else:
            print('invalid input!!')
    

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['Chicago', 'New York City','Washington']
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?').lower()
        if city.title() in cities:
            break
        else:
            print('invalid input!!')

    while True:
        choice = input('Would you like to filter the data by month, day, both or not at all?(type none if you don\'t want filters)')
        if choice.lower() in ['month','day','none', 'both']:
            break
        else: 
            print('invalid input!!')
        
    # get user input for month (all, january, february, ... , june)
    day = 'All'
    month = 'All'
    if choice.lower() == 'month':
        month = get_month()

    elif choice.lower() == 'day':
        day = get_day()

    elif choice.lower()=='both':
        month = get_month()
        day = get_day()
    
        
    
    


    # get user input for day of week (all, monday, tuesday, ... sunday)
    

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if month != 'All':
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
        
    print('FILTERS APPLIED: CITY: {}, DAY: {}, MONTH: {}'.format(city,day,month))
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('Most common month is : {}'.format(months[df['month'].mode()[0]-1].title()))


    # display the most common day of week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('Most common day is : {}'.format(df['day_of_week'].mode()[0]))


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most common start  hour is : {}'.format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station is {}'.format(df['Start Station'].mode()[0]))


    # display most commonly used end station
    print('Most commonly used end station is {}'.format(df['End Station'].mode()[0]))


    # display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip {}'.format((df['Start Station'] +' to '+df['End Station']).mode()[0]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time: {}'.format(df['Trip Duration'].sum()))


    # display mean travel time
    print('Mean travel time: {}'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    types = df['User Type'].value_counts()
    keys = types.keys()
    for typ in keys:
        print('{} has count of {}'.format(typ,types[typ]))
    


    # Display counts of gender
    if 'Gender' in df.columns:
        typess = df['Gender'].value_counts()
        keyss = typess.keys()
        for typ in keyss:
            print('{} has count of {}'.format(typ,typess[typ]))
    


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Most recent year of birth: {}'.format(int(df['Birth Year'].max())))
        print('erliest year of birth: {}'.format(int(df['Birth Year'].min())))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw(df):
    ans = input('\nWould you like to view individual trip  data? \'yes\' or \'no\' \n')
    if ans == 'yes':
        start = 0
        for i,row in df.iterrows():
            print('{}'.format(row))
            if start ==4:
                ans = input('\nWould you like to view more individual trip  data? \'yes\' or \'no\' \n')
                if ans == 'yes':
                    start = 0
                    continue
                elif ans== 'no':
                    return
                    
            start+=1
            print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
