#!/usr/bin/env python3

import glob
import os

color = lambda s, c: "\x1b[38;5;{}m{}\x1b[0m".format(c, s)

MISSING   = 0
AVAILABLE = 1

label = [
    "[ " + color("missing", 9) + " ]",
    "[ " + color("available", 112) + " ]"
]

def get_texlive_vesions():
    files = glob.glob("/usr/local/texlive/*", recursive=False)
    basename = os.path.basename
    normpath = os.path.normpath
    files = [ basename(x) for x in files ]
    files = [ x for x in files if x.isdigit() ]

if __name__ == "__main__":
    keys = "latexmk pdflatex xelatex lualatex biber bibtex".split()

    dependencies = { key: [ "-", label[MISSING] ] for key in keys }

    for path in glob.glob("/usr/local/texlive/2020/bin/x86_64-linux/*", recursive=False):
        name = os.path.basename(path)
        if name in keys:
            dependencies[name][0] = path
            dependencies[name][1] = label[AVAILABLE]

    max_key = len(max(keys, key=len))
    max_path = len(max(dependencies.values(), key=lambda x: len(x[0]))[0])

    space = 2

    for key in keys:
        path = dependencies[key][0]
        status = dependencies[key][1]
        print(key + " " * (max_key + space - len(key)), end="")
        print(path + " " * (max_path + space - len(path)), end="")
        print(status)
