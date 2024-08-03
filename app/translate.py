import googletrans
import random
from googletrans import Translator
import time
from pprint import pprint
# Gets things lost in translation
translator = Translator()
def scraggle(z: int, txt: str):
    if z < 2:
        z = 2
    if z>20:
        z = 20
    retArray = []
    languages = []
    offLimits = ["en", "zh-CN"]
    language = random.choice(list(googletrans.LANGUAGES.keys()))
    offLimits.append(language)
    try:
        x = translator.translate(txt, dest = language)
        offLimits.append(language)
    except KeyError:
        print("Try different text")
        scraggle(z)
    try: 
        og = googletrans.LANGUAGES[translator.detect(x.text).lang].capitalize()
    except KeyError:
        language = random.choice(list(googletrans.LANGUAGES.keys()))
        while language == 'zh-CN' or language == 'zh-TW':
            language = random.choice(list(googletrans.LANGUAGES.keys()))
        try: 
            og = googletrans.LANGUAGES[translator.detect(x.text).lang].capitalize()
        except KeyError:
            language = random.choice(list(googletrans.LANGUAGES.keys()))
    src = googletrans.LANGUAGES[language].capitalize()
    item = f"\nEnglish -> {src}<br/>"
    languages.append(item)
    item+=f"{x.origin} -> {x.text}\n"
    retArray.append(item)
    for i in range(z-1):
        language = random.choice(list(googletrans.LANGUAGES.keys()))
        while language in offLimits or language == 'zh-CN' or language == "chinese (simplified)"or language not in googletrans.LANGUAGES.keys() or language == 'zh-TW':
            language = random.choice(list(googletrans.LANGUAGES.keys()))
        offLimits.append(language)
        try: 
            og = googletrans.LANGUAGES[translator.detect(x.text).lang].capitalize()
        except KeyError:
            language = random.choice(list(googletrans.LANGUAGES.keys()))
            og = googletrans.LANGUAGES[translator.detect(x.text).lang].capitalize()
        x = translator.translate(x.text, dest=language)
        src = googletrans.LANGUAGES[language].capitalize()

        item = f"{og} -> {src}<br/>"
        languages.append(item)

        #time.sleep(0.5)
        item+=f"{x.origin} -> {x.text}<br/>"

        engVer = translator.translate(x.text, dest="en")
        item+=f"English version: {engVer.text}\n"
        retArray.append(item)
    try: 
        og = googletrans.LANGUAGES[translator.detect(x.text).lang].capitalize()
    except KeyError:
        og = "Chinese"
    x = translator.translate(x.text, dest="en")
    print("GOT HERE")
    item = f"{og} -> English<br/>"
    languages.append(item)

    #time.sleep(0.5)
    item+=f"{x.origin} -> {x.text}<br/>"
    retArray.append(item)


    #time.sleep(2)
    item=f"\n\nOriginal: {txt}<br/>Scrambled: {x.text}\n"
    retArray.append(item)
    return retArray, languages

if __name__ == "__main__":
    """ print(scraggle("Remy has great white toes", 25)) # increase this number   """
    for x in scraggle(4, "New Magic Wand"):
        print(x)
