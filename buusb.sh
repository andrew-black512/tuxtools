
SUB=$1  # relatvei to ~/
TOPDIR=$HOSTNAME/$USER   
DRIVE=$(locate_bu_device.sh)

DEST=$DRIVE/$TOPDIR
echo $DEST
mkdir -p $DEST/$SUB
rsync ~/$SUB/  $DEST/$SUB  -va
#tree -d $DEST
