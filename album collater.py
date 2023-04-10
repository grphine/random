import shutil
import os
import sys
import re

# This program flattens a frankly disgusting level of subdividing of images into a more manageable single directory.

# folder structure
# \collection
# ├──\2020
# │   ├──\album1
# │   │   ├──\sub
# │   │   │   ├── 1.jpg
# │   │   │   └── 2.jpg
# │   │   └──\sub2
# │   │       ├──\1
# │   │       │   ├── 1.jpg
# │   │       │   └── 2.jpg
# │   │       └──\2
# │   │           ├── 1.jpg
# │   │           └── 2.jpg
# │   └──\album2
# │       ├──\1
# │       │   ├── 1.jpg
# │       │   └── 2.jpg
# │       └──\2
# │           ├── 1.jpg
# │           └── 2.jpg
# └──\2021
#     └──\album1
#         ├── 1.jpg
#         └── 2.jpg

# desired structure
# \collection
# ├──\2020
# │   ├──album1_sub_1.jpg
# │   ├──album1_sub_2.jpg
# │   ├──album1_sub2_1_1.jpg
# │   ├──album1_sub2_1_2.jpg
# │   ├──album1_sub2_2_1.jpg
# │   ├──album1_sub2_2_2.jpg
# │   ├──album2_1_1.jpg
# │   ├──album2_1_2.jpg
# │   ├──album2_2_1.jpg
# │   └──album2_2_2.jpg
# └──\2021
#     ├──album1_1.jpg
#     └──album1_2.jpg

# folder to operate on
path = r'C:\Users\[user]\Desktop\folder\base'

for root, dirs, files in os.walk(path):
    fullpath = root.split("\\")   # ['C:', 'Users', '[user]', 'Desktop', 'folder', 'base', + year + subdirectories]
    subdir = fullpath[7:]         # current subdirectories

    # if in subdir
    if subdir:  
        # get base album folder name, i.e. 2020
        yr = fullpath[6] 

        # match leading digits of first subfolder name, i.e. 1-album, 14-album
        rePattern = "^\d{1,2}"
        dirmatch = re.match(rePattern, subdir[0])
        if dirmatch:
            # zero pad, for file ordering purposes. 01-album precedes 14-album
            subdir[0] = re.sub(rePattern, dirmatch.group(0).zfill(2), subdir[0])

        # zero pad files
        for file in files:
            filematch = re.match(rePattern, file)
            if filematch:
                paddedFileName = re.sub(rePattern, filematch.group(0).zfill(2), file)

            # C:\Users\[user]\Desktop\folder\base\2020\03_album_2_02.jpg
            newname = "{}\{}\{}_{}".format(path,yr,("_").join(subdir),paddedFileName)
            # perform rename and move
            shutil.move("{}\{}".format(root,file), newname)
            # deleting empty folder didn't quite work 
            # shutil.rmtree(root)
