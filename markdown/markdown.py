"""
   This module offers a solution to
    the "Markdown" exercise on Exercism.io.
"""

import re

HEADER_RE = re.compile(r"(#{6}|#{2}|#{1}) (.*)")
STRONG_RE = re.compile(r"__(.*?)__")
EM_RE = re.compile(r"_(.*?)_")
LIST_RE = re.compile(r"\* (.*)")

def parse(markdown:str) -> str:
    """parses the markdown string with Markdown syntax
        and returns the associated HTML for that string"""

    html = ''

    def parse_header(header_mo:re.Match) -> str:
        """parses header elements h6/h2/h1"""
        header_level = len(header_mo.group(1))
        header_content = header_mo.group(2)
        return f"<h{header_level}>{header_content}</h{header_level}>"

    def parse_fe(txt:str) -> str:
        """parses formatting elements strong/em"""
        txt = STRONG_RE.sub(r"<strong>\1</strong>", txt)
        txt = EM_RE.sub(r"<em>\1</em>", txt)
        return txt

    def parse_p(txt:str) -> str:
        """parses paragraph elements p"""
        return '<p>' + txt + '</p>'

    in_list = False

    def parse_list(li_mo:re.Match) -> str:
        """parses list elements li (ul)"""
        nonlocal html
        nonlocal in_list
        txt = ''
        if in_list:
            html = html[:-5]
        else:
            in_list = True
            txt = '<ul>' + txt
        li_ct = li_mo.group(1)
        txt += '<li>' + li_ct + '</li>'
        txt = txt + '</ul>'
        return txt

    md_lines = markdown.splitlines()
    for line in md_lines:
        line = parse_fe(line)
        if header_mo := HEADER_RE.match(line):
            line = parse_header(header_mo)
        elif li_mo := LIST_RE.match(line):
            line = parse_list(li_mo)
        else:
            if in_list:
                in_list = False
            line = parse_p(line)
        html += line
    return html
