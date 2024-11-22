

TUXLOC=$(dirname $(realpath "$BASH_SOURCE"))
echo $TUXLOC

alias flick='$TUXLOC/get_flickr_mb.py'
alias scone='$TUXLOC/scone.py'
alias lspdf='$TUXLOC/lspdf.py'
alias pdfannot='$TUXLOC/pdfannot.py'

alias g.tux='cd $TUXLOC' 

PATH=$PATH:$TUXLOC
    