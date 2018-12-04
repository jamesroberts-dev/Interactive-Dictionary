""" 
    Command Line Interface Dictionary
    Enter a word, and the dictionary will provide you with the 
    definition of the word you entered. This dictionary contains
    the definitions for over 49 000 English words.

    Written by James Roberts
"""
import json

words = json.load(open("words.json","r"))

def define(w):
    w = w.lower()
    if w in words:
        return words[w]
    else: 
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

print(define(word))


 