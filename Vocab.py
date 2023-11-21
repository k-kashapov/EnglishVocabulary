#! python3

import sys

if len(sys.argv) <= 2:
    print("USAGE: ./Vocab.py [-i] [-c] ARTICLE_NAME.pdf [-o OUTPUT_FILE] WORD_1 WORD_2 WORD_3...")
    print("\t-i is interactive mode")
    print("\t-c counts the number of definitions present in file. Usefull when running the script several times")

    exit(1)

import requests
from bs4 import BeautifulSoup
import fitz # pip install PyMuPDF
import random
import getch # pip install getch
import re

def process_word(word, output_file):
    url = 'https://dictionary.cambridge.org/dictionary/english/' + word
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    headers = {'User-Agent': user_agent}
    web_request = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_request.text, "html.parser")

    definition = soup.find("div", {"class": "def ddef_d db"})
    if not definition:
        print(f"Word {word} not found in the dictionary!")
        exit(-1)

    examples = soup.find_all("div", {"class": "examp dexamp"})
    
    if not examples:
        print(f"Word {word} not found in the dictionary!")
        exit(-1)

    print(f"\n\"{word}\":", file=output_file)
    print("Definition:", file=output_file)
    print("\t", definition.get_text()[:-2], file=output_file)
    print("Dictionary example:", file=output_file)
    print("\t", examples[0].get_text().lstrip(' '), file=output_file)

    # for ex in examples:
    #     print("\t", ex.get_text().lstrip(' '))

    print("Example from article:", file=output_file)

    present = False
    for sentence in sentences:
        if word in sentence:
            print("\t", (sentence.replace('\n', ' ') + '.').lstrip(' ').replace('- ', ''), file=output_file)
            present = True
            break

    if not present:
        print(f"Word \"{word}\" not found in article!")
        return

    print(file=output_file)

def find_element_in_list(element, list_element):
    try:
        index_element = list_element.index(element)
        return index_element
    except ValueError:
        return None

print("Warning! Check the output file after using the program! May contain artifacts")

interactive = False
if '-i' in sys.argv:
    interactive = True

output = find_element_in_list('-o', sys.argv)
output_file = None
if output:
    if len(sys.argv) < output + 2:
        print("ERROR: Output file should be specified after the -o flag")
        exit(-1)
    output_file = open(sys.argv[output + 1], "a+")
    
    if '-c' in sys.argv:
        output_file.seek(0)
        previous_text = output_file.read()
        print("Number of defined words: ", previous_text.count("Definition"))

file_name = sys.argv[1]

doc = fitz.open(file_name)
text = ""
for page in doc:
    text += page.get_text()

sentences = text.split('.')

words = []
if interactive:
    words = set(text.replace('\n', ' ').split(' '))
    for raw_word in words:
        word = re.sub('[^a-zA-Z]+', '', raw_word)
        if not word:
            continue

        string = f"\rDo you want to use the word \"{word}\" (y/m - modify and use/n/q - quit): "
        print(string, end="")
        key = getch.getch()
        if key == 'y':
            process_word(word, output_file)
        elif key == 'm':
            print("Enter the word you want to look up:")
            word = input()
            process_word(word, output_file)
        elif key == 'q':
            print("Quitting...")
            break
        print("\r" + " " * len(string), end='\r')
else:
    words = sys.argv[2:]
    for word in words:
        process_word(word, output_file)
