import re

# remplacer nom-du-fichier-index par le nom d'un fichier (cdx-00000, cdx-00001 etc)

input_data = ""
with open('nom-du-fichier-index') as fi:
    input_data = fi.read()

urls_list = re.findall('"url": "(?:(?:https?://)|(?:www\.))(?:[^?/ ])+', input_data)
urls_set = set(urls_list) # pour se debarrasser des repetitions

with open('urls.txt', 'w') as fo:
	for url in urls_set:
	    fo.write("{}\n".format(url[8:])) # substring pour prendre l'url sans "url": " au debut 
	fo.close()