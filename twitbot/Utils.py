import tweepy
import json


#auth shinannigans
keys = json.loads(open("credenciales.json").read())

auth = tweepy.OAuthHandler(keys["consumer_key"],keys["consumer_secret"])
auth.set_access_token(keys["access_token"],keys["access_token_secret"])

tapi = tweepy.API(auth, wait_on_rate_limit=True,
                  wait_on_rate_limit_notify=True)

#print (json.dumps(tapi.me()._json, indent=3))

tweetTarget=tapi.get_status("1255519947314339842")

print (json.dumps(tweetTarget._json, indent=3))




