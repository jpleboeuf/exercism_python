"""
   This module offers a solution to
    the "Matrix" exercise on Exercism.io.
"""

import array
import sys
from typing import List


class Matrix:
    """
    Matrix represents a m-by-n matrix.

    Indices start at 1.
    A Matrix is implemented as a list of arrays.
    """

    def __init__(self, matrix_string: str):
        self._m:List[array] = list()
        for matrix_row in matrix_string.split('\n'):
            m_i = array.array('q')  # signed long long
            for matrix_ij in matrix_row.split(' '):
                m_i.append(int(matrix_ij))
            self._m.append(m_i)

    def __str__(self):
        return str([ m_i.tolist() for m_i in self._m ])

    def row(self, index: int) -> List[int]:
        return self._m[index-1].tolist()

    def column(self, index: int) -> List[int]:
        return [ m_i[index-1] for m_i in self._m ]


def main():
    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]
    if argn_cmd >= 1:
        matrix = Matrix(argv_cmd[0].replace("\\n", '\n'))
        print("matrix = " + str(matrix))
        for i in range(3):
            print(f"row({i}) = " + str(matrix.row(i)))
        for j in range(3):
            print(f"column({j}) = " + str(matrix.column(j)))


if __name__ == '__main__':
    main()
