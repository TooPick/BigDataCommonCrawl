import wget
import gzip
import os

file = open("cc-index.paths", "r")

i = 0
for index_url in file:
	full_index_url = "https://commoncrawl.s3.amazonaws.com/" + index_url
	print "Downloading : " + full_index_url
	wget.download(full_index_url, './index_file.gz')
	print "End Download"
	print "Unzip File"

	os.system('gunzip index_file.gz')

	print "Unzip End"
	os.system('rm index_file.gz')

	print "Begin map : " + `i`
	os.system('cat index_file | ./map.py > out-map.txt')
	print "End map : " + `i`
	print "Begin Reduce : " + `i`
	os.system('cat out-map.txt | ./reduce.py >> out-reduce.txt')
	print "End Reduce : " + `i`

	os.system('rm out-map.txt')
	os.system('rm index_file')
	i = i +1
