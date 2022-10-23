DESCRIPTION
--------------------------------------------------------------------------------

Texparse is a simple command-line interface to latexmk and a log-file parser.

TEX LIVE SETUP
--------------------------------------------------------------------------------

Download the latest Tex Live distribution:

    $ wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz

Unpack and install:

    $ tar -xvf install-tl-unx.tar.gz
    $ cd install-tl-<version>
    $ perl install-tl

Update paths:

    export MANPATH=/usr/local/texlive/<version>/texmf-dist/doc/man:$MANPATH
    export INFOPATH=/usr/local/texlive/<version>/texmf-dist/doc/info:$INFOPATH
    export PATH=/usr/local/texlive/<version>/bin/x86_64-linux:$PATH

VERIFYING INSTALL
--------------------------------------------------------------------------------

$ ./check_install.py

USAGE
--------------------------------------------------------------------------------

Compile:

    $ texparse <root_file>

Clean:

    $ texparse -c
