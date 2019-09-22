import lyrics_translator.translator as t

# From Elton John's "Your Song"
lyrics = """
It's a little bit funny this feeling inside
I'm not one of those who can easily hide, I
Don't have much money but boy if I did
I'd buy a big house where we both could live
If I was a sculptor, but then again no
Or a man who makes potions in a traveling show
Oh I know it's not much but it's the best I can do
My gift is my song
And this one's for you.
"""

print(t.translate_lyrics(lyrics))
