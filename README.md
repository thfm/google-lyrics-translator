# Google Lyrics Translator

A fun little program that destroys the lyrics of your favourite songs by using Google Translate.

## First, a warning …

This repository is centred around a library called 'googletrans'. This is not authorised by Google, and so may be blocked or removed at any time.

## Download and usage

In order to utilise this repository's functionality, you will need to add the `lyrics_translator` package to the source code of each project you wish to use it in.

Then, simply import the package by calling `import lyrics_translator.translator as t` (or something similar to that). Google Lyrics Translator should now be ready for use!

To translate the lyrics of your choice into AI gibberish, simply type the following:

`print(t.transate_lyrics(<lyrics>))`

This function works by translating the lyrics into a range of different languages before returning back to English. You can optionally specify the amount of languages the function passes the lyrics through by setting the `count` parameter (the default is 35):

`print(t.translate_lyrics(<lyrics>, count = 50))`

If you are still confused as to the usage of this repository, see the `example.py` file for a full example scenario.
