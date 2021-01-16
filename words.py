#coding; utf-8

from requests_oauthlib import OAuth1Session
import json
import os
import random
from datetime import datetime

def puttweet():

	#print(os.environ["CONSUMER_KEY"])
	#print(os.environ["CONSUMER_SECRET"])
	#print(os.environ["ACCESS_TOKEN_KEY"])
	#print(os.environ["ACCESS_TOKEN_SECRET"])

	twitter = OAuth1Session(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])

	f = open('./data.txt')
	today = datetime.now()

	while 1:
		line = f.readline()
		if not line:
			break

		datetext, text = line.split(',')
		mon, day = datetext.split('/')
		if int(mon) == today.month and int(day) == today.day:
			#msg = unicode(text, 'utf-8')
			msg = text.replace('\n','')
			msg = msg[0:138]
			msg += str(today.second)
			params = {"status": msg} 
			#print(params)
			req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
			print(today,req.status_code,msg)

if __name__ == "__main__":
	puttweet()
