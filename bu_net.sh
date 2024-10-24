
SUB=$1  # relatvei to ~/
TOPDIR=$HOSTNAME   
DRIVE='rsync:ludford.local/Public/backups/$TOPDIR'

DEST=$DRIVE/$TOPDIR
mkdir -p $DEST/$SUB
eho rsync ~/$SUB/  $DEST/$SUB  -va
#tree -d $DEST
