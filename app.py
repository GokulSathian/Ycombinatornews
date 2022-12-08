from scrap import *
import pandas as pd
import pymongo
from flask import Flask, make_response, jsonify,render_template
import time


#list created for storing urls and data
urls=[]
title_name=[]
Url_link=[]
Upvotes_data=[]

#Connectint to MongoDB
client = pymongo.MongoClient(host="localhost",port=27017)
# db=client.test
db = client["news_db"]
collection = db["top_news"]

#Storing URL
for var in range(1,5):
    url = ["https://news.ycombinator.com/news?p=%i"%(var)]
    urls.append(url[0])

#Storing to MongoDB
def load_data(dataset):
    for (row,rs) in dataset.iterrows():
        print(row,rs)
        Title = rs[0]
        URL = rs[1]
        Upvotes = rs[2]
        d = {'Title':Title,'URL':URL,'Upvotes':Upvotes}       
        collection.insert_one(d)       
    print("Done")

# dataset = scrap(urls)
# df = pd.DataFrame(dataset)
# load_data(df)

#Initializing cursor to fetch data from MongoDB
x=collection.find()

for j in x:
    title_name.append(j["Title"])
    Url_link.append(j["URL"])
    Upvotes_data.append(j["Upvotes"])
    
while True:
    #Calling scraping function
    dataset = scrap(urls)

    #converting to dataframe 
    df = pd.DataFrame(dataset)
    #calling load_data
    load_data(df)

    app = Flask(__name__)

    @app.route('/')
    def show_home():
        return render_template("index.html")

    @app.route('/Topnews')
    def show_home():
        return render_template("Topnews.html",titles = title_name,url = Url_link,votes = Upvotes_data)

    @app.route('/chart')
    def google_chart():
        return render_template("Googlechart.html",x=title_name[0],y=title_name[1],z=title_name[2],x1=Upvotes_data[0],y1=Upvotes_data[1],z1=Upvotes_data[2])


    if __name__ == '__main__':
        app.run()
    
    db.collection.remove({})

    time.sleep(24*60*60)

