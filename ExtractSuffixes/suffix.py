import wget
import gzip

file = open("cc-index.paths", "r")

for index_url in file:
	full_index_url = "https://commoncrawl.s3.amazonaws.com/" + index_url
	print "Downloading : " + full_index_url
	wget.download(full_index_url, './index_file.gz')
	print "End Download"
	print "Unzip File"

	index_file = gzip.GzipFile('./index_file.gz', 'rb')
	s = index_file.read()
	index_file.close()

	outF = file("index_file1", 'wb')
	outF.write(s)
	outF.close()

	print "Unzip End"
	break
