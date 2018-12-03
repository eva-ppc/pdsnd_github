import time
import pandas as pd
import numpy as np


CITY_DATA = { "chicago": "chicago.csv",
              "new york city": "new_york_city.csv",
              "washington": "washington.csv" }

months = ["january", "february",
            "march", "april",
            "may", "june", "all"]

days = ["monday", "tuesday",
        "wednesday", "thursday", "friday",
        "saturday", "sunday", "all"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let\"s explore some US bikeshare data!")
# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input (str("What is the city you want to analyze? Choose from New York City, Chicago, or Washington?")).lower()
        if city in ("washington", "chicago", "new york city"):
            break
        else:
            print("Please choose one of the city options provided")

# get user input for month (all, january, february, ... , june)

    while True:
        month = input(str("Would you like to look at the data for any specific month?\nPlease choose from: January, February, March, April, May, June, or all?\n ")).lower()
        if month in months:
            break
        else:
            print ("Please choose from: January, February, March, April, May, June, or all!\n")



    while True:
        day = input(str("If you would like to analize a day of the week, please specify the day now:\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all of them?\n" )).lower()
        if day in days:
            break
        else:
            print ("Please try again: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all of them!\n")
    # Display what is the filter applied
    print("-"*40)
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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour

    # filter by month if applicable
    if month != "all":
        # use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # display the most common month
    most_common_month = df["month"].mode()[0]
    print("The most common month is :", most_common_month)


    # display the most common day of week
    most_common_day_of_week = df["day_of_week"].mode()[0]
    print("The most common day of week is :", most_common_day_of_week)

    # display the most common start hour
    most_common_start_hour = df["hour"].mode()[0]
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df["Start Station"].mode()[0]
    print("The most commonly used start station is:", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]
    print("The most commonly used end station :", most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + ' & ' + df['End Station']

    most_common_start_end_station = df['Start End'].value_counts().idxmax()

    print("The most commonly used start station and end station :",most_common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    total_travel = df["Trip Duration"].sum()
    print("Total travel time is:",total_travel)

    # display mean travel time
    mean_travel = df["Trip Duration"].mean()
    print("Average travel time is:",mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    user_counts = df["User Type"].value_counts()
    print(user_counts)

    # Display counts of gender
    if "Gender" in df.columns:
        gender_counts = df["Gender"].value_counts()
        print(gender_counts)
    else:
        print("Oops!  That was no valid parametr for the city you've picked. Select Another city and try again...")

    # Display earliest, most recent, and most common year of birth
    # Most common birth year
    if "Birth Year" in df.columns:
        birth_year = df["Birth Year"]
        most_common_birth_year = birth_year.mode()[0]
        print("The most common birth year is", most_common_birth_year)
    else:
        print("Oops!  That was no valid parametr for the city you've picked. Select Another city and try again...")
    # Most recent birth Year
    if "Birth Year" in df.columns:
        most_recent_birth = birth_year.max()
        print("The most recent birth year:", most_recent_birth)
    else:
        print("Oops!  That was no valid parametr for the city you've picked. Select Another city and try again...")
    # Least recent birth Year
    if "Birth Year" in df.columns:
        least_recent_birth_year = birth_year.min()
        print("The most earliest birth year:", least_recent_birth_year)
    else:
        print("Oops!  That was no valid parametr for the city you've picked. Select Another city and try again...")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

# Ask user if raw data should be presented
        x=5
        while True:
            raw_data=input("\nWould you like to see raw data? Enter yes or no.\n").lower()
            print(df.head(x))
            x=x+5
            if (raw_data == 'no'):
                restart = input("\nWould you like to restart? Enter yes or no.\n").lower()
                if restart == "yes":
                    break
                else:
                    print("Thanks for your attention!")
                    exit()




if __name__ == "__main__":
	main()

print(main())
