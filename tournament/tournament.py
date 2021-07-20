"""
   This module offers a solution to
    the "Tournament" exercise on Exercism.io.
"""

import sys
from typing import Final, Literal
from typing import List
from typing import Tuple, NamedTuple
from typing import Dict, DefaultDict


def parse_results(rows:List[str]) -> DefaultDict[str, List[int]]:
    """loads the input into a point history for each team"""
    # pylint: disable=inconsistent-quotes
    # typing.Literal does not seem to be supported by pylint at this time
    MatchOutcome = Literal[  # pylint: disable=unsubscriptable-object
        "draw", "win", "loss"]
    Match = NamedTuple('Match',
        [
            ('team_1', str),
            ('team_2', str),
            ('outcome', MatchOutcome)
        ])
    # typing.Final not supported by pylint at this time
    #  https://github.com/PyCQA/pylint/issues/3197
    outcome_points:Final[Dict[  # pylint: disable=unsubscriptable-object
            MatchOutcome,
            Tuple[int, int]
        ]] = {"draw": (1, 1), "win": (3, 0), "loss": (0, 3)}
    # pylint: enable=inconsistent-quotes
    points: DefaultDict[str, List[int]] = DefaultDict(list)
    for row in rows:
        match = Match(*row.split(";"))
        for team_i, team in enumerate(match[:2]):
            points[team].append(outcome_points[match.outcome][team_i])
    return points

TallyData = Dict[
    str, Dict[
        Literal[  # pylint: disable=unsubscriptable-object
            "MP", "W", "D", "L", "P"],
        int]]

def process_points(points:Dict[str, List[int]]) -> TallyData:
    """generates the tally data from the point history of each team"""
    tally_data:TallyData = dict()
    for team_name, team_points in points.items():
        tally_data[team_name] = {
                "MP": len(team_points),
                "W":  len([p for p in team_points if p == 3]),
                "D":  len([p for p in team_points if p == 1]),
                "L":  len([p for p in team_points if p == 0]),
                "P":  sum(team_points),
            }
    return dict(sorted(tally_data.items(),
        key=lambda item: (-item[1]["P"], item[0].upper())))

def gen_table(tally_data:TallyData) -> List[str]:
    """generates the tally table for output"""
    table_column_names:Tuple[str, ...] = ("Team", "MP", "W", "D", "L", "P")
    table_format:Final[str] = (  # pylint: disable=unsubscriptable-object
        "{0: <30} | {1: >2} | {2: >2} | {3: >2} | {4: >2} | {5: >2}" )
    table:List[str] = [table_format.format(*table_column_names)]
    for team_name, team_td in tally_data.items():
        table.append(table_format.format(team_name,
            *[team_td[ttd_key] for ttd_key in table_column_names[1:]]))
    return table

def tally(rows:List[str]) -> List[str]:
    return gen_table(process_points(parse_results(rows)))


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
