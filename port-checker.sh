#!/bin/bash
TARGET=$1
PORTS=(22 80 443)
NAMES=("SSH" "HTTP" "HTTPS") #array called names, index matches ports -> ssh is 22 and so on...

echo "Target: $TARGET"
echo "-------------------" #prints header to screen, $Target is replaced with the IP Domain that is typed 
# example: Target: google.com
# intermission: Bash is a shell scripting language to automate multiple terminal commands
for i in 0 1 2; do #loop that runs 3 times, every port once
  (echo >/dev/tcp/$TARGET/${PORTS[$i]}) 2>/dev/null #attempt a network connection and if it fails error code is hidden
  if [ $? -eq 0 ]; then  # 0 means success = port open, so it  means if port is open
   echo "[OPEN]   Port ${PORTS[$i]} (${NAMES[$i]})" #print open with port nr and name
  else
    echo "[CLOSED] Port ${PORTS[$i]} (${NAMES[$i]})" # if closed then same info
  fi # closes the if statement (if backwards lol how creative)
done #closes for loop

