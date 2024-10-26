#!/bin/bash

<<'###'
1. for each dir in current "parent" dir
2. enter dir
3. get current dir name (e.g. "ash")
4. list files
5. awk unique occurrences of second column
   e.g. 
     ├── ash_201733_044BMB_201733090.jpg 
     ├── ash_201733_044BMB_201733134.jpg 
     ├── ash_195204_044ASI_195204001.jpg
     ├── ash_195204_044ASI_195204002.jpg
   will result in
     201733
     195204
6. loop over all lines of stdout, and assign current line to $id
7. ignore any empty lines
8. create folder (ignore if it already exists)
9. move file into folder matching col name
   e.g. 
     ash_201733_044BMB_201733090.jpg -> 201733/ash_201733_044BMB_201733090.jpg
     ash_195204_044ASI_195204001.jpg -> 195204/ash_195204_044ASI_195204001.jpg
10. exit dir, goto 1
###

file_mover () {
   folder=$(echo "${PWD##*/}")
   ls | awk -F"_" '{a[$2]++} END { for (b in a) {print b} }' | while read -r line; do
      if [ -n "$line" ]; then
         mkdir -p $line
         mv -i $folder*$line* $line/
      fi;
   done;
}

for D in ./*; do
    if [ -d "$D" ]; then
        cd "$D"
        file_mover
        cd ..
    fi;
done;

