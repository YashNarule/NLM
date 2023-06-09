# -*- coding: utf-8 -*-
"""nlm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qPYSwJRWnJwWX_9usQ9dWIo57IddqdBN

# **NLM Assignment 1**


*   USN-ENG20AM0063

*   Name-Yash Mahesh Narule
*   Section-6H
"""



"""**All the inport statements**"""

#taking all the inputs for the code
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

import seaborn as sns
import matplotlib.pyplot as plt

from tqdm.auto import tqdm
import time

#reading data from the csv file which has been take from kaggle website
#https://www.kaggle.com/code/sujithmandala/spam-filtering-nlp-logistic-regression-98-acc/input
df = pd.read_csv('/content/spam.csv',encoding='latin-1')

#checking the data frame
df

#dropping unwanted columns
df.drop(['Unnamed: 2','Unnamed: 3', 'Unnamed: 4'], axis = 1, inplace = True)

#checking our data
df.head()

# Concatenate all tweet texts into a single string
all_text = ' '.join(df['v2'].values)
# Remove URLs, mentions, and hashtags from the text
all_text = re.sub(r'http\S+', '', all_text)
all_text = re.sub(r'@\S+', '', all_text)
all_text = re.sub(r'#\S+', '', all_text)

#checking our all tweets are mergerd correctly or not
all_text

"""**Tokenization**"""

#using nltk library and using word_tokenize funtion we tokenize the data collected#yash_narule
nltk.download('punkt')
nltk_tokens = nltk.word_tokenize(all_text)
print (nltk_tokens)

"""**Using Regular Expression with Findall function to list meaningful tokens from the source dataset**"""

regex = '[a-zA-Z]+'                
clean = re.findall(regex,all_text) 
print(clean)

"""**Removing Stop Words**"""

from nltk.corpus import stopwords
nltk.download('stopwords')

tokens_without_sw = [word for word in clean if not word in stopwords.words()]

print(tokens_without_sw)

"""Some more fine cleaning using the rear expressions"""

#removing single words like n,g,etc
clean2=[]
r = '[a-zA-Z]'             
for words in tokens_without_sw:
  if words not in (re.findall(r,words)):
    clean2.append(words) 
print(clean2)

"""**Normalization And Converting it to lower string**"""

clean3=[]
for words in clean2:
  clean3.append(words.lower())
print(clean3)

"""**Lemmatization of data set**"""

#importing word package from textblob to lemmatize the words#yash_narule
from textblob import Word
nltk.download('wordnet')
nltk.download('omw-1.4')
clean4=[]
clean5=[]
clean6=[]
clean7=[]
clean8=[]

for words in clean3:
  v = Word(words)
  clean4.append(v.lemmatize())
for words in clean4:
  v = Word(words)
  #verb
  clean5.append(v.lemmatize("v"))
for words in clean5:
  v = Word(words)
  #Adjective
  clean6.append(v.lemmatize("a"))
for words in clean6:
  v = Word(words)
  #Noun
  clean7.append(v.lemmatize("n"))
for words in clean7:
  v = Word(words)
  #Abverb
  clean8.append(v.lemmatize("r"))
print(clean8)

"""**Word Frequency**"""

# counter to count the txts
from collections import Counter
top_words=[]
word_counts = Counter(clean8)
top_words = word_counts.most_common()
top_words



"""## Web Scraping """

#import statements
import requests
from bs4 import BeautifulSoup

#yash_narule
import requests
from bs4 import BeautifulSoup
#requesting the requests from the url
page = requests.get('https://www.businessinsider.in/sports/the-20-most-famous-athletes-in-the-world/slidelist/52209638.cms#slideid=52209639')
soup = BeautifulSoup(page.text, 'html.parser')

#checking the response what we got
print(soup.prettify())

#finding all the H2 tags
names=[]
artist_name_list_items = str(soup.find_all('h2'))
artist_name_list_items

# Concatenate all tweet texts into a single strin
# Remove URLs, mentions, and hashtags from the text
all_text2 = re.sub(r'"[0-9]+\t[\w+]"', '', artist_name_list_items)
all_text2

#using regular expression to get unique players names
regex ='[0-9]+ [a-zA-z]+ \w+'             
uni_names=[]
names = re.findall(regex,artist_name_list_items)
names
for x in names:
  if x not in uni_names:
    uni_names.append(x)
uni_names

#to find the meaning full content from the website here we have it in span=caption class
elements = str(soup.find_all("span", class_="caption"))
elements

#using regular expressions to tokenize the data collected
new_web=[]
from nltk.classify.rte_classify import RegexpTokenizer
rg=r"[0-9]*.[0-9]*[\w]* [\w]*[<\/p>]+$"
tokens_web=RegexpTokenizer(rg)
new_web=tokens_web.tokenize(elements)

#fine cleaning of the data
ver1=[]
for word in new_web:
  if word !="a></p>":
    ver1.append(word)
ver1

#gathering the key words and discard the unuseful words
new_web=[]
for txt in ver1:
  new_web.append(txt.replace("</p>",""))
new_web

#final cleaning
new_web1=[]
for txt in new_web:
  new_web1.append(txt.replace(": ",""))
new_web1

#gathering all the data in to differnt list for further usage
a=0
b=1
c=2
d=3
game=[]
country=[]
salary=[]
endo=[]
for i in range(0,20):
  game.append(new_web1[a])
  country.append(new_web1[b])
  salary.append(new_web1[c])
  endo.append(new_web1[d])
  a=a+4
  b=b+4
  c=c+4
  d=d+4
print(game)

#tabulating the collect the data 
from tabulate import tabulate

print(tabulate([uni_names,game,country,salary,endo], tablefmt="simple"))



"""# **Same process using 2nd type of source Data**"""

!pip install textract
import textract
text = textract.process('/content/book.pdf', method='pdfminer')

text

#using nltk library and using word_tokenize funtion we tokenize the data collected#yash_narule
all_text=str(text)
nltk.download('punkt')
nltk_tokens = nltk.word_tokenize(all_text)
print (nltk_tokens)

regex = '[a-zA-Z]+'                
clean = re.findall(regex,all_text) 
print(clean)

from nltk.corpus import stopwords
nltk.download('stopwords')
tokens_without_sw = [word for word in clean if not word in stopwords.words()]

print(tokens_without_sw)

#removing single words like n,g,etc
clean2=[]
r = '[a-zA-Z]'             
for words in tokens_without_sw:
  if words not in (re.findall(r,words)):
    clean2.append(words) 
print(clean2)

clean3=[]
for words in clean2:
  clean3.append(words.lower())
print(clean3)

#importing word package from textblob to lemmatize the words#yash_narule
from textblob import Word
nltk.download('wordnet')
nltk.download('omw-1.4')
clean4=[]
clean5=[]
clean6=[]
clean7=[]
clean8=[]

for words in clean3:
  v = Word(words)
  clean4.append(v.lemmatize())
for words in clean4:
  v = Word(words)
  #verb
  clean5.append(v.lemmatize("v"))
for words in clean5:
  v = Word(words)
  #Adjective
  clean6.append(v.lemmatize("a"))
for words in clean6:
  v = Word(words)
  #Noun
  clean7.append(v.lemmatize("n"))
for words in clean7:
  v = Word(words)
  #Abverb
  clean8.append(v.lemmatize("r"))
print(clean8)

# counter to count the txts
from collections import Counter
top_words=[]
word_counts = Counter(clean8)
top_words = word_counts.most_common()
top_words

