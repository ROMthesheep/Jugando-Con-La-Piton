import tweepy
import json


class TweetListener(tweepy.StreamListener):
    def on_connect(self):
        print("Estoy pendiente del tweet!")


    def on_status(self, status):
        try:
            file = open("reg.txt", "a")
            file.write(status._json["user"]["screen_name"] + )
            print(status._json["user"]["screen_name"])
            file.write("\n")
            print("\n")
            file.close()

        except:
            pass

    def on_error(self, status_code):
        print("Sa liao hermano ", status_code)

#auth shinannigans
keys = json.loads(open("credenciales.json").read())

auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])

tapi = tweepy.API(auth, wait_on_rate_limit=True,
                  wait_on_rate_limit_notify=True)

# logica prebarrido

stream = TweetListener()
streamingApi = tweepy.Stream(auth=tapi.auth, listener=stream)


streamingApi.filter()