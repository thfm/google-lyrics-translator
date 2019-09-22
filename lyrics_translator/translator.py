from googletrans.constants import LANGUAGES
from googletrans import Translator

# All languages available for Google Translate
languages = list(LANGUAGES.keys())

t = Translator()


# Translates the given lyrics through 'count' different languages before 
# returning to English
def translate_lyrics(lyrics, count = 35):
    # Check that the given 'count' does not exceed the amount of languages
    if count > len(languages):
        print("[ERROR]: The 'count' argument exceeds the amount of available"
            + " languages for translation.")
        return None

    # Go through the first 'count' languages in the list
    for language in languages[:count]:
        # Translate the lyrics to the current language
        lyrics = t.translate(lyrics, src = "auto",
            dest = language).text
    # Finally, translate the lyrics back to English
    return t.translate(lyrics, dest = "en").text
