from googletrans.constants import LANGUAGES
from googletrans import Translator

# Keep only short versions of language names
LANGUAGES = list(LANGUAGES.keys())
NUM_LANGUAGES = len(LANGUAGES)

T = Translator()


def translate_lyrics(lyrics, lang_count=35):
    if lang_count > NUM_LANGUAGES:
        print(f"[WARNING]: Given language count ({lang_count}) exceeds " +
              f"maximum number of languages ({NUM_LANGUAGES})")
        lang_count = NUM_LANGUAGES
        print(f"[INFO]: Using all languages for translation")

    for language in LANGUAGES[:lang_count]:
        lyrics = T.translate(lyrics, dest=language).text
    return T.translate(lyrics, dest="en").text
