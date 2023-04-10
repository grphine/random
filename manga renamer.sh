# rename all manga titles in a collection

# /Collection
# ├── /Title1
# │   ├── _66.cbz
# │   └── _Chapter 67.cbz
# ├── /Title2
# │   ├── Chapter 117.cbz
# │   └── Chapter 118 - Name.cbz
# ├── /Title3
# │   ├── foo bar_Ch.10 - Name.cbz
# │   ├── foo_Ch.21.cbz
# │   └── foo_Ch.22.cbz
# ├── /Title4
# │   ├── _Chapter 72_Voluminous.cbz
# │   └── _Chapter 73_Final Chapter.cbz
# ├── /Title5
# │   └── name.cbz
# ├── /Title6
# │   └── Chapter 11 - Ch.11.cbz
# └── /Title7
#     ├── bar_Ch.58.2.cbz
#     └── bar_Vol.11 Ch.58.1.cbz

# desired structure
# /Collection
# ├── /Title1
# │   ├── Ch.66.cbz
# │   └── Ch.67.cbz
# ├── /Title2
# │   ├── Ch.117.cbz
# │   └── Ch.118 - Name.cbz
# ├── /Title3
# │   ├── Ch.10 - Name.cbz
# │   ├── Ch.21.cbz
# │   └── Ch.22.cbz
# ├── /Title4
# │   ├── Ch.72 - Voluminous.cbz
# │   └── Ch.73 - Final Chapter.cbz
# ├── /Title5
# │   └── name.cbz
# ├── /Title6
# │   └── Ch.11.cbz
# └── /Title7
#     ├── Ch.58.2.cbz
#     └── Vol.11 Ch.58.1.cbz

shopt -s globstar	#allow subdirectory traversal with **
for file in **/*.cbz
do
    # regex to split filepath into groups
    [[ $file =~ ^(.*/)?(.*)(\..*)$ ]]
    dirname=${BASH_REMATCH[1]}
    filename=${BASH_REMATCH[2]}
    extension=${BASH_REMATCH[3]}

    # match and rebuild volume name
    [[ $filename =~ Vol(ume)?[.\ ]([0-9]+) ]]
    volume=${BASH_REMATCH[2]}

    filename=${filename#*"${BASH_REMATCH[0]}"}

    # match and rebuild chapter name
    [[ $filename =~ Ch(apter)?[.\ ]([0-9]+(\.[0-9]+)*)|([0-9]+(\.[0-9]+)*) ]]
    chapter=${BASH_REMATCH[2]}${BASH_REMATCH[4]}

    # report failed filename
    [[ ${chapter:+X} ]] || {
        printf 'illegal filename: %q\n' "$file" 1>&2
        continue
    }
    filename=${filename#*"${BASH_REMATCH[0]}"}

    # replace '_' with ' - '
    [[ $filename =~ [_\ ]+(-\ +)?(.*)$ ]]
    title=${BASH_REMATCH[2]}

    filename=${volume:+Vol."$volume" }Ch.$chapter${title:+ - "$title"}

    # printf '%q %q %q\n' mv "$file" "$dirname$filename$extension" # echo command

    if [[ $file != "$dirname$filename$extension" ]]
    then mv "$file" "$dirname$filename$extension"
    fi
done

