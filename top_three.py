# Description: This file contains the function to get the top three upvoted articles from the page.
def top_three(x):
    article_upvotes=[]
    article_upvote_bckup=[]
    indexes=[]
    count=0
    article_upvotes = [int(k.getText().split()[0]) for k in x.find_all('span',{"class":"score"})]
    article_upvote_bckup = [int(k.getText().split()[0]) for k in x.find_all('span',{"class":"score"})]
    while count<3:
        largest_number =max(article_upvotes)
        indexes.append(article_upvotes.index(largest_number))
        article_upvotes[article_upvotes.index(largest_number)] =0
        count+=1
    return indexes,article_upvote_bckup