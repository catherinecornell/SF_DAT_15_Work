# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 20:38:20 2015

@author: ccornell
"""
import csv
import json
import pandas as pd
import requests
import numpy as np
commentdata = {}
url_template = 'https://breadcrumb.zendesk.com/api/v2/tickets/{0}/comments.json'
data = []
for page in [323161,323196,323642,323646,323656,325150,325158,325162,325207,
325224,325425,325426,325514,325669,325818,325821,325823,325824,325831,325846,
326201,328588,331016,331142,331253,331296,331360,331780,332623, 333707,333944,
335162,335483,336171,336206,336210,336971,336974,336990,337331,337406,337691,
337779,338074,338128,338229,338262,338267,338284,338285,338286,338502,338504,
338516,338546,338645,338657,338660,338705,338757,338780,338800,338808,338811,
338816,338904,338933,339034,339041,339064,339131,339136,339191,339284,339375,
339486,339524,339538,339540,339544,339550,339942,339958,339969,339976,339981,
339993,340363,340366,340404,340409,340431,340442,340450,340451,340464,340482,
340483,340486,340519,340532,340534,340535,340541,340543,340548,340551,340556,
340562,340577,340587,340601,340620,340622,340639,340703,340869,340905,341012,
341015,341260,341267,341987,342171,342244,342247,342268,342298,342621,342630,
342650,342654,342699,342702,342705,342764,342789,342820,342849,342855,]:
    url = url_template.format(page)
    user = 'ccornell@groupon.com'
    pwd = ''
    response = requests.get(url, auth=(user, pwd))
    commentdata[page]=response.json()
    nested_data = commentdata[page]['comments'][0]['data']
    data.append({
        'comments': nested_data['transcription_text'],
        'call_duration': nested_data.get('call_duration'),
        'callback_number': nested_data.get('from'),
        'ticket_id': nested_data.get('ticket_ids')
    })
    

pd.DataFrame(data).to_csv('voicemails.csv', index=False)    
voicemails=pd.read_csv('voicemails.csv')  
voicemails.head()  
voicemails.comments.count()
voicemails.isnull().sum()
voicemails.fillna(value= "hangup" , inplace=True)


stringcomment= []
for comment in voicemails.comments:
    str(comment)
    stringcomment.append(comment)

len(stringcomment)

from textblob import TextBlob
#http://aparrish.neocities.org/textblob.html
#TextBlob can calculate the "sentiment" of a sentence. 
#"Sentiment" is a measurement of the emotional content of the sentence: 
#the number is positive (between 0 and 1) if the sentence says something 
#"good" and negative (between 0 and -1) if the sentence says something "bad."
#http://planspace.org/20150607-textblob_sentiment/ -DEFINITIONS OF POLARITY AND SUBJECTIVITY

train = [('sync errors', 'neg'),
    ('declining all', 'neg'),
     ('offline mode', 'neg'),
     ('I have been on hold for 8 minutes', 'neg'),
     ('No one has returned my call', 'neg'),
     ('middle of dinner service', 'neg'),
     ('great service', 'pos'),
     ('i have a question about my reports', 'pos'),
     ('thank you', 'pos'),
     ('thank you', 'pos'),
     ('thank you', 'pos'),
     ('quick question about how to add a user', 'pos'),
     ('monthly subscription charge question', 'pos')

 ]

test = [('I am still waiting for a call back', 'neg'),
     ('Im an accountant and I had a question about balancing reports', 'pos'),
     ('declining everything', 'neg'),
     ('I have been waiting on hold for 20 minutes', 'neg'),
     ('This problem is still not resolved', 'neg')
 ]

from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(train)

cl.classify("im in offline mode")

prob_dist = cl.prob_classify("im in offline mode")
prob_dist.max()
round(prob_dist.prob("pos"), 2)
round(prob_dist.prob("neg"), 2)    

cl.classify("we are busy with dinner service and need help")

prob_dist = cl.prob_classify("we are busy with dinner service and need help")
prob_dist.max()
round(prob_dist.prob("pos"), 2)
round(prob_dist.prob("neg"), 2)    


polarity=[]


def GetPolarity(string):
    return TextBlob(string).polarity

for i in stringcomment:
    j = GetPolarity(i)
    polarity.append(j)

voicemails['polarity'] = polarity

subjectivity = []

def GetSubjectivity(string):
    return TextBlob(string).subjectivity

for string in stringcomment:
    j = GetSubjectivity(string)
    subjectivity.append(j)

voicemails['subjectivity']= subjectivity

sentiment=[]

def GetSentiment(string):
    return TextBlob(string).sentiment

for string in stringcomment:
    j = GetSentiment(string)
    sentiment.append(j)

voicemails['sentiment']= sentiment

pos_or_neg=[]

def GetPosOrNeg(string):
    return cl.classify(string)

for string in stringcomment:
    j = GetPosOrNeg(string)
    pos_or_neg.append(j)

voicemails['pos_or_neg']=pos_or_neg

ProbNeg=[]

def GetProbNeg(string):
    return cl.prob_classify(string).prob('neg')
    
for string in stringcomment:
    j = GetProbNeg(string)    
    ProbNeg.append(j)

voicemails['prob_neg']=ProbNeg    

ProbPos=[]


def GetProbPOS(string):
    return cl.prob_classify(string).prob('pos')
    
for string in stringcomment:
    j = GetProbPOS(string)    
    ProbPos.append(j)
    

voicemails['prob_pos']=ProbPos


#sanity check that the new created columns were added to the datafram
voicemails.head()

voicemails.plot(x='call_duration', y='prob_neg', kind='scatter', alpha=0.3)

voicemails.sentiment.mean()
cl.classify("im in middle of dinner service and need a call")

#this spits out the index for the highest sentiment
voicemails.polarity.idxmin(axis=0, skipna=True)
voicemails.sentiment[15]
voicemails.prob_neg[15]
voicemails.comments[15]

voicemails.prob_neg.idxmax(axis=0, skipna=True)
voicemails.sentiment[68]
voicemails.comments[68]
voicemails.prob_neg[68]

voicemails.prob_pos.idxmax(axis=0, skipna=True)
voicemails.comments[115]
voicemails.sentiment[115]
