"""
   This module offers a solution to
    the "Word Count" exercise on Exercism.io.
"""

import sys
from typing import Dict

from collections import namedtuple
from types import SimpleNamespace


def count_words(sentence:str) -> Dict[str, int]:

    CursorWindow = namedtuple('CursorWindow', ['prev', 'curr', 'next'])

    def is_ja(cw:CursorWindow) -> bool:
        """is the current char a joining apostrophe?"""
        return cw.prev.isalnum() and cw.curr == "'" and cw.next.isalnum()

    word_count: Dict[str, int] = {}
    cursor = SimpleNamespace()
    cursor.pos = -1
    word = SimpleNamespace()
    word.w = ""
    word.built = False
    while cursor.pos+1 < (len_s := len(sentence)):
        cursor.pos += 1
        cursor.win = CursorWindow(*[\
                sentence[cursor.pos-1] if cursor.pos-1 >= 0    else 'BEGIN>',\
                sentence[cursor.pos],\
                sentence[cursor.pos+1] if cursor.pos+1 < len_s else '<END'\
            ])
        if cursor.win.curr.isalnum() or is_ja(cursor.win):
            word.w += cursor.win.curr.lower()
        else:
            if word.w: word.built = True
        if word.built or (word.w and cursor.win.next == '<END'):
            word_count[word.w] = word_count.get(word.w, 0) + 1
            word.w = ""
            word.built = False
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
