# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:16:06 2019

@author: dfb
"""

import collections, re
texts = ['John likes to watch movies. Mary likes too.',
   'John also likes to watch football games.']

with open('FoodInspection.txt', 'r') as file:
    data = file.read().replace('\n', '')

#print(data)

bagsofwords = [ collections.Counter(re.findall(r'\w+', txt))
            for txt in data]

#bagsofwords = [ collections.Counter(re.findall(r'\w+', txt))
#            for txt in texts]

#print( bagsofwords[0] ) 
#c =  collections.Counter({'likes': 2, 'watch': 1, 'Mary': 1, 'movies': 1, 'John': 1, 'to': 1, 'too': 1})
#print( bagsofwords[1] )
#d = collections.Counter({'watch': 1, 'games': 1, 'to': 1, 'likes': 1, 'also': 1, 'John': 1, 'football': 1})
#sumbags = sum(bagsofwords, collections.Counter())
#sumbags
#e = collections.Counter({'likes': 3, 'watch': 2, 'John': 2, 'to': 2, 'games': 1, 'football': 1, 'Mary': 1, 'movies': 1, 'also': 1, 'too': 1})
#print (sumbags)

#file = open(r"FoodInspection - Copy.txt", "r", encoding="utf-8-sig")
file = open(r"FoodInspection.txt", "r", encoding="utf-8-sig")

#Furthermore, for counting, you can use collections.Counter:
from collections import Counter
wordcount = Counter(file.read().split())
#print(wordcount)

for k,v in wordcount.items():
    if (v > 2000) and (v < 10000):
        print ( k, v)


filename = 'FoodInspection.txt'
filename = 'FoodInspection - Copy.txt'

file = open(filename, 'rt')
text = file.read()
file.close()
# Read in the file
#with open('file.txt', 'r') as file :
#  filedata = file.read()

# Replace the target string
#text = text.replace('RepeatViolation', 'Repeat Violation')
#text = text.replace('RepeatViolation', 'Repeat violation')
#text = text.replace('RepeatViolation', 'repeat violation')
#text = text.replace('RepeatViolation', 'REPEAT violation')


#Repeat Violation
#words = ['RepeatViolation' if x=='Repeat Violation' else x for x in words]


# Write the file out again
#with open('file.txt', 'w') as file:
#  file.write(filedata)
  

# split into words by white space
words = text.split()
# convert to lower case
words = [word.lower() for word in words]
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
#print(stripped[:100])
words = stripped
#Remove stop words like and to etc
#from nltk.corpus import stopwords
#stop_words = stopwords.words('english')
#print(stop_words)
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

words = ['New 310111' if x=='310111' else x for x in words]

words = ['mold' if x=='moldy' else x for x in words]
words = ['mold' if x=='moldincrease' else x for x in words]
words = ['mold' if x=='moldlike' else x for x in words]

words = ['fish' if x=='salmon' else x for x in words]
words = ['fish' if x=='seafood' else x for x in words]
words = ['fish' if x=='eggsfish' else x for x in words]
words = ['fish' if x=='shrimp' else x for x in words]
words = ['fish' if x=='fishseafood' else x for x in words]
words = ['fish' if x=='cdituna' else x for x in words]


words = ['meat' if x=='sausage' else x for x in words]
words = ['meat' if x=='meats' else x for x in words]
words = ['meat' if x=='pork' else x for x in words]
words = ['meat' if x=='chicken' else x for x in words]
words = ['meat' if x=='meateggs' else x for x in words]
words = ['meat' if x=='meatsraw' else x for x in words]
words = ['meat' if x=='beeffoods' else x for x in words]
words = ['meat' if x=='veal' else x for x in words]
words = ['meat' if x=='beeffoods' else x for x in words]
words = ['meat' if x=='hamburger' else x for x in words]
#
#words = ['meat' if x=='roasts' else x for x in words]
words = ['meat' if x=='nuggets' else x for x in words]
#words = ['meat' if x=='beeffoods' else x for x in words]


words = ['time' if x=='received' else x for x in words]
words = ['time' if x=='delivered' else x for x in words]
words = ['time' if x=='ready' else x for x in words]

words = ['temperature' if x=='degrees' else x for x in words]
words = ['temperature' if x=='degree' else x for x in words]
words = ['temperature' if x=='temps' else x for x in words]
words = ['temperature' if x=='cool' else x for x in words]
words = ['temperature' if x=='heat' else x for x in words]
words = ['temperature' if x=='hot' else x for x in words]
words = ['temperature' if x=='cooling' else x for x in words]
words = ['temperature' if x=='cold' else x for x in words]
words = ['temperature' if x=='temperatures' else x for x in words]

words = ['fridge' if x=='freezer' else x for x in words]
words = ['fridge' if x=='cooler' else x for x in words]
words = ['fridge' if x=='refrigerator' else x for x in words]
words = ['fridge' if x=='FRIG' else x for x in words]

words = ['scoop' if x=='scoops' else x for x in words]

words = [w for w in words if not w in stop_words]
words_remove = ['must','keep','use','please','least','make','day','tcs','walk','hold','650112','350116','a2','certified','330414','490311a','460111','450111','460111b'] 
words = [w for w in words if not w in words_remove]

words_remove = ['1','3','2','b','also','pic','hours','ensure','135f','held'] 
words = [w for w in words if not w in words_remove]

#cutting boards
#residue

from collections import Counter
wordcount = Counter(words)
#print(wordcount)
#list_B = [word if word != 'world' else 'friend' for word in list_A]
#print( wordcount.index("RepeatViolation") )
#Equipment must be in good repair. Repeat item
#need for cleaning pink residue cross contamination

for k,v in wordcount.items():
    #if (v > 400) and (v < 2000):
    #    print ( k, v)
    if (k=='repeat'):
        print ( k, v)
    if (k=='violation'):
        print ( k, v)
    if (k=='contamination'):
        print ( k, v)
    if (k=='recontamination'):
        print ( k, v)
    if (k=='residue'):
        print ( k, v)
    if (k=='growth'):
        print ( k, v)
    if (k=='soiled'):
        print ( k, v)
    if (k=='equipment'):
        print ( k, v)
    if (k=='employees'):
        print ( k, v)
        #RepeatViolation

#a=[1,2,3,1,3,2,1,1]
#[4 if x==1 else x for x in a]



from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
data_corpus = ["John likes to watch movies. Mary likes movies too.", "John also likes to watch football games."]
#X = vectorizer.fit_transform(data_corpus) 
#X = vectorizer.fit_transform(words) 
#print(vectorizer.vocabulary_)
#print(X.toarray())
#print(vectorizer.get_feature_names())