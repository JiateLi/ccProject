te.sh is the shell script answered the q7 of checkpoint
use the following lines to run it
chmod u+x te.sh
./te.sh 'britney spears' 1990 2000



Q1. grep -i -P 'The Beatles' million_songs_metadata.csv|wc -l

Q3. awk ' BEGIN {FS = ","} ; {if ($7 ~ /Elvis Presley/) { print; }}' million_songs_metadata.csv|wc -l

Q4. awk ' BEGIN {FS = ","} ; {if( $11 >= 1970 && $11 <= 1990 && $10 >0.8) { print; }}' million_songs_metadata.csv

Q5. awk 'BEGIN {FS = ","};{sum = sum + $8;num= num + 1}END{print sum/num}' million_songs_metadata.csv

Q6
vim te.sh

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

chmod u+x te.sh
./te.sh 'britney spears' 1990 2000



Q9
join -t "," -o 1.1 1.2 1.3 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 2.10 2.11 million_songs_sales_data.csv million_songs_metadata.csv  > million_songs_metadata_and_sales.csv

awk 'BEGIN {max=0; num=0; FS=","} {a[$7]+=$3;b[$7]=$9} END {for (i in a) if (a[i]>num){num=a[i]+0;max=b[i]};{print max,num}}' million_songs_metadata_and_sales.csv 

Q13:
SELECT * FROM songs WHERE binary track_id LIKE '%The Beatles%' OR binary title LIKE '%The Beatles%' OR binary song_id LIKE '%The Beatles%' OR binary `release` LIKE '%The Beatles%' OR binary artist_id LIKE '%The Beatles%' OR binary artist_mbid LIKE '%The Beatles%' OR binary artist_name LIKE '%The Beatles%' OR binary duration LIKE '%The Beatles%' OR binary artist_familiarity LIKE '%The Beatles%' OR binary artist_hotttnesss LIKE '%The Beatles%' OR binary year LIKE '%The Beatles%';

Q14
SELECT * FROM songs WHERE track_id LIKE '%The Beatles%' OR title LIKE '%The Beatles%' OR song_id LIKE '%The Beatles%' OR `release` LIKE '%The Beatles%' OR artist_id LIKE '%The Beatles%' OR artist_mbid LIKE '%The Beatles%' OR artist_name LIKE '%The Beatles%' OR duration LIKE '%The Beatles%' OR artist_familiarity LIKE '%The Beatles%' OR artist_hotttnesss LIKE '%The Beatles%' OR year LIKE '%The Beatles%';

Q15
SELECT year,count(*) FROM songs GROUP BY year ORDER BY count(*) DESC LIMIT 5;

Q16
SELECT artist_name,count(*) FROM songs GROUP BY artist_id ORDER BY count(*) DESC LIMIT 5;


Q17
SELECT songs.artist_name,SUM(sales_count) AS total_sale FROM songs INNER JOIN sales on songs.track_id = sales.track_id WHERE songs.artist_id = (SELECT DISTINCT artist_id FROM songs WHERE BINARY artist_name = 'Beastie Boys') ORDER BY total_sale;


Q18
SELECT songs.artist_name,SUM(sales_count>50) AS total_sale FROM songs INNER JOIN sales on songs.track_id = sales.track_id WHERE songs.artist_name = 'Johnny Cash' OR songs.artist_name = 'Bob Dylan' OR songs.artist_name = 'Britney Spears' OR songs.artist_name = 'Michael Jackson' OR songs.artist_name = 'Franz Ferdinand' GROUP BY songs.artist_name ORDER BY total_sale DESC;
