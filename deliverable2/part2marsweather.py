# Module 11
# Part 2: Scrape and Analyze Mars Weather Data

# dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
import pandas as pd
import os

# an automated browser instance
browser = Browser('chrome')

# define url
url = "https://static.bc-edx.com/data/web/mars_facts/temperature.html"

# visit method of Browser object
browser.visit(url)

# automate browser
html = browser.html

# BeautifulSoup object used for parsing html
table_soup = soup(html, 'html.parser')

# define the html table to scrape
table = table_soup.find('table')

# list comprehension to create a list of table headers
headers = [th.text for th in table.find('tr').find_all('th')]

# dictionary comprehension
data = {header: [] for header in headers}

# a for loop that iterates through the rows of the table
# a list slicing operation removes the headers of the table
for row in table.find_all('tr')[1:]:

# a for loop that iterates through the cells of table
# a zip function aggregates the header and cells
    for header, cell in zip(headers, row.find_all('td')):
    
# append the data dictionary comprehension
        data[header].append(cell.text)
        
# DataFrame creation
df = pd.DataFrame(data)

# Print the DataFrame
print()
print('Mars Weather DataFrame')
print('------------------------------------------------------')
print(df)
print('------------------------------------------------------')
print()

# Print the data types
print()
print('Original Data Types')
print('------------------------------------------------------')
print(df.dtypes)
print('------------------------------------------------------')
print()

# changed the data types for analysis
df['terrestrial_date'] = pd.to_datetime(df['terrestrial_date'])

df['sol'] = pd.to_numeric(df['sol']).astype('Int64')

df['ls'] = pd.to_numeric(df['ls']).astype('Int64')

df['month'] = pd.to_numeric(df['month']).astype('Int64')

df['min_temp'] = pd.to_numeric(df['min_temp']).astype('float')

df['pressure'] = pd.to_numeric(df['pressure']).astype('float')

# print the df DataFrame with the new data types
print()
print('New Data Types')
print('------------------------------------------------------')
print(df.dtypes)
print('------------------------------------------------------')
print()

# How many months exist on Mars?
months = df.groupby('month').size()
print()
print('How many month exist on Mars?')
print('------------------------------------------------------')
print(months)
print('------------------------------------------------------')
print()

# how many Martian days worth of data are there?
sols = df['sol'].nunique()
print()
print('how many Martian days worth of data are there?')
print('------------------------------------------------------')
print(f"There are {sols} Martian days worth of data.")
print('------------------------------------------------------')
print()

# What is the average low temperature by month?
avg_low_temp = df.groupby('month')['min_temp'].mean()
print()
print('What is the average low temperature by month?')
print('------------------------------------------------------')
print(avg_low_temp)
print('------------------------------------------------------')
print()

# bar plot of the average tempature by month
avg_low_temp.plot(kind='bar')
plt.title('Average Low Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Temperature (C)')
plt.show()

#save the plot as png image in current directory
plt.savefig("/Users/grahammarsh/Documents/GitHub/module11-webscraping/deliverable2/avg_low_temp_by_month.png")

# sorted bar plot of the average temperature by month from lowest to highest
avg_low_temp.sort_values().plot(kind='bar')
plt.title('Sorted Average Low Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Temperature (C)')
plt.show()

#save the plot as png image in current directory
plt.savefig("/Users/grahammarsh/Documents/GitHub/module11-webscraping/deliverable2/sorted_avg_low_temp_by_month.png")

# average pressure by month
avg_pressure = df.groupby('month')['pressure'].mean()
print()
print('Average Pressure by Month')
print('------------------------------------------------------')
print(avg_pressure)
print('------------------------------------------------------')
print()

# sorted bar plot of pressure by month from lowest to highest
avg_pressure.sort_values().plot(kind='bar')
plt.title('Average Pressure by Month')
plt.xlabel('Month')
plt.ylabel('Pressure (Pa)')
plt.show()

#save the plot as png image in current directory
plt.savefig("/Users/grahammarsh/Documents/GitHub/module11-webscraping/deliverable2/avg_pressure_by_month.png")

# plot of the daily min temperature by elapsed sol
df.plot(x='sol', y='min_temp')
plt.title('Daily Min Temperature by Elapsed Sol')
plt.xlabel('Elapsed Sol')
plt.ylabel('Temperature (C)')
plt.show()

#save the plot as png image in current directory
plt.savefig("/Users/grahammarsh/Documents/GitHub/module11-webscraping/deliverable2/daily_min_temp_by_elapsed_sol.png")

# CSV file of df DataFrame to current directory
df.to_csv('mars_weather.csv', index=False)

# export df.datatypes, months, sols, avg. low temp by month and avg. pressure by month to a text file
with open('mars_weather_data.txt', 'w') as f:
    f.write('Data Types\n')
    f.write(str(df.dtypes))
    f.write('\n\nMonths\n')
    f.write(str(months))
    f.write('\n\nSols\n')
    f.write(str(sols))
    f.write('\n\nAverage Low Temperature by Month\n')
    f.write(str(avg_low_temp))
    f.write('\n\nAverage Pressure by Month\n')
    f.write(str(avg_pressure))

# browser quit
browser.quit()





