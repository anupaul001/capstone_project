from sklearn.cluster import KMeans
import numpy as np
import re
import nltk
import csv
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

def reading():
    all_messages = []
    with open("Filtered.csv","r") as csvfile:
        myfile = csv.reader(csvfile)
        for line in myfile:
            all_messages.append(line[4])

    # all_messages = all_messages[:]
    # print((all_messages))
    return all_messages

def clean(msg):
    try:
        tokens=[]
        for tweet in msg:

            tweet = re.sub(r'[^\w\s]', '', tweet)  # delete punctuations
    # tweet = re.sub(r"(?:\@\'https?\://)\s+", "", tweet)  # customized deletion
    # tweet = re.sub(r'\bRT\b\s+', "", tweet)
            tweet = re.sub("\d+", "", tweet)  # remove number from tweet
            tokens_next = nltk.word_tokenize(tweet)
    # print tokens_next
            stopwords = nltk.corpus.stopwords.words('english')  # stopword reductio
            tokens_next = [w for w in tokens_next if w.lower() not in stopwords and len(w) > 2]
    # print tokens_next
            for i in tokens_next:
                    tokens.append(i)

    # ps = PorterStemmer()
    # tokens_next=[ps.stem(w) for w in tokens_next]

        # print "afterrrrr"
        # print tokens

        return tokens
    except ValueError:
         print 'My exception occurred, value:'


def save(msg):
    print msg
    with open("tokens.csv", "wb") as csvfile:
        myfile = csv.writer(csvfile, dialect="excel")
        myfile.writerow("TOKENS")
        for label in msg:
            myfile.writerow([label])



def main():

    all_messages = reading()
    msg=clean(all_messages)
    save(msg)




main()
