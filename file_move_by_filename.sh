#!/bin/bash

<<'###'
0. get current dir name (e.g. "ash")
1. list files
2. awk unique occurrences of second column
   e.g. 
     ├── ash_201733_044BMB_201733090.jpg 
     ├── ash_201733_044BMB_201733134.jpg 
     ├── ash_195204_044ASI_195204001.jpg
     ├── ash_195204_044ASI_195204002.jpg
   will result in
     201733
     195204
3. loop over all lines of stdout, and assign current line to $id
4. ignore any empty lines
5. create folder (ignore if it already exists)
6. move file into folder matching col name
   e.g. 
     ash_201733_044BMB_201733090.jpg -> 201733/ash_201733_044BMB_201733090.jpg
     ash_195204_044ASI_195204001.jpg -> 195204/ash_195204_044ASI_195204001.jpg
###

folder=$(echo "${PWD##*/}")
ls | awk -F"_" '{a[$2]++} END { for (b in a) {print b} }' | while read -r id; do
  if [ -n "$id" ]; then
    mkdir -p $id
    mv -vi $folder*$id* $id/
  fi;
done;

