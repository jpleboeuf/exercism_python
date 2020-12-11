"""
   This module offers a solution to
    the "Word Count" exercise on Exercism.ioo.
"""

import sys
from typing import Dict


def count_words(sentence:str) -> Dict[str, int]:

    def is_ja(string:str, char_pos:int) -> bool:
        """is char at pos a joining apostrophe?"""
        return\
                   ((char_pos-1 >= 0)\
                    and string[char_pos-1].isalnum())\
               and string[char_pos] == "'"\
               and ((char_pos+1 < len(string))
                    and string[char_pos+1].isalnum())

    def add_word_to_count(count:Dict[str, int], word:str):
        word = word.lower()
        count[word] = count.get(word, 0) + 1

    word_count: Dict[str, int] = {}
    cur_word = ""
    for i, c in enumerate(sentence):
        if c.isalnum() or is_ja(sentence, i):
            cur_word += c
        else:
            if cur_word:
                add_word_to_count(word_count, cur_word)
                cur_word = ""
    if cur_word:
        add_word_to_count(word_count, cur_word)
    return word_count


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
