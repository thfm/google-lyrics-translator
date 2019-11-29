from googletrans.constants import LANGUAGES
from googletrans import Translator

# All languages available for Google Translate
LANGUAGES_LIST = list(LANGUAGES.keys())

T = Translator()


# Translates the given lyrics through 'count' different languages before
# returning to English
def translate_lyrics(lyrics, count=35):
    # Check that the given 'count' does not exceed the amount of languages
    if count > len(LANGUAGES_LIST):
        print("[ERROR]: The 'count' argument exceeds the amount of available"
              + " languages for translation.")
        return None

    # Go through the first 'count' languages in the list
    for language in LANGUAGES_LIST[:count]:
        # Translate the lyrics to the current language
        lyrics = T.translate(lyrics, src="auto",
                             dest=language).text
    # Finally, translate the lyrics back to English
    return T.translate(lyrics, dest="en").text
