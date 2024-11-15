
if [[ $# -lt 1 ]]; then
    echo "Error: Not enough arguments provided."
    echo "Usage: $0 <argument1>  ..."
    echo "Please provide at least 1 argument1."
    exit 1
fi
SUB=$1  # relatvei to ~/
OPTS='--delete-during -a -v'

DEST=$DRIVE/$TOPDIR
##mkdir -p $DEST/$SUB

TOPDIR=$HOSTNAME   
#DRIVE="animals@tallis.local:Public/backups"
DRIVE="animals@localhost:Public/backups"

DEST=$DRIVE/$TOPDIR
##mkdir -p $DEST/$SUB
set -x
rsync ~/$SUB/  $DEST/$SUB  $OPTS

#tree -d $DEST
