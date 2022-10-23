#!/usr/bin/env python3

import glob
import os
import re

class Color:
    RED     = 0
    GREEN   = 1

def color(string, key):
    code = { Color.RED: "91", Color.GREEN: "92" }
    return "\x1b[0;{}m{}\x1b[0m".format(code.get(key, "97"), string)

def texlive_releases():
    install_path = "/usr/local/texlive"

    if not os.path.isdir(install_path):
        print("{}: {} does not exist!".format(
              color("ERROR", Color.RED), install_path))
        exit(1)

    releases = []

    for item in glob.glob(install_path + "/*"):
        basename = os.path.basename(item)
        pattern_match = re.match(r"\d{4}", basename)
        if pattern_match:
            releases.append(basename)

    if not releases:
        print("{}: No releases found under {}!".format(
              color("ERROR", Color.RED), install_path))
        exit(1)

    return releases

def contains(haystack, needle, func):
    for item in haystack:
        if func(needle, item):
            return True
    return False

def main():
    releases = texlive_releases()

    required_bins = sorted("latexmk pdflatex xelatex lualatex biber bibtex".split())

    for release in releases:
        print(f"Tex Live {release}")
        print("-" * 79)
        installed_bins = []
        for path in glob.glob(f"/usr/local/texlive/{release}/bin/x86_64-linux/*"):
            name = os.path.basename(path)
            if name in required_bins:
                installed_bins.append(path)
        for name in required_bins:
            if contains(installed_bins, name, lambda x,y: x == os.path.basename(y)):
                print("[ {} ] {}".format(color("OK", Color.GREEN), name))
            else:
                print("[ {} ] {}".format(color("MISSING", Color.RED), name))

if __name__ == "__main__":
    main()
