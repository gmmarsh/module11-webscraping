#Module 11 Part 1 Mars News

#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
import json

#define browser
browser = Browser('chrome')

#define url
url = "https://static.bc-edx.com/data/web/mars_news/index.html"

#tell the automated browser what url to visit
browser.visit(url)

#retrieve the HTML and assign it to a variable
html = browser.html

#define the Beautiful Soup object
news_soup = soup(html, 'html.parser')

#use the find_all method to find the news titles
news_title = news_soup.find_all('div', class_='content_title')

#use the find_all method to find the new article previews
news_preview = news_soup.find_all('div', class_='article_teaser_body')

#define an empty list to store the dictionaries
news_list = []

#a for loop equal with a range equal to the length of the new_title list
for i in range(len(news_title)):
    news_dict = {}
    news_dict['title'] = news_title[i].text
    news_dict['preview'] = news_preview[i].text
    news_list.append(news_dict)
    
#export news_list to a json file called 'news_summary' using the open function in write mode
#the json.dump function writes the new_list into a json_file
with open('news_summary.json', 'w') as json_file:
    json.dump(news_list, json_file)

#quit the browser
browser.quit()

