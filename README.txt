SETUP
--------------------------------------------------------------------------------

Clone this repo and add it to your path.

USAGE
--------------------------------------------------------------------------------

TeXparse is a simple wrapper-script which calls latexmk with the appropriate arguments
and displays debug-information from the logfile in a format that won't make your
eyes bleed.

Compiling

    $ texparse <root_file>

Cleaning

    $ texparse <root_file> -c

FEATURE REQUEST
--------------------------------------------------------------------------------

Add support for filtering biblatex warnings and errors.
