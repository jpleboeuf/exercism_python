"""
   This module offers a solution to
    the "Markdown" exercise on Exercism.io.
"""

import re

def parse(markdown:str) -> str:
    """parses the markdown string with Markdown syntax
        and returns the associated HTML for that string"""

    def parse_header(txt:str) -> str:
        """parses header elements h6/h2/h1"""
        if re.match('###### (.*)', txt) is not None:
            txt = '<h6>' + txt[7:] + '</h6>'
        elif re.match('## (.*)', txt) is not None:
            txt = '<h2>' + txt[3:] + '</h2>'
        elif re.match('# (.*)', line) is not None:
            txt = '<h1>' + txt[2:] + '</h1>'
        return txt

    def parse_fe(txt:str) -> str:
        """parses formatting elements strong/em"""
        strong_mo = re.match('(.*)__(.*)__(.*)', txt)
        if strong_mo:
            txt = strong_mo.group(1) + '<strong>' + \
                  strong_mo.group(2) + '</strong>' + \
                  strong_mo.group(3)
        em_mo = re.match('(.*)_(.*)_(.*)', txt)
        if em_mo:
            txt = em_mo.group(1) + '<em>' + \
                  em_mo.group(2) + '</em>' + \
                  em_mo.group(3)
        return txt

    def parse_p(txt:str) -> str:
        """parses paragraph elements p"""
        t_mo = re.match('<h|<ul|<li|<p', txt)
        if not t_mo:
            txt = '<p>' + txt + '</p>'
        txt = parse_fe(txt)
        return txt

    in_list = False
    in_list_append = False

    def list_open(txt:str='') -> str:
        """opens a list with <ul>"""
        nonlocal in_list
        in_list = True
        txt = txt + '<ul>'
        return txt

    def list_close(txt:str='') -> str:
        """closes a list with </ul>"""
        nonlocal in_list_append
        txt = '</ul>' + txt
        in_list_append = False
        return txt

    def parse_list(txt:str) -> str:
        """parses list elements li (ul)"""
        nonlocal in_list, in_list_append
        li_mo = re.match(r'\* (.*)', txt)
        if li_mo:
            txt = ''
            if not in_list:
                txt = list_open(txt)
            li_ct = li_mo.group(1)
            li_ct = parse_fe(li_ct)
            txt += '<li>' + li_ct + '</li>'
        else:
            if in_list:
                in_list = False
                in_list_append = True
        return txt

    html = ''
    md_lines = markdown.split('\n')
    for line in md_lines:
        line = parse_header(line)
        line = parse_list(line)
        line = parse_p(line)
        if in_list_append:
            line = list_close(line)
        html += line
    if in_list:
        html += list_close()
    return html
