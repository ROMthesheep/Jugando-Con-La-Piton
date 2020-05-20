import tweepy
import json
import wget
from pathlib import Path
import sys

counter=0
counterimgs=0

class TweetListener(tweepy.StreamListener):
    def on_connect(self):
        global targetWord
        print("Estoy escuchando a los resultados de: " + targetWord)
        Path("./imgs/" + targetWord + "/").mkdir(parents=True, exist_ok=True)
    def on_status(self, status): #logica en barrido
        global  counter
        global counterimgs
        check=1
        # print(json.dumps(status._json, indent=3))
        counter+=1
        print(status.text,"\nTweets analizados: ",counter,"\nImagenes obtenidas: ",counterimgs,"\n\n")

        try:
           wget.download(status._json["entities"]["media"][0]["media_url"], out="./imgs/" + targetWord + "/")
           check=2
           counterimgs+=1
        except:
            pass
        # if check == 2:
        #     sys.exit()
    def on_error(self, status_code):
        print("algo ha pasao ",status_code)

#auth shinannigans
keys = json.loads(open("credenciales.json").read())

auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])

tapi = tweepy.API(auth, wait_on_rate_limit=True,
                  wait_on_rate_limit_notify=True)

# logica prebarrido
print("word based image scrapper, creara una carpeta llamada imgs en donde este programa este alojado")
print("Dame la palabra sobre la que quieres monitorizar:")
targetWord=input()


stream = TweetListener()
streamingApi = tweepy.Stream(auth=tapi.auth, listener=stream)

streamingApi.filter(
    track=[targetWord],
)