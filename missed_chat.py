import csv
import json
import pandas as pd
import requests
url = 'https://www.zopim.com/api/v2/chats'
user = 'ratkins@groupon.com'
pwd = 'Groupon1'
request = requests.get(url, auth=(user, pwd))
chat_data = request.json()
nested_data = chat_data['chats']

def get_useful_info(message_dict):
    result = {}
    keys = ["visitor.name","visitor.phone", "visitor.email","session.region", "timestamp", "message", "unread", "session.country_code"]
    for key in keys:
        split_key = key.split(".")
        nested_obj = message_dict.copy()
        for nested_key in split_key:
            if nested_obj.has_key(nested_key):
                nested_obj = nested_obj[nested_key]
        result[key] = nested_obj
    return result

res = []
for datum in nested_data:
    res.append(get_useful_info(datum))

info = pd.DataFrame(res)

missed = info[(info['unread'] == True) & (info['session.country_code']=='US') ]
del missed['unread']
del missed['session.country_code']
missed.to_csv('missed_chat.csv', index=False) 

#send an email
import smtplib
import os

from email.mime.multipart import MIMEMultipart


# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Missed Chat Leads'
# me == the sender's email address
# family = the list of all recipients' email addresses
msg['From'] = 'ccornell@groupon.com'
msg['To'] = ('catherinefcornell@gmail.com')
msg.preamble = 'Missed Chat Leads'
msg.attach('missed_chat.csv')

# Send the email via our own SMTP server.
s = smtplib.SMTP('localhost')
s.sendmail(msg['From'], msg['To'], msg['Subject'])
s.quit()




##def is_unread():
	##for i in nest_data.type

##timestamp stripped of hms, region, country, vistor{phone, email
##name, message, unread(bool), type 
