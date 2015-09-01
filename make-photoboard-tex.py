#!/usr/bin/env python

import argparse
import sys

numcolumns = 23
numrows = 9     # num rows per page, not really relevant if it's all on one page

header = r"""\documentclass{article}

\usepackage{array}
\usepackage{etoolbox}
\usepackage{fix-cm}
\usepackage[landscape, paperwidth=36in, paperheight=60in, top=1cm, bottom=0cm, left=1.5cm, right=1.5cm]{geometry}
\usepackage{graphicx}
\usepackage[none]{hyphenat}
\usepackage[utf8]{inputenc}

\newcolumntype{x}[1]{>{\centering\hspace{0pt}\arraybackslash}p{#1}}

\newcommand{\photosize}{4cm}
\newcommand{\photoheight}{\photosize}
\newcommand{\photowidth}{\photosize}
\newcommand{\rowheight}{5cm}
\newcommand{\insertimage}[1]{\includegraphics[width=\photowidth,height=\photoheight,keepaspectratio]{#1}}
\newcommand{\nophoto}{\insertimage{noun_project_419}}
\newcommand{\photo}[1]{\insertimage{"photos/#1"}}
\newcommand{\name}[1]{#1}
\newcommand{\colwidth}{""" + str(0.9/numcolumns) + r"""\textwidth}

\renewcommand{\arraystretch}{1.5}

% Patch the \includegraphics command to use \nophoto if the specified
% image fails to load
\makeatletter
\patchcmd{\Gin@ii}
  {\begingroup}% <search>
  {\begingroup\renewcommand{\@latex@error}[2]{\nophoto}}% <replace>
  {}% <success>
  {}% <failure>
\makeatother

\begin{document}
\pagestyle{empty}

\begin{center}
\fontsize{64}{76}\selectfont
Your Title Here

\vspace{1cm}

\fontsize{24}{28}\selectfont
"""

footer = r"""

\fontsize{14}{16}\selectfont
User icon from The Noun Project, available under a Creative Commons Attribution 3.0 Unported license

\end{center}
\end{document}"""

def chunk(l, n):
    """ Creates n-sized chunks from l.
    """
    return [l[pos:pos + n] for pos in range(0, len(l), n)]

def photo(person):
    s = ""
    s += r"\photo{" + person + r"}"
    return s

def name(person):
    return r"\name{" + person + r"}"

def print_people(title, people, colwidth):
    print(r"\vspace{0.8cm}")
    print(r"")
    print(r"\fontsize{64}{76}\selectfont")
    print(title)
    print(r"")
    print(r"\vspace{0.8cm}")
    print(r"")
    print(r"\fontsize{24}{28}\selectfont")

    columns = [[] for i in range(numcolumns)]
    for i, person in enumerate(people):
        columns[i % numcolumns].append(person)

    rows = chunk(people, numcolumns)

    for rownum, row in enumerate(rows):
        if rownum % numrows == 0:
            print(r"  \begin{tabular}{" + (r"x{" + str(colwidth) + r"\textwidth}") * numcolumns + r"}")

        for command in [photo, name]:
            if command == photo:
                print(r"\rule{0cm}{\rowheight}")

            for i, person in enumerate(rows[rownum]):
                if command == photo:
                    if len(person.split('[')) > 1:
                        person = person.split('[')[1].split(']')[0]
                else:
                    if len(person.split('[')) > 1:
                        person = person.split('[')[0]
                ending = r"&" if i < len(row) - 1 else r"\\"
                print("    " + command(person) + " " + ending)

        if (rownum+1) % numrows == 0 or rownum == len(rows) - 1:
            print(r"  \end{tabular}")

    print(r"")
    print(r"\vspace{0.5cm}")
    print(r"")

def main(argv=None):
    if argv is None:
        argv = sys.argv
    parser = argparse.ArgumentParser(description='Create photoboard.tex')
    args = parser.parse_args()

    print(header)

    groups = [
        ["Group 1", "group1.txt"],
        ["Group 2", "group2.txt"]]

    for group in groups:
        if type(group[0]) is list:
            for subgroup in group:
                print(r"\begin{minipage}{" + str(0.9/(len(group))) + r"\textwidth}")
                print(r"\begin{center}")
                with open(subgroup[1], "r") as f:
                    people = f.read().strip().split('\n')
                    print_people(subgroup[0], people, 0.9 / len(people))
                print(r"\end{center}")
                print(r"\end{minipage}")
        else:
            with open(group[1], "r") as f:
                people = f.read().strip().split('\n')
                print_people(group[0], people, 0.9 / numcolumns)
        print(r"\vspace{2.5cm}")

    print(footer)

if __name__ == "__main__":
    sys.exit(main())
