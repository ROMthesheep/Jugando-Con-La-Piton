import tweepy
import json
import _json

#auth shinannigans
keys = json.loads(open("credenciales.json").read())

auth = tweepy.OAuthHandler(keys["consumer_key"],keys["consumer_secret"])
auth.set_access_token(keys["access_token"],keys["access_token_secret"])

tapi = tweepy.API(auth, wait_on_rate_limit=True,
                  wait_on_rate_limit_notify=True)

#obtener infpormacion propia
# data = tapi.me()
# print (json.dumps(data._json, indent=2))

# obtener info de tweet
print(json.dumps(tapi.get_status("1255565860481249282")._json, indent=2))

# obtener followers
#data = tapi.followers("Santi_ABASCAL")
 # for user in data:
 #     print(json.dumps(user._json,indent=2))

# # paqueton de datos 100  mas mejor que 20
# for user in tweepy.Cursor(tapi.followers, "Santi_ABASCAL").items(100):
#     print(json.dumps(user._json,indent=2))

# Obtener timeline
# for userlm in tweepy.Cursor(tapi.user_timeline, "romthesheep", tweet_mode="extended").items(1):
#     print(json.dumps(userlm._json, indent=2))

# Buscar tweets
# for tw in tweepy.Cursor(tapi.search, q="España", tweet_mode="extended").items(1):
#      print (json.dumps(tw._json, indent=2))

# # publicar tweet
# tapi.update_status("aqui con la piton")
# # hacer RT y fav
# tweetId= "1017528972802973696"
# tapi.retweet(tweetId)
# tapi.create_favorite(tapi.me()._json["status"]["id"])
# tapi.destroy_favorite(tapi.me()._json["status"]["id"])
# respodner a tweet
# tapi.update_status("texto random", in_reply_to_status_id="1255445683588534273")

# media
# idImagen = tapi.media_upload("./imagen.jpg")
# print (idImagen)

#tapi.update_status("texto", media_ids=["7864917865"])

# seguir a cuentas
# tapi.create_friendship("nike")
# tapi.destroy_friendship("nike")

# mandar MD
# tapi.send_direct_message(idUser, text="jajaxd")
