#! /bin/bash 

while read line 
do 
full_index_url='https://commoncrawl.s3.amazonaws.com/'
wget $full_index_url$line -O index_file.gz
gunzip index_file.gz
grep -o "\"url\":.*\.fr/" index_file | grep -o "[a-zA-Z0-9-]*\.fr" | awk '!x[$0]++' >> resultat.txt
rm index_file
done < cc-index.paths
awk '!x[$0]++' resultat.txt > resultatFinal.txt
