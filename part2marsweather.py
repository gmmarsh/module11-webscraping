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




