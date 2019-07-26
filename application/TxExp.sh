#!/bin/bash
# Script for recording transmission times of various image sizes on varying bandwidths.

# 1) Need to run in order to use 'identify':
# sudo apt-get update
# sudo apt-get install imagemagick

# 2) Measure bandwidth on interface
# ifstat -i eth0 -q 1

# 3) Control link bandwidth:
# sudo wondershaper eth1 downspeed upspeed
# sudo wondershaper clear eth1

# $) To SCP to another host you need to create a RSA key and share it
# ssh-keygen -t rsa
# ssh jonpatma@198.129.50.7 mkdir -p .ssh

# Login to host that you are transferring to and put:
# sudo passwd
# cat ~/.ssh/id_rsa.pub | ssh jonpatma@198.129.50.7 'cat >> .ssh/authorized_keys'

FILES=/usr/local/Face_Recognition_Files/FaceRec_Dataset/lowres/*
# output=/usr/local/"DataOutput.csv"

# if [ ! -f $output ]; then
#     touch $output
# else 
#     rm $output
#     touch $output
# fi
#rm -rf $output_dir/*	# Clean-up old files

# time (scp /usr/local/ExpImg/0000.png jonpatma@128.194.6.155:ExpImg)
# awk -F'[ ms]+' '/^real/ {print "copy time: "1000*$2"ms"}' $output
# echo "1000*$2ms" >> $output
# #rm $output

sudo rm output.txt

echo -e "Filename\tImgHeight\tImgWidth\tDatasize\tTx" >> output.txt
startTot=$(date +%s.%N)
for f in $FILES
do
  # TODO: Add code for adding dimensions of images
  
  echo "processing: $f"
  W=`identify $f | cut -f 3 -d " " | sed s/x.*//` #width
  H=`identify $f | cut -f 3 -d " " | sed s/.*x//` #height
  DS=$(wc -c < $f)
  start=$(date +%s.%N)
  exe=$(scp $f jonpatma@198.129.50.7:/usr/local/ExpImg_lowres)
  end=$(date +%s.%N)
  DIFF=$(echo "$end - $start" | bc)
  # echo $DIFF >> $output
  echo -e "$f\t$H\t$W\t$DS\t$DIFF" >> output/transmission.txt
done
echo "Transferring complete!"
endTot=$(date +%s.%N)
DIFF1=$(echo "$endTot - $startTot" | bc)
echo "Total time: $DIFF1"

# sudo echo "export PYTHONPATH=$PYTHONPATH:/local/models/research:/local/models/research/slim" >> /etc/ssh/sshrc