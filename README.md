# English Vocabulary speedrun

This program does the tedious English Vocabulary task for you.
#### WARNING: It does not generate "your own sentence" required in the task. You have to do it by hand :(

Requires Internet connection to parse https://dictionary.cambridge.org

## Usage
`./Vocab.py [-i] [-c] ARTICLE_NAME.pdf [-o OUTPUT_FILE] WORD_1 WORD_2 WORD_3...`
```
-i is interactive mode. It will split the file into words and ask you if you want to use each of them.
-c counts the number of definitions present in file. Usefull when running the script several times.
-o lets you specify the output file. If not specified, stdout will be used.
```

When prompted for words, you have 4 options:
```
y - Use the word.
    Will print it to the file with all the info.

m - Modify the word and use it.
    Use it in case a cropped or distorted version of a word is showing. Note that it will most likely not be found in the article.

q - quit the program.

Any other button - skip the word and continue.
```

## Run example
```
$ ./Vocab.py ../dvornik2019.pdf -i -o output.txt -c
Warning! Check the output file after using the program! May contain artifacts
Number of defined words:  0
Do you want to use the word "much" (y/m - modify and use/n/q - quit):
```

## Output example
```
"luminosity":
Definition:
     the state of producing or reflecting bright light; the state of appearing to shine
Dictionary example:
     The photographer achieved the luminosity in the image through careful manipulation in the darkroom.
Example from article:
     The most obvious one is studying the group properties as a function of halo mass, where using the two-dimensional method can give better constraints on scaling relations of group halo mass with luminosity of central galaxies, their stellar mass, size, X-ray gas emission, and the concentration of such haloes.
```

Also check out test.txt file. This is test run on a Virtio documentation.
