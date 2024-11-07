from deep_translator import GoogleTranslator
import random


def scraggle(z: int, txt: str):
    if z < 2:
        z = 2
    if z > 20:
        z = 20
    retArray = []
    languages = []
    offLimits = ["en", "zh-cn", "zh-tw"]

    # Create an instance of GoogleTranslator
    translator = GoogleTranslator()
    language_list = translator.get_supported_languages(as_dict=True)

    # Select a random language for the first translation
    language = random.choice(list(language_list.keys()))
    while language in offLimits:
        language = random.choice(list(language_list.keys()))
    offLimits.append(language)

    # Translate from English to the chosen language
    x = GoogleTranslator(source="en", target=language).translate(txt)
    item = f"English -> {language.capitalize()}\n{x}\n"
    retArray.append(item)
    prevLanguage = language
    prevSentence = x
    # Apply additional translations for the 'scraggle' effect
    for _ in range(z - 1):
        language = random.choice(list(language_list.keys()))
        while language in offLimits:
            language = random.choice(list(language_list.keys()))
        offLimits.append(language)

        # Translate text to the chosen language and back to English
        x = GoogleTranslator(source=prevLanguage, target=language).translate(txt)
        back_to_english = GoogleTranslator(source=language, target="en").translate(x)

        item = f"{prevLanguage.capitalize()}: {prevSentence}\n\n{language.capitalize()}: \n{x}\n\nEnglish:{back_to_english}\n"
        retArray.append(item)
        prevLanguage = language
        prevSentence = x
    return retArray, languages
