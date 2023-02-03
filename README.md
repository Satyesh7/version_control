
### Date of Project
This project was completed on 22nd Jan,2023.

### Explore US Bikeshare Data
In this project, I put my python,numpy and pandas skills to use by exploring and creating different statistics and insights
about the Bikeshare Data.

### Description
This project exlpores the bikeshare data of three major cities-Chicago,Washington and New York City and presents various 
statistics and insights about the rental activites of the customers.
A glimpse of the questions answered are below:

* Which is the most popular hour of travel?
* Which is the most popular day for travel?
* Which is the most popular week for travel?
* The number of people who are subscribers and those who are one time customer
* Which is the most popular Start Station?
* Which is the most popular End Station?



### Files used
`bikeshare.py`
`chicago.csv`
`washington.csv`
`new_york_city.csv`

### Sample Usage
```
Hello! Let's explore some US bikeshare data!
Enter the Name of the City you want the data for-Chicago or New York City or Washington:washington
Enter the Name of the Month['January','february','march','april','may','june'] you want the data for[enter 'all' for all months]:all
Enter the Name of the Day you want the data for[enter 'all' for all days]:all
----------------------------------------

Calculating The Most Frequent Times of Travel...

The most popular month of travel is:June
The most popular day of travel is:Wednesday
The most common start hour of travel is:8

This took 0.05032920837402344 seconds.
----------------------------------------

Calculating The Most Popular Stations and Trip...

The most Popular Start Station is:Columbus Circle / Union Station, with a count of 5656
The most Popular End Station is:Columbus Circle / Union Station, with a count of 6048
The most Popular combination of Start and End station trip is:Jefferson Dr & 14th St SW to Jefferson Dr & 14th St SW, with a count of 673

This took 0.7213177680969238 seconds.
----------------------------------------

Calculating Trip Duration...

Total travel time is: 371183985.484 seconds OR 103106.0 hour(s), 39.0 minute(s) and 45.48400002717972 second(s)
Mean travel time is: 1237.2799516133334 seconds 

This took 0.0050771236419677734 seconds.
----------------------------------------

Calculating User Stats...

Here are the different types of Users:
 Subscriber    220786
Customer       79214
Name: User Type, dtype: int64

Sorry, there is no gender data for Washington

Sorry, there is no birth year data for Washington

This took 0.03942728042602539 seconds.
----------------------------------------

```

