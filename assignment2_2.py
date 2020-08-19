from itertools import islice
import collections
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
def readfile(files):
    print("hi")
    temp=files.read().replace('\n',' ')
    return temp;
def wordCount(content):
    words=content.split()
    return len(words);
def topTenWords(content):
    l = content.split()
    d={}
    for i in l:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)
    sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for i in range(10):
        print(sort_orders[i])
def topTenKeyWords(contents, stopWords):
    count = 0
    keywords = []
    for word in contents.split():
        if word not in stopWords:
            keywords.append(word)
            count += 1
        if count == 10:
            break
    return keywords
def main():
    files=open("cloud.txt","r")
    content=readfile(files)
    print(content)
    wordCountDict= wordCount(content)
    print(wordCountDict)
    topTenWords(content)
    
    stopWords = set(stopwords.words('english'))
    print("Top 10 keywords:- ")
    count = 0
    for w in content.split():
        if w not in stopWords:
            print(w)
            count += 1
        if count == 10:
            break
    files.close()
if __name__ == "__main__":
    main()