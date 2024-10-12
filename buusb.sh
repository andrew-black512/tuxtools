
SUB=$1  # relatvei to ~/   
DRIVE=/media/andrew/seagate2019 
DRIVE=$(locat_bu_device.sh)

DEST=$DRIVE/tallisbu_22
mkdir -p $DEST/$SUB
rsync ~/$SUB/  $DEST/$SUB  -va
#tree -d $DEST
