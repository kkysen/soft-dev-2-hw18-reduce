# Khyber Sen and Yuyang Zheng
# SoftDev2 pd7
# K18 -- Reductio ab Absurdum
# 2018-04-30

from __future__ import print_function

import re
from collections import Counter

from typing import List


class WordFrequencies(object):
    
    def __init__(self, path="Dante's Inferno.txt"):
        # type: (str) -> None
        self.text = open(path).read()  # type: str
        # TODO check regex
        self.words = re.split("//S+", self.text)  # type: List[str]
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
        return len((" " + self.text + " ").split(phrase)) - 1
    
    def words_frequency(self, words):
        # type: (List[str]) -> int
        return sum(self.word_frequencies[word] for word in words)


def test():
    word_frequencies = WordFrequencies()
    print(word_frequencies.most_common_word())


if __name__ == '__main__':
    test()
