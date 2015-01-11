#!/bin/bash
artist_name=$1
start_year=$2
end_year=$3
count=0
OLD_IFS="$IFS"
IFS=','
while read line
do
arr=(${line})
shopt -s nocasematch
if [[ "${arr[6]}" =~ "$artist_name" ]] && [ ${arr[10]} -le $end_year ] && [ ${arr[10]} -ge $start_year ]
then
count=$(($count+1))
fi
done < million_songs_metadata.csv
shopt -u nocasematch
IFS="$OLD_IFS"
echo $count
