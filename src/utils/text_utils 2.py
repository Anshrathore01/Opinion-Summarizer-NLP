from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re

ps = PorterStemmer()

def stem_text(text):
    if not text:
        return ""
    tokens = word_tokenize(text)
    return " ".join(ps.stem(t) for t in tokens)
