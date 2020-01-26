import click

from googletrans.constants import LANGUAGES
from googletrans import Translator

# Keep only short versions of language names
LANGUAGES = list(LANGUAGES.keys())
NUM_LANGUAGES = len(LANGUAGES)

T = Translator()

@click.command()
@click.argument("source")
@click.option("-f", "--file", "is_file",
              is_flag=True,
              help="Use the contents of a file as the lyrics source.")
@click.option("-c", "--count", "lang_count",
              help="The number of languages to translate to before " +
              "returning to English.",
              default=35)
def translate_lyrics(source, is_file, lang_count):
    lyrics = open(source).read() if is_file else source
    if lang_count > NUM_LANGUAGES:
        print(f"[WARNING]: Given language count ({lang_count}) exceeds " +
              f"maximum number of languages ({NUM_LANGUAGES})")
        lang_count = NUM_LANGUAGES
        print(f"[INFO]: Using all languages for translation")

    print("Translating... (this may take a while)")
    for language in LANGUAGES[:lang_count]:
        lyrics = T.translate(lyrics, dest=language).text
    print(T.translate(lyrics, dest="en").text)
