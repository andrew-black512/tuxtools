
SUB=$1  # relatvei to ~/
TOPDIR=$HOSTNAME   
DRIVE="ludford.local:Public/backups"

DEST=$DRIVE/$TOPDIR
mkdir -p $DEST/$SUB
rsync ~/$SUB/  $DEST/$SUB  -va
#tree -d $DEST
