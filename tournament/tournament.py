"""
   This module offers a solution to
    the "Tournament" exercise on Exercism.io.
"""

import sys
from collections import defaultdict
from typing import List, DefaultDict, Final


def parse_results(rows:List[str]) -> DefaultDict[str, List[int]]:
    results: DefaultDict[str, List[int]] = defaultdict(list)
    for row in rows:
        r_e:str = row.split(";")
        t_1:List[int] = results[r_e[0]]
        t_2:List[int] = results[r_e[1]]
        if r_e[2] == "draw":
            t_1.append(1)
            t_2.append(1)
        elif r_e[2] == "win":
            t_1.append(3)
            t_2.append(0)
        elif r_e[2] == "loss":
            t_1.append(0)
            t_2.append(3)
    return dict(sorted(results.items(),
        key=lambda item: (-sum(item[1]), item[0].upper())))

def gen_table(results:DefaultDict[str, List[int]]) -> List[str]:
    # typing.Final not supported by pylint at this time
    #  https://github.com/PyCQA/pylint/issues/3197
    table_format:Final[str] = (  # pylint: disable=unsubscriptable-object
        "{0: <30} | {1: >2} | {2: >2} | {3: >2} | {4: >2} | {5: >2}" )
    table:List[str] = [table_format.format("Team", "MP", "W", "D", "L", "P")]
    for t_name, t_points in results.items():
        table.append(table_format.format(
                    t_name,
                    len(t_points),
                    len([p for p in t_points if p == 3]),
                    len([p for p in t_points if p == 1]),
                    len([p for p in t_points if p == 0]),
                    sum(t_points),
                )
            )
    return table

def tally(rows:List[str]) -> List[str]:
    return gen_table(parse_results(rows))


def main():
    argn_cmd = len(sys.argv)-1
    argv_cmd = sys.argv[1:]

    if argn_cmd >= 1:
        for table_line in tally(argv_cmd):
            print(table_line)
    else:
        raise SystemExit(
            f"Usage: {sys.argv[0]} result... {{enclosed in doublequotes}}")

if __name__ == '__main__':
    main()
