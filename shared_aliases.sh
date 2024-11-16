
set -x
TUXLOC=$(dirname "$BASH_SOURCE")


alias flick='$TUXLOC/get_flickr_mb.py'
alias scone='$TUXLOC/scone.py'
alias lspdf='$TUXLOC/lspdf.py'
alias pdfannot='$TUXLOC/pdfannot.py'

alias g.tux='cd $TUXLOC' 

PATH=$PATH:$TUXLOC
set +x
