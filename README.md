# Google Lyrics Translator

A fun little program that destroys the lyrics of your favourite songs by using Google Translate.

## First, a warning …

This repository is centred around a library called 'googletrans', which is not authorised by Google, and so may be blocked or removed at any time.

## Download and installation

To start translating the lyrics of your choice into gibberish, you will need to:

1. Download and extract the source code of this repository
2. Navigate to the downloaded folder using a shell. Ensure that this folder contains the ```setup.py``` file
3. Install the CLI through PIP: ```pip install .```

If the installation was successful, you should be able to run ```translate --help``` in the command line, from any location, with no errors.

## Usage

### The basics

This program works by translating the given lyrics into a number of different languages, before returning back to English.

As an example, run the ```translate``` command, with a single string as it's argument:

```translate "We are the champions, my friends"```

After a while, the interface will print the translated result (note that this can take some time).

### Sourcing from files

You can optionally have the translator source lyrics from a file. To do this, use the ```-f``` flag, followed by the path to the file:

```translate -f "lyrics/Your Song.txt"```

### Adjusting the language count

As specified earlier, the program translates text through a number of different languages. You can adjust this number, called the 'count', by supplying an integer value after ```-c``` in a translation command:

```translate "Hello? It's me." -c 15```

The higher the count, the less sense the resulting text will make. Higher counts will also take longer to translate.

### Finally …

If at any point you get stuck on the usage of this tool, you can run ```translate --help``` to see the command options with their corresponding descriptions.
