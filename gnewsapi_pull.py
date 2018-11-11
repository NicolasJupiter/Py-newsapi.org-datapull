""""

Name: Google News API (newsapi.org) pull
Description: This program uses newsapi.org in order to pull and output the headlines/urls from google news
Author: mk-wintr

Date: 2018/11/10

""""

import datetime
import os.path
import requests

# save_path defines the location api information will be output
save_path = 'C:/Users/ZZZZ/'

# configurations to set the file name to a headline file with the date
this_date = datetime.datetime.now()
date_str_year = this_date.strftime("%Y")
date_str_month = this_date.strftime("%m")
date_str_day = this_date.strftime("%d")
date_str = date_str_year + "-" + date_str_month + "-" + date_str_day
filename = 'HL-' + date_str + '.txt'
complete_name = os.path.join(save_path, filename)

# goes into url specified from newsapi.org - creating a username is crucial where you can add your apiKey
url = ('https://newsapi.org/v2/top-headlines?sources=google-news&'
       'apiKey=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
response = requests.get(url)

# print to check that the url is properly accessed
print(response.status_code)

# store the response's json object and create variable to access 'articles'
json_object = response.json()
articles_list = json_object['articles']

# prepare file to append new information
i = 0
f = open(complete_name,'a')

# writes the top 10 article dates, titles and urls with the ";~;" as delimiters
while i < len(articles_list):
	f.write(articles_list[i]['publishedAt'] + ";~;" + 
		articles_list[i]['title'] + ";~;" + 
		articles_list[i]['url'] + ";~;" + "\n")
	i+= 1
	
f.close()