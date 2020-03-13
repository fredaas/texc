DESCRIPTION
--------------------------------------------------------------------------------

Texparse is a thin wrapper on top of latexmk.

Texparse calls latexmk with the appropriate arguments and displays debug
information from the log file in a format that won't make you're eyes bleed.

TEX LIVE SETUP
--------------------------------------------------------------------------------

Download the latest Tex Live distribution:

    $ wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz

Unpack and install:

    $ tar -xvf install-tl-unx.tar.gz
    $ cd install-tl-unx
    $ perl install-tl

USAGE
--------------------------------------------------------------------------------

Compile:

    $ texparse <root_file>

Clean:

    $ texparse -c
