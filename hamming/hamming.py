"""
   This module offers a solution to
    the "Hamming" exercise on Exercism.io.
"""

import sys


def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("sequences not of equal length")
    return len([np for np in zip(strand_a, strand_b) if np[0] != np[1]])


def main():
    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]
    if argn_cmd == 2:
        # pylint: disable=unbalanced-tuple-unpacking
        dna_strand_a, dna_strand_b = argv_cmd
        print(f"Hamming distance = {distance(dna_strand_a, dna_strand_b)}")
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} dna_strand_a dna_strand_b")

if __name__ == '__main__':
    main()
