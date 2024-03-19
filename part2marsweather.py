# Module 11
# Part 2: Scrape and Analyze Mars Weather Data

# dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
import pandas as pd

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

# Print the data types
print()
print('Original Data Types')
print('------------------------------------------------------')
print(df.dtypes)

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

# How many months exist on Mars?
months = df.groupby('month').size()
print()
print('How many month exist on Mars?')
print()
print(months)

# how many Martian days worth of data are there?
sols = df['sol'].nunique()
print()
print('how many Martian days worth of data are there?')
print()
print(f"There are {sols} Martian days worth of data.")
print()

# What is the average low temperature by month?
avg_low_temp = df.groupby('month')['min_temp'].mean()
print('What is the average low temperature by month?')
print()
print(avg_low_temp)
print()









