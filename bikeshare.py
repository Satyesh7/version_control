#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'C:/Users/SATYESH/Downloads/All_Project_files/chicago.csv',
              'new york city': 'C:/Users/SATYESH/Downloads/All_Project_files/new_york_city.csv',
              'washington': 'C:/Users/SATYESH/Downloads/All_Project_files/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city=input("Enter the Name of the City you want the data for-Chicago or New York City or Washington:")
            if city.lower()=='chicago' or city.lower()=='new york city' or city.lower()=='washington':
                break
            else:
                print("Sorry, That is not the intended input, Please enter the name of any one city from the above 3 options")
        except:
            print("That is not a valid input. Please try again!")
           

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            months=['january','february','march','april','may','june','all']
            month=input("Enter the Name of the Month['January','february','march','april','may','june'] you want the data for[enter 'all' for all months]:")
            if month.lower() in months:
                break
            else:
                print("Sorry, That is not the intended input, Please enter the name of any valid Month")
        except:
            print("That is not a valid input. Please try again!")
           

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
            day=input("Enter the Name of the Day you want the data for[enter 'all' for all days]:")
            if day.lower() in days:
                break
            else:
                print("Sorry, That is not the intended input, Please enter the name of any valid Day")
        except:
            print("That is not a valid input. Please try again!")


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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
    
    if month!='all':
        months=['january','february','march','april','may','june','july','august','september','october','november','december']
        month=months.index(month)+1
        df=df[df['month']==month]
     
    if day!='all':
        df=df[df['day_of_week']==day.title()]
        
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months=['january','february','march','april','may','june','july','august','september','october','november','december']
    popular_month=months[df['month'].mode()[0]-1]
    print("The most popular month of travel is:{}".format(popular_month.title()))


    # TO DO: display the most common day of week
    popular_week=df['day_of_week'].mode()[0]
    print("The most popular day of travel is:{}".format(popular_week))


    # TO DO: display the most common start hour
    popular_hour=df['hour'].mode()[0]
    print("The most common start hour of travel is:{}".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('The most Popular Start Station is:{}, with a count of {}'.format(popular_start_station,df['Start Station'].value_counts()[0]))


    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('The most Popular End Station is:{}, with a count of {}'.format(popular_end_station,df['End Station'].value_counts()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    popular_combination_trip=df['Start Station'] + " to " + df['End Station']
    print('The most Popular combination of Start and End station trip is:{}, with a count of {}'.format(popular_combination_trip.mode()[0],popular_combination_trip.value_counts()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time=df['Trip Duration'].sum()
    hours=Total_travel_time//3600
    minutes=(Total_travel_time - hours*3600)//60
    seconds=Total_travel_time-((hours*3600) + (minutes*60))
    print("Total travel time is: {} seconds OR {} hour(s), {} minute(s) and {} second(s)".format(Total_travel_time,hours,minutes,seconds))
   
  

    # TO DO: display mean travel time
    Mean_travel_time=df['Trip Duration'].mean()
    print("Mean travel time is: {} seconds ".format(Mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Here are the different types of Users:\n",df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if city.lower()=='washington':
        print("\nSorry, there is no gender data for Washington")
    else:
        print("\nHere is the count of Gender:\n",df['Gender'].value_counts())
    
        

    # TO DO: Display earliest, most recent, and most common year of birth
    if city.lower()=='washington':
        print("\nSorry, there is no birth year data for Washington")
    else:
        year=df['Birth Year']
        print("The earliest year of  birth is:{}".format(year.min()))
        print("The most recent year of  birth is:{}".format(year.max()))
        print("The most common year of  birth is:{}".format(year.mode()[0]))
        
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Display a prompt asking if the user wants to see the raw data for 5 rows"""
    choice=input("\nWould you like to see the raw data for 5 rows? [Enter 'yes' or 'no']:")
    if choice.lower()=='yes':
        count=0
        while True:
            print(df.iloc[count:count+5])
            count+=5
            ask=input("Would you like to see the next 5 rows of raw data? [Enter 'yes' or 'no']:")
            if ask.lower()!='yes':
                break
                
            


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:




