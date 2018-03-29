import wget
import gzip
import os

file = open("cc-index.paths", "r")

i = 0
for index_url in file:
	full_index_url = "https://commoncrawl.s3.amazonaws.com/" + index_url
	print "Downloading : " + full_index_url
	wget.download(full_index_url, './index_file.gz')
	print "\nEnd Download"
	print "Unzip File"

	os.system('gunzip index_file.gz')

	print "Unzip End"

	print "Begin map : " + `i`
	os.system('cat index_file | ./map.py > out-map.txt')
	print "End map : " + `i`
	print "Begin Reduce : " + `i`
	os.system('cat out-map.txt | ./reduce.py >> out-reduce.txt')
	print "End Reduce : " + `i`

	os.system('rm out-map.txt')
	os.system('rm index_file')
	i = i +1

print "Begin final reduce"
os.system('cat out-reduce.txt | ./reduce.py >> out-reduce-final.txt')
os.system('rm out-reduce.txt')
print "Begin map TLD"
os.system('cat out-reduce-final.txt | ./map-tld.py > out-map-tld.txt')
print "Begin reduce TLD"
os.system('cat out-map-tld.txt | ./reduce.py >> out-reduce-tld.txt')

