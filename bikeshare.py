import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities = ['Chicago','New York','Washington']
    months = ['January','Feburary','March','April','May','June','All']
    days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
    selection = ['Yes', 'No', 'Exit']
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWhich city\'s data do you want to take a look at? \"Chicago\", \"New York\" or \"Washington\"? \n')
        city = city.lower()
        if city.title() in cities:
            print('\nYou entered {}.'.format(city.title()))
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nDo you want to look at a specific month? You can pick data from January to June. If you need data for all months, just enter All. \n')
        month = month.lower()
        if month.title() in months:
            print('\nYou entered {}.'.format(month.title()))
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nDo you want to look at a specific day of week? If you need to look at all week, just enter All\n')
        day = day.lower()
        if day.title() in days_of_week:
            print('\nYou entered {}.'.format(day.title()))
            break
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
    df = pd.read_csv(city)

    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = months.index(month) + 1

        
        df = df[df['month'] == month]

    
    if day != 'all':
       
        df = df[df['day_of_week'] == day.title()]


    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Month'] = df['Start Time'].dt.month
    common_month = df['Month'].mode()[0]


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day
    common_day = df['day_of_week'].mode()[0]


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_Start = df['common_start'].mode()[0]
    print ('The most common start station is: ', common_Start)

    # TO DO: display most commonly used end station
    df['common_end'] = df['End Station']
    common_end = df['common_end'].mode()[0]
    print('The most common end station is: ', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    common_trip = df['common_start'] + ' to ' + df['common_end']
    print('The most common trip is: ', common_trip.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Trip Total Time'] = trip_start - trip_end
    # Adding total trip
    total_time =  df['Trip Total Time'].sum()
    print("The total amount of time for a trip is: " + str(total_time))

    # TO DO: display mean travel time
      mean_time = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
   
   
    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    if city != 'washington':

    # TO DO: Display earliest, most recent, and most common year of birth
     earliest_year = df.sort_values('Birth Year').iloc[0]
     common_year = df['Birth Year'].mode()[0]
     if city != 'washington':

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
#update