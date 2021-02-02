#!/usr/bin/env python3

import glob
import os
from datetime import datetime

MISSING   = 0
AVAILABLE = 1

color = lambda s, c: "\x1b[38;5;{}m{}\x1b[0m".format(c, s)

label = [
    "[ " + color("missing", 9) + " ]",
    "[ " + color("available", 112) + " ]"
]

target_root = "/usr/local/texlive"

target_bin = lambda version: "/usr/local/texlive/{}/bin/x86_64-linux".format(version)

def get_texlive_versions():
    if not os.path.isdir(target_root):
        print("[ERROR] Couldn't find a Tex Live installation on your system!\n")
        exit(1)

    versions = glob.glob(target_root + "/*", recursive=False)

    years = [ str(x) for x in range(2014, datetime.now().year + 1) ]

    basename = os.path.basename
    versions = [ basename(x) for x in versions ]
    versions = [ x for x in versions if x in years ]

    return versions

def print_texlive_tools_status(version):
    if not os.path.isdir(target_bin(version)):
        print("[ERROR] Couldn't find any Tex Live tools on your system!\n")
        exit(1)

    keys = "latexmk pdflatex xelatex lualatex biber bibtex".split()

    dependencies = { key: [ "-", label[MISSING] ] for key in keys }

    for path in glob.glob(target_bin(version) + "/*", recursive=False):
        name = os.path.basename(path)
        if name in keys:
            dependencies[name][0] = path
            dependencies[name][1] = label[AVAILABLE]

    max_key = len(max(keys, key=len))
    max_path = len(max(dependencies.values(), key=lambda x: len(x[0]))[0])

    print("Tex Live {}".format(version))

    space = 2
    indent = 4
    for key in keys:
        path = dependencies[key][0]
        status = dependencies[key][1]
        print(" " * indent + key + " " * (max_key + space - len(key)), end="")
        print(" " * indent + path + " " * (max_path + space - len(path)), end="")
        print(" " * indent + status)


if __name__ == "__main__":
    texlive_versions = get_texlive_versions()
    for version in texlive_versions:
        print_texlive_tools_status(version)
