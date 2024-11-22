
if [[ $# -lt 2 ]]; then
    echo "Error: Not enough arguments provided."
    echo "Usage: $0 <argument1>  ..."
    echo "Please provide at least 2 argument1."
    exit 1
fi
NODE=$1
SUB=$2  # relatvei to ~/
OPTS='--delete-during -a -v' 
#    TODO --backup-dir=BACKUP '

DEST=$DRIVE/$TOPDIR
##mkdir -p $DEST/$SUB

TOPDIR=$HOSTNAME   
DRIVE="$NODE.local:Public/backups"

DEST=$DRIVE/$TOPDIR
##mkdir -p $DEST/$SUB
set -x
rsync ~/$SUB/  $DEST/$SUB  $OPTS

#tree -d $DEST
