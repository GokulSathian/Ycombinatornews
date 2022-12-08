from create_csv import *
from top_three import *
from bs4 import BeautifulSoup
import requests
from csv import writer


def scrap(urls):
    scraped_list=[]
    data ={'Title':[],'URL':[],'Upvotes':[]}
    create_csv()
    for j in range(0,4):
        #webpage=yc_webpage()
        article_tag=[]
        article_text=[]
        article_link=[]
        webpage_soup = requests.get(urls[j])
        webpage =webpage_soup.text
        soup= BeautifulSoup(webpage,"html.parser")
        article_title = soup.find_all('span',{"class":"titleline"})
        for i in article_title:
            tag= i.find('a')
            link =tag.get("href")
            article_link.append(link)
            text = tag.getText()
            article_text.append(text)
        index_largest,article_upvotes =top_three(soup)    
        f  = open('news.csv','a',encoding ='utf8',newline='')
        cursor =writer(f)
        for i in index_largest:
            scraped_list =[article_text[i],article_link[i],article_upvotes[i]]
            data['Title'].append(article_text[i])
            data['URL'].append(article_link[i])
            data['Upvotes'].append(article_upvotes[i])
            cursor.writerow(scraped_list)
            print(scraped_list)
        f.close()
    return data