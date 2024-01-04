import string

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist

from collections import Counter

ulysses = open("tesr/ulysses.txt", "r") 
text = ulysses.read()

nltk.download("stopwords")
sw_set = set(stopwords.words("english"))
punct_set = set(string.punctuation)

tokens = word_tokenize(text)
clean_text = [t for t in tokens if t not in sw_set and t not in punct_set]
print(clean_text[:20])