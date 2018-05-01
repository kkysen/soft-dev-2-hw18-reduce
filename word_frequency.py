# Khyber Sen and Yuyang Zhang
# SoftDev2 pd7
# K18 -- Reductio ab Absurdum
# 2018-04-30

from __future__ import print_function

import re
from collections import Counter

from functools import reduce

from typing import List, Tuple


# Polyfills using reduce

def sum(iterable):
    return reduce(lambda a, b: a + 1, iterable, 0)


def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    return reduce(lambda a, b: a if key(a) > key(b) else b, args)


class WordFrequencies(object):

    def __init__(self, path="Dante's Inferno.txt"):
        # type: (str) -> None
        self.text = open(path).read()  # type: str
        # blacklist = "[ \n\r\t.,;:?!\"/\\\{}[\\]()]*"
        whitelist = "[a-zA-Z-]+"
        self.words = re.findall(whitelist, self.text.lower())  # type: List[str]
        self.word_frequencies = Counter(self.words)  # type: Counter[str]
        self.num_words = len(self.words)  # type: int

    def most_common_word(self):
        # type: () -> str
        return max(*self.word_frequencies.viewitems(), key=lambda item: item[1])[0]

    def word_frequency(self, word):
        # type: (str) -> int
        return self.word_frequencies[word]

    def phrase_frequency(self, phrase):
        # type: (str) -> int
        return sum(1 for _ in re.finditer(phrase, self.text))

    def words_frequency(self, words):
        # type: (List[str]) -> int
        return sum(self.word_frequencies[word] for word in words)

    def frequency_order(self, reverse=False):
        # type: () -> List[Tuple[str, int]]
        return sorted(self.word_frequencies.viewitems(), key=lambda x: x[1], reverse=reverse)


def test():
    word_frequencies = WordFrequencies()
    map(print, word_frequencies.frequency_order())
    print(word_frequencies.most_common_word())
    # print(re.split("[ \n\r\t.,;:?!\"/\\\{}[\\]()]*", "  hello   world "))
    print(word_frequencies.phrase_frequency("Project Gutenberg"))
    print(word_frequencies.phrase_frequency("Dante"))
    print(word_frequencies.phrase_frequency("he is"))
    print(word_frequencies.phrase_frequency("He is"))



if __name__ == '__main__':
    test()
