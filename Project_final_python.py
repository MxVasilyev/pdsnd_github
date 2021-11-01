"""This is a project work for udacity programm. Explore US Bike Share Data."""
import time

import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """Asks user to specify a city, month, and day to analyze.

    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to month filter
    (str) day - name of the day of week to filter by, or "all" to day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ""
    while city not in CITY_DATA:
        city = input("Please choose and type city from the list:"
                     " Chicago, New York City, Washington :\n").lower()
    # TO DO: get user input fore
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = ""
    while month not in months:
        month = input("Please choose and type month from the list:"
                      " all, january, february, ... , june :\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']
    day = ""
    while day not in days:
        day = input("Please choose and type day of the week from the list:"
                    " all, monday, tuesday, ... sunday :\n").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or
            "all" to apply no month filter
        (str) day - name of the day of week to filter by,
            or "all" to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df.rename(columns={'Unnamed: 0': 'num'}, inplace=True)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Start hour'] = df['Start Time'].dt.hour
    print("\nThe most common hour is ", df['Start hour'].mode()[0])
    # TO DO: display the most common month
    df['Start month'] = df['Start Time'].dt.month_name()
    print("The most common month is ", df['Start month'].mode()[0])
    # TO DO: display the most common day of week
    df['Start day'] = df['Start Time'].dt.weekday_name
    print("\nThe most common day is ", df['Start day'].mode()[0])
    # TO DO: display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nThe most common start station is ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("\nThe most common end station is ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination
    # of start station and end station trip
    df['Station_combination'] = ("\nStart station: "+df['Start Station'] +
                                 "\nEnd station: " + df['End Station'])
    print("\nMost common combination of "
          "stations:", df['Station_combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types:\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('\ncounts of gender'
          ':\n', df['Gender'].fillna('Unknown').value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    # df['year'] = df['Birth Year'].dt.year
    print('\n Earliest year: ', int(df['Birth Year'].min()), '\n '
          'Most recent: ', int(df['Birth Year'].max()), '\n '
          'Most common: ', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def see_raw_data(df):
    """Offering to check raw data."""
    x = 0
    while x+5 <= len(df):
        print(df.iloc[x:x+5, :8], '\n ', x, '-', x+5, ' records of ', len(df))
        show = input("\nDo you want to see want to see 5 lines of raw data?\n")
        if show.lower() == 'yes':
            x += 5
        else:
            break
    return


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_d = input('Do you want to see 5 lines of raw data?\n')
        if raw_d.lower() == 'yes':
            see_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
