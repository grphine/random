# This program will get all images in subdirectories with the listed extensions and create symlinks in a single folder, so that Window's inflexible slideshow wallpaper setting can find the images to show.
# Admin perms required because Python can't creat Windows dirs with delete perms.
# Intended to be run from the root of all the subdirs, and creates a new folder called "wallpapers" with all the links.

import os
from pathlib import Path
import pyuac

root = Path(os.getcwd())
image_extensions = [".png", ".jpeg", ".jpg"]

# folder to place symlinks
symlink_dir = "wallpapers"

def clean_dirs():
    print("Cleaning up dirs")
    # delete and recreate folder
    try:
        os.unlink(root / symlink_dir)
    except OSError:
        pass
    os.makedirs(root / symlink_dir)

def create_links():
    print("Creating image links")
    # walk all subdirs
    for path, subdirs, files in os.walk(root):
        # skip the symlink dir
        if symlink_dir in path:
            continue
        # operate on each file found
        for name in files:
            # if file matches extensions listed
            if any(ext in name for ext in image_extensions):
                # create symlink of image to new folder
                src = os.path.join(path, name)
                dst = root / symlink_dir / name
                os.symlink(src, dst)

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin")
        pyuac.runAsAdmin()
    else:        
        clean_dirs()
        create_links()
        print("Done")

