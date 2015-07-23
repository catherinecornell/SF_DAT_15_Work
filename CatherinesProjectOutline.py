###Saas centered businesses live and die off customer satisfaction. I wanted to create a model
#to identify customers who are vocally unhappy with our service and venues who are
#vocally pleased with our service. I decided to look for both potenial reference customers and customers 
#that need account management 
#attention by analyzing our customer support emails and tweets for positive or negative 
#comments. 


#Step 1 Collect zendesk comment data for the last 8 months: 

>>> import requests
>>> response = requests.get(url, auth=(user, pwd))
>>> url = 'https:/{subdomain}.zendesk.com/api/v2/tickets/{org_tag}/comments.json'
>>> user = 'myemail@company.com'
>>> pwd = 'password'
params = {}
params['public'] = Yes
params['created_at'] > 01-01-2015
>>> response = requests.get(url, auth=(user, pwd), params=params)
#sanity check
>>> print response
<Response [200]>
>>> data = response.json()

#Step 2 Turn zendesk data into a csv

zendesk_data= [ ]

zendesk_dataWriter = csv.writer(open('zendesk_comments.csv', 'w'), dialect='excel', delimiter=' ',quotechar='|')
zendesk_dataReader = csv.reader(open("C:\StoredTweets.csv", "r"))

for row in zendesk_dataReader:

    #TweetList.append(rows)
    Tweets.append({ 'tweet': row[0], 'date': row[1] }) ## Stores from CSV in list.

for rows in Tweets:


    #print TweetList

    data = urllib.urlencode({'Tweet': row[0], 'Date': row[1]}) ##Takes Tweet and date to construct query.

    #print data

    API_request = urllib.urlopen("http://data.tweetsentiments.com:8080/api/analyze.json?q=", data) ## Adds query to end of URL and queries API

    result = json.load(API_request('{"sentiment":}') ## "Sentiment": is a heading in the JSON response

    TweetWriter.writerow(result)
    
# Step 3 Collect twitter data from the last 8 months
https://api.twitter.com/1.1/search/tweets.json?q=breadcrumb%20pos&src=typd

for row in zendesk_dataReader:

    #TweetList.append(rows)
    Tweets.append({ 'tweet': row[0], 'date': row[1] }) ## Stores from CSV in list.

for rows in Tweets:


    #print TweetList

    data = urllib.urlencode({'Tweet': row[0], 'Date': row[1]}) ##Takes Tweet and date to construct query.

    #print data

    API_request = urllib.urlopen("http://data.tweetsentiments.com:8080/api/analyze.json?q=", data) ## Adds query to end of URL and queries API

    result = json.load(API_request('{"sentiment":}') ## "Sentiment": is a heading in the JSON response

    TweetWriter.writerow(result)



#Step 4 Turn twitter data into a csv



#Step 5 Use text blob to analyze the sentiment of the comments and tweets

from textblob import TextBlob, Word




#Step 6 Break sentiment scores into three categories: Detractor, Passive, Promoter.
#Merchants that fall into the Detractor group will receive an outbound call from our 
#account management team. Merchants in the Promoter category will receive an incentive 
#package from their sales rep to act as a referrl or testimonial custmer. 

#Bonus step: set up our twitter account to auto retweet positive comments. 




 
