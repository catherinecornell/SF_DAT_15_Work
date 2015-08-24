###Saas based business live and die off customer satisfaction. I wanted to create a model
#to identify both venues who are vocally unhappy with our service and venues who are
#vocally pleased with our service. I decided to look for reference customers and customers 
#that need account management 
#attention by analyzing our customer support emails and tweets for positive or negative 
#comments. 

#Step 1 Collect zendesk comment data for the last 8 months: 
import csv
import json
import pandas as pd
import requests
url_template = 'https://breadcrumb.zendesk.com/api/v2/tickets/{0}/comments.json'
for page in [338123,338937,338342,338342,340313,340051,340337,340790]: 
    url = url_template.format(page)
    user = 'ccornell@groupon.com'
    pwd = 'breadcrumb1023'
    response = requests.get(url, auth=(user, pwd))
    old_data = response.json()
 
 


url = 'https://breadcrumb.zendesk.com/api/v2/tickets.json'
user = 'ccornell@groupon.com'
pwd = 'breadcrumb1023'
params = {}
params['id'] = '204343'
params['ticket_form_id'] = '6111'
request = requests.get(url, auth=(user, pwd), params = params)
ticket_data = request.json()





#sanity check
print response
data = response.json()
data.items()
zendesk_data=str(data.items())
print zendesk_data[:20]
type(zendesk_data)
zendesk_data.split()
print data
type(response.json())
data.keys()
new_data = json.loads(old_data)[0]

old_data[u'comments'][0].keys()

#cycle through everything "for i in dictionary , make the comments into a dictionary, 
#


import re
def isGoodString(s):
   reg = '^\w+$'
   return re.search(reg, s)
   print s
isGoodString(zendesk_data)


from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(ngram_range=(1,3), tokenizer=isGoodString)
vect.fit_transform(zendesk_data)
([a for a in zendesk_data.split(' ') if isGoodString(a)])


from collections import Counter
c = Counter(zendesk_data)
c.most_common(25) 
sorted(c.items())[:25]  # counts similar words separately
for item in sorted(c.items())[:25]:
    print item[0], item[1]

import nltk
new_zendesk_data = nltk.word_tokenize(zendesk_data)
type(tokenized)
new_zendesk_data = []
tokenized = new_zendesk_data
print new_zendesk_data

from textblob import TextBlob, Word


blob = TextBlob(zendesk_data)
blob.sentences
blob.sentiment.polarity
[sent.sentiment.polarity for sent in blob.sentences]
if blob.sentiment.polarity != 0:
    return blob.sentance
    blob.classify

blob.classify


blob = TextBlob("i hate bananas")
-COUNT 25 MOST COMMON WORDS IN POSITIVE TICKETS
-COUNT 25 MOST COMMON WORDS IN NEGATIVE TICKETS

#Step 5 Use text blob to analyze the sentiment of the comments and tweets

from textblob import TextBlob, Word

#Step 6 Break sentiment scores into three categories: Detractor, Passive, Promoter.
#Merchants that fall into the Detractor group will receive an outbound call from our 
#account management team. Merchants in the Promoter category will receive an incentive 
#package from their sales rep to act as a referrl or testimonial custmer. 

#Need to include metrics and accurrancy in the model

import tweepy

api_key = 'BQaCxgwhdCqxT5eZGRSG2WTMY'
api_secret = 'xmXhfJm1Ek3G6ZTQaXHAqrb5PvzRI2z4uLAszmhIlXVwyMXCtV'
access_token = '3319244641-BYLSBHhqRtlE4xD7FAEWsWCk1KeBSdloKUlHoFT'
access_secret = 'giybjEH94aNngxUc8YbEFgDm01WtWRccYOXbP17DEAz65'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


tweets = tweepy.Cursor(api.search,
                           q="breadcrumb",
                           result_type="recent",
                           lang="en").items()

for tweet in tweets:
    print tweet.text, tweet.user.screen_name, tweet.user.friends_count


    

from textblob import TextBlob

def ToSentiment(string):
    return TextBlob(string).sentiment.polarity
    
ToSentiment('i hate bananas')

tweets['sentiment'] = tweets.Text.map(stringToSentiment)

# Make a column called day which holds the unique
# day it was tweeted, e.g. 5/24/2015


tweets['day'] = tweets.Date.map(lambda x: x[:10])

sent = tweets.groupby('day')['sentiment'].mean()
volume = tweets.groupby('day')['Status'].mean()


sent.plot()

volume.plot()

mport csv
import json
import pandas as pd
import requests
url_= 'https://breadcrumb.zendesk.com/api/v2/tickets.json'

    user = 'ccornell@groupon.com'
    pwd = 'breadcrumb1023'
    response = requests.get(url, auth=(user, pwd))
    old_data = response.json()




###TAKE THE VOICEMAILS AND SORT BASED ON HOW PISSED PEOPLE SOUNDDDD

 
