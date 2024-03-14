# Description: This file contains the function to scrape the data from the website and write it to a csv file.
from create_csv import *
from top_three import *
from bs4 import BeautifulSoup
import requests
from csv import writer


def scrap(urls):
    scraped_list=[]
    data ={'Title':[],'URL':[],'Upvotes':[]}
    create_csv()

    #For loop to scrape data from 4 pages of the website.
    for j in range(0,4):
        #webpage=yc_webpage()
        article_tag=[]
        article_text=[]
        article_link=[]

        #Requesting the webpage and creating a soup object with it.
        webpage_soup = requests.get(urls[j])
        webpage =webpage_soup.text
        soup= BeautifulSoup(webpage,"html.parser")
        article_title = soup.find_all('span',{"class":"titleline"})

        # Loop to get the article title and link.
        for i in article_title:
            tag= i.find('a')
            link =tag.get("href")
            article_link.append(link)
            text = tag.getText()
            article_text.append(text)
        index_largest,article_upvotes =top_three(soup)    

        f  = open('news.csv','a',encoding ='utf8',newline='')
        # cursor to write the data to the csv file. calling the writer function from file create_csv.
        cursor =writer(f)

        #Loop to write the data to the csv file.
        for i in index_largest:
            scraped_list =[article_text[i],article_link[i],article_upvotes[i]]
            data['Title'].append(article_text[i])
            data['URL'].append(article_link[i])
            data['Upvotes'].append(article_upvotes[i])
            cursor.writerow(scraped_list)
            print(scraped_list)
        f.close()
    return data