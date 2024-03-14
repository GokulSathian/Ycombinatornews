from scrap import *
import pandas as pd
import pymongo
from flask import Flask, make_response, jsonify,render_template
import time


#list created for storing urls and data
urls=[]     #   List to store URL
title_name=[]  #   List to store Title
Url_link=[]   
Upvotes_data=[]  #   List to store Upvotes for each news

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

    @app.route('/Topnews', methods=['POST', 'GET'])
    def topnews():
        table = df.to_html()
        return render_template('Topnews.html', table=table)

    if __name__ == '__main__':
        app.run()
    
    db.collection.remove({})

    time.sleep(24*60*60)

