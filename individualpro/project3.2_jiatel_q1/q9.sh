#!/bin/bash
join -t "," -o 1.1 1.2 1.3 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 2.10 2.11 million_songs_sales_data.csv million_songs_metadata.csv  > million_songs_metadata_and_sales.csv
awk 'BEGIN {max=0; num=0; FS=","} {a[$7]+=$3;b[$7]=$9} END {for (i in a) if (a[i]>num){num=a[i]+0;max=b[i]};{print max,num}}' million_songs_metadata_and_sales.csv 
