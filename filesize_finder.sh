#args: /location *.ext

#!/bin/bash

echo "start"
location="$1"
ext="$2"
find $location -type f -name $ext -print0 | du -ch --files0-from=- --total -s | tail -1
#find $location -type f -name $ext -exec rm {} \;

