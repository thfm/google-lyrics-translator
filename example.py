import translator as t

LYRICS = input("Enter your lyrics: ")
LANG_COUNT = int(input("How many languages would you like to translate to? "))

print("Translating... (this may take a while)")
print(t.translate_lyrics(LYRICS, LANG_COUNT))
