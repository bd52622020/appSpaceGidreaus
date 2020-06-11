#! /bin/bash

DIR1="/$HOME/Documents/Files"
DIR2="/$HOME/Documents/Files2"

### Check for dir, if not found create it using the mkdir ###
[ ! -d "$DIR2" ] && mkdir -p "$DIR2"


### Find html files and randomly copy some of them in DIR2 ###
HTML_FILES=($(ls | grep "html"))

echo RANDOM HTML FILES COPYING
for file in "${HTML_FILES[@]}"
do
	if (( $(( RANDOM % 2 )) == 0 ))
	then
		cp "$DIR1/$file" "$DIR2"
		echo $file is copied.
	fi
done


### Copy all files in the same directory
cp -a $DIR1/* $DIR2
#ALL_FILES=($(ls -a))

echo "${HTML_FILES[@]}"



