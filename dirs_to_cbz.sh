#!/bin/bash

# given folders in a directory, replace  with a cbz archive of their contents

IFS=$'\n'

for f in $(find "$1" -mindepth 1 -maxdepth 1 -type d ); do
  zip -rjm "$f.cbz" "$f"
done
