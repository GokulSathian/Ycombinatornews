# Description: This file is used to create a csv file with the headers Title, URL and Upvotes. The function write_csv takes in three parameters -
from csv import writer

def create_csv():
    with open('news.csv','w',encoding ='utf8',newline='') as f:
        cursor =writer(f)
        header=['Title','URL','Upvotes']
        cursor.writerow(header)  