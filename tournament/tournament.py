"""
   This module offers a solution to
    the "Tournament" exercise on Exercism.io.
"""

import sys
from typing import Final, Literal, cast
from typing import List
from typing import Tuple, NamedTuple
from typing import Dict, DefaultDict


TeamPoints = DefaultDict[str, List[int]]

def parse_results(rows:List[str]) -> TeamPoints:
    """loads the input into a point history for each team"""
    # pylint: disable=inconsistent-quotes
    # typing.Literal does not seem to be supported by pylint at this time
    MatchOutcome = Literal[  # pylint: disable=unsubscriptable-object
        "draw", "win", "loss"]
    Match = NamedTuple('Match', [
            ('team_1', str),
            ('team_2', str),
            ('outcome', MatchOutcome)
        ])
    def new_match(match_elems: List[str]) -> Match:
        assert len(match_elems) == 3
        assert match_elems[2] in ["draw", "win", "loss"]
        return Match(match_elems[0], match_elems[1],
            cast(MatchOutcome, match_elems[2]))
    # typing.Final not supported by pylint at this time
    #  https://github.com/PyCQA/pylint/issues/3197
    outcome_points: Final[Dict[  # pylint: disable=unsubscriptable-object
            MatchOutcome,
            Tuple[int, int]
        ]] = {"draw": (1, 1), "win": (3, 0), "loss": (0, 3)}
    # pylint: enable=inconsistent-quotes
    points: TeamPoints = TeamPoints(list)
    for row in rows:
        match = new_match(row.split(";"))
        for team_i, team in enumerate(match[:2]):
            ( points[team]  # pylint: disable=unsubscriptable-object
                .append(outcome_points[match.outcome][team_i]) )
    return points

TallyDataKey = Literal[  # pylint: disable=unsubscriptable-object
    "MP", "W", "D", "L", "P"]
TallyData = Dict[str, Dict[TallyDataKey, int]]

def process_points(points:TeamPoints) -> TallyData:
    """generates the tally data from the point history of each team"""
    tally_data: TallyData = dict()
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
    def safely_cast_str_to_ttd_key(ttd_key:str) -> TallyDataKey:
        assert ttd_key in ["MP", "W", "D", "L", "P"]
        return cast(TallyDataKey, ttd_key)
    table_format:Final[str] = (  # pylint: disable=unsubscriptable-object
        "{0: <30} | {1: >2} | {2: >2} | {3: >2} | {4: >2} | {5: >2}" )
    table:List[str] = [table_format.format(*table_column_names)]
    for team_name, team_td in tally_data.items():
        table.append(table_format.format(team_name,
            *[team_td[safely_cast_str_to_ttd_key(ttd_key)]
                for ttd_key in table_column_names[1:]]))
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
