#!/usr/bin/env bash

set -e

ROOT=$(realpath "${BASH_SOURCE[0]}")
ROOT=$(dirname "$ROOT")
cd "$ROOT"

download_tar()
{
    DIR="$1" URL="$2" FILE=${URL##*/}
    wget "$URL"
    mkdir -p "$DIR" && tar -xvf "$FILE" -C $DIR --strip-components 1
}

INSTALL_DIR="texlive"

download_tar "$INSTALL_DIR" "http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz"

cd "$INSTALL_DIR"

sudo perl install-tl

cat << EOF

-------------------------------------------------------------------------------

Installation complete!

You may want to add these to your .bashrc:

export MANPATH=/usr/local/texlive/<release>/texmf-dist/doc/man:\$MANPATH
export INFOPATH=/usr/local/texlive/<release>/texmf-dist/doc/info:\$INFOPATH
export PATH=/usr/local/texlive/<release>/bin/x86_64-linux:\$PATH

-------------------------------------------------------------------------------

EOF
