# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:47:56 2022

@author: r387515 - Georges Da Fonte
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore US bikeshare data!')
    
    cities = ('chicago', 'new york city', 'washington')
    months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
    days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("\nSelect the city name you want to analyze (chicago, new york city, washington):\n ").lower()
    while city not in cities:
        print("choose a valid name please")
        city = input("\nSelect the city name to analyze (chicago, new york city, washington):\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nSelect the month to filter by or all (january, february, march, april, may, june, all):\n").lower()
    while month not in months:
        print("choose a valid name please")
        month = input("\nSelect the month to filter or all (january, february, march, april, may, june, all):\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nSelect the day of week to filter by or all (monday, tuesday, wednesday, thursday, friday, saturday, sunday, all):\n").lower()
    while day not in days:
        print("choose a valid name please")
        day = input("\nSelect the day of week to filter by or all (monday, tuesday, wednesday, thursday, friday, saturday, sunday, all):\n").lower()

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

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
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month : \n", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("Most common day of week : \n", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("Most common start hour : \n", df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station : \n", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most commonly used end station : \n", df['End Station'].mode()[0])

   # TO DO: display most frequent combination of start station and end station trip
    print("Most frequent combination of start station and end station trip: \n", df.groupby(['Start Station','End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time : \n", df["Trip Duration"].sum())
    # TO DO: display mean travel time
    print("Mean travel time : \n", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays bikeshare users statistics."""

    print('\nCalculating User Stats \n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types :")
    userTypes = df['User Type'].value_counts()
    for userType in userTypes.index:
        print(userType, ":", userTypes[userType])

    # TO DO: Display counts of gender
    try:
        print("Counts of gender :")
        genderTypes = df['Gender'].value_counts()
        for genderType in genderTypes.index:
            print(genderType, ":", genderTypes[genderType])
    except:
        print("No Gender Data")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("Earliest birth year :\n",df["Birth Year"].min())
        print("Most recent birth year :\n", df["Birth Year"].max())
        print("Most common birth year :\n", df["Birth Year"].mode()[0])
    except:
        print("No Birth Year Data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def row_data(df):
    """ Based on Udacity review feedback 
    creation of new function called display_data to show the 5 rows of data. Use of start_loc variable & df.iloc function 
    -used loc function as index reference as iloc function was returning same 5 rows
  
    """
    display_data = input("Do you want to see the first 5 rows of data?\n(Yes or No): ") 
    start_loc = 0
    #start_iloc = 0
    keep_asking = True
    while (keep_asking):
        print(df.iloc[start_loc:start_loc + 5])
        #print(df.iloc[start_iloc:start_iloc + 5])
        start_loc =+ 5
        #start_iloc =+ 5
        display_data = input("Do you want to see the next 5 rows of data?\n").lower()
        if display_data == "no": 
            keep_asking = False
        
            print('-'*40)  
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        selection = input("Do you want to see time stats of {} \n(yes/No) : ".format(city)).lower()
        while selection not in ("yes","no"):
            print("Enter a Valid Input")
            selection = input("Do you want to see time stats of {} \n(Yes/No) : ".format(city)).lower()
        if selection == 'yes': time_stats(df)
        selection = input("Do you want to see station stats of {}\n(Yes/No) : ".format(city)).lower()
        while selection not in ("yes","no"):
            print("Enter a Valid Input")
            selection = input("Do you want to see station stats of {} \n(Yes/No) : ".format(city)).lower()
        if selection == 'yes': station_stats(df)
        selection = input("Do you want to see trip duration of {} \n(Yes/No) : ".format(city)).lower()
        while selection not in ("yes","no"):
            print("Enter a Valid Input")
            selection = input("Do you want to see trip duration of {} \n(Yes/No) : ".format(city)).lower()
        if selection == 'yes': trip_duration_stats(df)
        selection = input("Do you want to see user stats of {} \n(Yes/No) : ".format(city)).lower()
        while selection not in ("yes","no"):
            print("Enter a Valid Input")
            selection = input("Do you want to see user stats of {} \n(yes/No) : ".format(city)).lower()
        if selection == 'yes': user_stats(df)
        while selection not in ("yes","no"):
           print("Enter a Valid Input")
           selection = input("Do you want 10 lines of raw data? {} \n(yes/No) : ".format(city)).lower()
        if selection == 'yes': row_data(df)
        
        restart = input("\nWould you like to restart this US bikeshare data exploration? \n(Yes/No) ")
        if restart.lower() != 'yes':
            break
    
if __name__ == "__main__":
    main()