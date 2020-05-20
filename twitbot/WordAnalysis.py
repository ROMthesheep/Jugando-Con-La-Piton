import tweepy
import json
import keyboard
import itertools
import matplotlib.pyplot as plt
import squarify
from wordcloud import WordCloud
from pathlib import Path
import numpy as np

plt.rcParams.update({'font.size': 8})
keys = json.loads(open("credenciales.json").read())

auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])

tapi = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

palabras = {}
counter = 0


class IlloEhcushameEhta(tweepy.StreamListener):
    def on_connect(self):
        global palabras
        global targetWord
        Path("./WordAnalysis/"+targetWord).mkdir(parents=True, exist_ok=True)
        print("habla cucuruxo que yo te ehcuxo")

    def on_status(self, status):
        palabrasNoSignificativas = [targetWord.lower(), "ni", "hay", "sí", "si", "ya", "todo", "esta", "este", "sea",
                                    "le", "ha", "se", "es", "no", "mas", "nos", "más", "del", "y", "tu", "yo", "ellos",
                                    "vosotros", "el", "´él", "la", "lo", "los", "las", "un", "una", "unos", "unas",
                                    "que", "cuales", "qué", "a", "ante", "bajo", "con", "contra", "de", "desde",
                                    "durante", "en", "enter", "hacia", "hasta", "mediante", "para", "por", "según",
                                    "sin", "so", "sobre", "tras", "versus", "vía", "xd", "rt", "fav", "🇪🇸", "|","mi",
                                    "tiene", "está", "1.", "2.", "3.", "4.", "5.", "🇫🇷", "🇺🇸", "🇮🇹", "🇨🇳", "🚩*", "http*",
                                    "van", "me", "ir", "voy", "ahora", "cuando", "estas", "hace", "porque", "estás",
                                    "ademas", "además", "luego", "espera", "sigue", "al", "vaya", "%", "son", "haya",
                                    "⚽️", "🔹", "como", "están", "su", "te", "cuál", "ser", "otro", "muy"]
        tweetaso = status.text.split()
        global counter
        try:
            for p in tweetaso:
                if not palabrasNoSignificativas.__contains__(p.lower()) and not palabras.__contains__(p.lower()):
                    palabras[p] = 1
                elif palabras.__contains__(p.lower()):
                    palabras[p] += 1
        except:
            pass
        counter = counter + 1
        top = dict(itertools.islice(palabras.items(), 15))
        for key, value in sorted(top.items(), key=lambda item: item[1],reverse=True):
            print("%s: %s" % (key, value))
        print("\n\n")
        print(counter)
        print("\n\n")

        if keyboard.is_pressed('q'): #Comienza el cierre
            # Desmantelando la lista
            valores = list(top.values())
            claves = list(top.keys())

            # Generando grafico treemap
            squarify.plot(sizes=valores, label=claves, alpha=.8)
            plt.title('Palabras relacionadas con ' + targetWord + ":")

            plt.axis('off')
            fl = "WordAnalysis Treechart" + targetWord + ".png"
            plt.savefig("./WordAnalysis/"+targetWord+"/"+fl, dpi=200)

            plt.close() # cerramos la instancia de matplotlib

            # Diagrama barras
            y_pos=np.arange(len(valores))
            plt.barh(y_pos,valores)
            plt.yticks(y_pos,claves)
            plt.title('Palabras relacionadas con ' + targetWord + ":")
            fl = "WordAnalysis barras" + targetWord + ".png"
            plt.savefig("./WordAnalysis/"+targetWord+"/"+fl, dpi=200)
            # Creacion del txt
            try:
                file = open("./WordAnalysis/"+targetWord+"/top 15 palabras.txt", "a")
                file.truncate(0)
                for key, value in sorted(top.items(), key=lambda item: item[1], reverse=True):
                    try:
                        file.write("%s: %s\n" % (key, value))
                    except:
                        pass

                mensaje="Se han analizado %s Tweets" % counter
                
                file.write(mensaje)
                file.close()
            except:
                pass
            return False # cerramos el listener

    def on_error(self, status_code):
        print("illo hermano tas pasao:", status_code)


print("dame una palabra hermano")
targetWord = input()

streamApi = tweepy.Stream(auth=tapi.auth, listener=IlloEhcushameEhta())

streamApi.filter(
    track=[targetWord]
)