import shutil
import os
import sys
import re

# This program is a modification of the album collater script working on a much simpler directory structure

# folder structure
# /root
# ├──/01
# │   ├──/png
# │   │   ├──/01.png
# │   │   └──/04.png
# │   └──/gif
# │       ├──/01.gif
# │       └──/03.gif
# ├──/02
# │   ├──/png
# │   │   ├──/01.png
# │   │   └──/04.png
# │   └──/gif
# │       ├──/01.gif
# │       └──/03.gif
# └──/extra
#     ├──/png
#     │   ├──/01.png
#     │   └──/04.png
#     └──/video.mp4

# desired structure
# /collection
# └──/date
#     ├──01_01.png
#     ├──01_04.png
#     ├──01_01.gif
#     ├──01_03.gif
#     ├──extra_01.png
#     └──extra_video.mp4

def rename_move_images(path_length, album_path, rename_path):
    for root, dirs, files in os.walk(album_path):
        fullpath = root.split("\\")   # ['C:', 'Users', 'user', 'Downloads', 'folder', 'base']
        subdir = fullpath[path_length:]         # current subdirectories

        # # if in subdir
        if subdir:  
            # get base album folder name, i.e. 2020
            yr = fullpath[path_length - 1] 
            # print("dir: ", yr, subdir)
            
            for file in files:
                oldname = "{}\{}".format(root,file)
                print("old name: ", oldname)
                newname = "{}\{}\{}_{}".format(album_path, rename_path, yr, file)
                print("new name: ", newname)
                shutil.copy(oldname, newname)

root_dir = os.getcwd()
album = input("album to operate on: ")
if album == "":
    # if empty
    print("no album provided, operating on current dir:")
    album_path = os.getcwd()
    print(album_path, "\n")
else:
    album_path = os.path.join(os.getcwd(), album)
    if os.path.isdir(album_path) == False:
        # check exists
        print("provided album does not exists\nexiting")
        sys.exit()

new_base = input("folder to create: ")
if new_base == "":
    # if empty
    print("nothing provided, using default (renamed_python_album)")
    new_base = "renamed_python_album"
if os.path.isdir(new_base) == False:
    # if doesn't exist
    print("doesn't exists, creating")
    os.makedirs(os.path.join(album_path, new_base))
else:
    print("folder exists, using")

# where to operate on in file path
split_dir = album_path.split("\\")
dir_length = len(split_dir) + 1

rename_move_images(dir_length, album_path, new_base)
print("rename done")