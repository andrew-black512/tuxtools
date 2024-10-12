
SUB=$1  # relatvei to ~/
TOPDIR=$HOSTNAME   
DRIVE=$(locate_bu_device.sh)

DEST=$DRIVE/$TOPDIR
mkdir -p $DEST/$SUB
rsync ~/$SUB/  $DEST/$SUB  -va
#tree -d $DEST
