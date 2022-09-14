import re
from typing import Any
import nltk
from nltk.stem.snowball import SnowballStemmer
import numpy as np

stemmer = SnowballStemmer('english')

def tokenize(sentence: str):
    return nltk.word_tokenize(sentence)

def stem(word: str):
    return stemmer.stem(word.lower())
# text -> tokenized sentence
def bag_of_words(text, all_words):
    tokenized_text = [stem(w) for w in text]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for i, w in enumerate(all_words):
        if w in tokenized_text:
            bag[i] = 1.0
    return bag
