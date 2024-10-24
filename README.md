# random
A collection of random scripts for backup purposes.

## album collater.py
renames and flattens a directory structure

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
3. loop over all lines of stdout
4. skip empty lines
5. move file into folder matching col name (folder already exists)
   e.g. 
     ash_201733_044BMB_201733090.jpg -> 201733/ash_201733_044BMB_201733090.jpg
     ash_195204_044ASI_195204001.jpg -> 195204/ash_195204_044ASI_195204001.jpg
   
## file_move_by_filename.sh 
move a file into a folder matching its second column
```
ash_201733_044BMB_201733090.jpg -> 201733/ash_201733_044BMB_201733090.jpg
ash_195204_044ASI_195204001.jpg -> 195204/ash_195204_044ASI_195204001.jpg
```

## filesize_finder.sh
finds the total size of all files matching the extension.  
takes arguments `/location *.ext`  
includes delete line

## manga renamer.sh
renames inconsistent naming of titles in a manga collection

