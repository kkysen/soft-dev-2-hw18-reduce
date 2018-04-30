# Khyber Sen and Yuyang Zheng
# SoftDev2 pd7
# K18 -- Reductio ab Absurdum
# 2018-04-30

from __future__ import print_function

import re
from collections import Counter


class WordFrequencies(object):
    
    def __init__(self, path="Dante's Inferno.txt"):
        self.text = open(path).read()
        self.words = re.split("//S+", self.text)
        self.word_frequencies = Counter(self.words)  # type: Counter
        self.num_words = len(self.words)
    
    def most_common_word(self):
        return max(*self.word_frequencies.viewitems(), key=lambda item: item[1])
    
    def word_frequency(self, word):
        return self.word_frequencies[word]
    
    def phrase_frequency(self, phrase):
        return len((" " + self.text + " ").split(phrase)) - 1


def test():
    word_frequencies = WordFrequencies()
    print(word_frequencies.most_common_word())


if __name__ == '__main__':
    test()
