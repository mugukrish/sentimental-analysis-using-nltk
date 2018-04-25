#!/usr/bin/env python

import sys
import pandas as pd
import nltk
from nltk import classify
from nltk.classify.util import accuracy
from sklearn.model_selection import train_test_split
import MySQLdb

nltk.data.path.append('/home/mugunth/nltk_data')


user_input_feedback = str((sys.argv[1]))
#inp = ["awesome movie", "dont watch not a good movie","this is the best movie ever","worst movie",
#       "story is the best", "no story at all boring movie",]
#user_input_feedback = "it is very nice and timings of library is good "
data=pd.read_excel("train.xlsx")
data.dropna(inplace=True)
data["label"]=data["label"].astype(int)
data["feedback"]=data["feedback"].astype(str)
data.drop(data[data.label == 2].index,inplace=True)
data["label"].replace({1:0,3:4},inplace=True)
data["label"].replace({0:-1,4:1},inplace=True)
print("hi")
print(user_input_feedback)

def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

positive=data[data['label']==1]['feedback']
#negative=pd.concat([data[data['label']==-1]['feedback'],data[data['label']==0]['feedback']])
negative=data[data['label']==-1]['feedback']
pos = []
for i in positive:
    pos.append([format_sentence(i), 'pos'])
neg = []
for i in negative:
    neg.append([format_sentence(i), 'neg'])

print(len(pos),len(neg))

training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]
test = pos[int((.8)*len(pos)):] + neg[int((.8)*len(neg)):]
classifier = classify.naivebayes.NaiveBayesClassifier.train(training)
#print(classifier.show_most_informative_features())
#print(classifier.classify(format_sentence(user_input_feedback)))
ans = classifier.classify(format_sentence(user_input_feedback))
print(ans)

with open('output.txt','w') as f:
    f.write(str(ans))

#print(accuracy(classifier, test))



db = MySQLdb.connect("127.0.0.1","root","spiderman","feedback" )
cursor = db.cursor()
lab =1 if ans == 'pos' else -1
cursor.execute("insert into nlpt_feedback values(%s,%s)",(user_input_feedback,lab))
db.commit()
db.close()
'''
for i in inp:
    ans = classifier.classify(format_sentence(i))
    print(ans)

    with open('output.txt','w') as f:
        f.write(str(ans))

    #print(accuracy(classifier, test))



    db = MySQLdb.connect("127.0.0.1","root","spiderman","feedback" )
    cursor = db.cursor()
    lab =1 if ans == 'pos' else -1
    cursor.execute("insert into nlpt_feedback values(%s,%s)",(i,lab))
    db.commit()
    db.close()
'''
