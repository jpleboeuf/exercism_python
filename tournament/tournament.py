"""
   This module offers a solution to
    the "Tournament" exercise on Exercism.io.
"""

import sys
from typing import List, DefaultDict, Final
from typing import NamedTuple


def parse_results(rows:List[str]) -> DefaultDict[str, List[int]]:
    # pylint: disable=inconsistent-quotes
    Match = NamedTuple('Match',
        [('team_1', str), ('team_2', str), ('outcome', int)])
    # pylint: enable=inconsistent-quotes
    results: DefaultDict[str, List[int]] = DefaultDict(list)
    for row in rows:
        match = Match(*row.split(";"))
        t_1:List[int] = results[match.team_1]
        t_2:List[int] = results[match.team_2]
        if match.outcome == "draw":
            t_1.append(1)
            t_2.append(1)
        elif match.outcome == "win":
            t_1.append(3)
            t_2.append(0)
        elif match.outcome == "loss":
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

if __name__ == '__main__':  # pylint: disable=inconsistent-quotes
    main()
