#!/usr/bin/env bash

set -e

wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar -xvf install-tl-unx.tar.gz

INSTALL_DIR=`ls | rg -o "install-tl-\d+$"`
[ -z $INSTALL_DIR ] && echo "[ERROR] Failed to parse string" && exit 1

TEXLIVE_RELEASE=`echo $INSTALL_DIR | rg -o -r '$1' "install-tl-(\d{4}).*$"`
[ -z $TEXLIVE_RELEASE ] && echo "[ERROR] Failed to parse string" && exit 1

# cd $INSTALL_DIR
# sudo perl install-tl

cat << EOF

-------------------------------------------------------------------------------

Installation complete!

You may want to add these to your .bashrc:

export MANPATH=/usr/local/texlive/$TEXLIVE_RELEASE/texmf-dist/doc/man:\$MANPATH
export INFOPATH=/usr/local/texlive/$TEXLIVE_RELEASE/texmf-dist/doc/info:\$INFOPATH
export PATH=/usr/local/texlive/$TEXLIVE_RELEASE/bin/x86_64-linux:\$PATH

-------------------------------------------------------------------------------

EOF
