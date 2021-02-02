#!/usr/bin/env python3

import glob
import os

RED = 9
GREEN = 112

color = lambda s, c: "\033[38;5;{}m{}\033[0m".format(c, s)

def get_texlive_vesions():
    files = glob.glob("/usr/local/texlive/*", recursive=False)
    basename = os.path.basename
    normpath = os.path.normpath
    files = [ basename(x) for x in files ]
    files = [ x for x in files if x.isdigit() ]

if __name__ == "__main__":
    keys = "latexmk pdflatex xelatex lualatex biber bibtex".split()
    dependencies = { key: [ "-", "[ " + color("missing", RED) + " ]" ] for key in keys }

    for path in glob.glob("/usr/local/texlive/2018/bin/x86_64-linux/*", recursive = False):
        name = os.path.basename(path)
        if name in keys:
            dependencies[name][0] = path
            dependencies[name][1] = "[ " + color("available", GREEN) + " ]"

    maxl_name = len(max(keys, key=len))
    maxl_path = len(max(dependencies.values(), key=lambda x: len(x[0]))[0])

    space = 2

    for key in keys:
        path = dependencies[key][0]
        is_available = dependencies[key][1]
        print(key + " " * (maxl_name + space - len(key)), end="")
        print(path + " " * (maxl_path + space - len(path)), end="")
        print(is_available)
