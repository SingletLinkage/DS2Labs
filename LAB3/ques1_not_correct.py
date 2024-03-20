'''
Question 1:

The exponential distribution is ideal to model waiting times (e.g, time to failure of sensors in a system, flood occurrence, etc.). We will be using the exponential distribution to model time to the arrival of the next confirmed case of Covid-19 in India. Based upon data of confirmed cases from the source https://www.covid19india.org/, between 17th April 2020 and 23rd April 2020, there were on average 1373 confirmed cases per day, i.e. on average around 57 cases per hour. 

    (a) Write a program to plot the probability density function of the wait time for the next Covid-19 confirmed case, where the X axis is the wait time in hours and Y axis is the probability density.
    (b) Write a program to find the probability of the wait time for the next Covid-19 confirmed case to be less than or equal to 1 minute (Hint: convert minutes into hours before using it in the cumulative density function).
    (c) Write a program to find the probability of the wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes.
    (d) Now, write a program to find the probability of the wait time for the next Covid-19 confirmed case to be more than 2 minutes.
    (e) Suppose the average number of cases per hour doubled. Write a program to find the probability of wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes.
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

dates = ['2020-04-17', '2020-04-18', '2020-04-19', '2020-04-20', '2020-04-21', '2020-04-22', '2020-04-23']

# Load the data
url = 'https://data.covid19india.org/v4/min/timeseries.min.json'

f = open('timeseries.json')
r = json.load(f)
f.close()

# Extract the data
data : dict = {}

for key in r.keys():
    data[key] = {}
    for date in dates:
        try:
            data[key][date] = r[key]['dates'].get(date, {}).get('delta', {}).get('confirmed', 0)

        except KeyError as e:
            print(f"Error: {e} at {key} {date}")

database = pd.DataFrame(data).T
print(database)


# part 1

# get total cases per day inclusive of all states
print(database.sum().mean())