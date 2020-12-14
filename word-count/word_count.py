"""
   This module offers a solution to
    the "Word Count" exercise on Exercism.io.
"""

import sys

import string
from typing import Dict as DictType
from collections import Counter
from typing import Counter as CounterType


def count_words(sentence:str) -> DictType[str, int]:

    word_count:CounterType[str] = Counter()
    punctuation = string.punctuation.replace("'", "")
    sentence_cleaned = sentence.translate(\
            str.maketrans(punctuation, " " * len(punctuation)))
    for word in [w_stripped.lower()\
            for w in sentence_cleaned.split() if (w_stripped := w.strip("'"))]:
        word_count.update([word])
    return dict(word_count)


def main():
    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]
    if argn_cmd == 1:
        for w, c in count_words(argv_cmd[0]).items():
            print(f"{w}: {c}")
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} sentence")

if __name__ == '__main__':
    main()
