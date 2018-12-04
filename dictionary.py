""" 
    Command Line Interface Dictionary
    Enter a word, and the dictionary will provide you with the 
    definition of the word you entered. This dictionary contains
    the definitions for over 49 000 English words.
    

    Written by James Roberts
"""
import json
from difflib import get_close_matches

words = json.load(open("words.json","r"))

def define(w):
    w = w.lower()
    if w in words:
        return words[w]
    similar_words = get_close_matches(w, words.keys())
    if len(similar_words > 0):
        response = input("Did you mean %s instead? Enter Y if yes, or N if no: " % similar_words[0])
        if response == "Y" or response == "y":
            return words[similar_words[0]]
        else:
            return "We couldn't find anything for that word. Please try another one."
    else: 
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = define(word)
# For multiple definitions print each one
if type(output) == list:
    for definition in output:
        print(definition)
# Otherwise print the single definition string that was returned
else:
    print(output)


