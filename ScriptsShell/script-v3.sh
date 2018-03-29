#!/bin/bash

date
start=`date +%s`
while read line
do
	file="$(basename $line)"
	path="/srv/data_350/Feb2018/"
	zcat $path$file | cut -f1,2 -d',' | cut -f1 -d')' | awk '!x[$0]++' | grep "^$1," >> resultat.txt

done < $2
awk '!x[$0]++' resultat.txt > resultatFinal.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
date


