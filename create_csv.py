from csv import writer

def create_csv():
    with open('news.csv','w',encoding ='utf8',newline='') as f:
        cursor =writer(f)
        header=['Title','URL','Upvotes']
        cursor.writerow(header)  