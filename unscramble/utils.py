import itertools
import nltk
from nltk.corpus import words

nltk.download('words')

def unscramble(scrambled_word):
    valid_words = set(words.words())
    permutations = itertools.permutations(scrambled_word)
    unscrambled_words = set(
        [''.join(p) for p in permutations if ''.join(p) in valid_words]
    )
    return unscrambled_words