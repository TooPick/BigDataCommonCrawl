import re
from itertools import groupby

# separer une ligne de donnees en trois parties : timestamp, url et code http
def separate(data):
    url = data[24:] # enlever tout ce qui esr avant l'url
    tld = re.findall('(?:(?:https?://)|(?:www\.))(?:(?:\w*[a-zA-Z]\w*)[^?/ ])+', url)[0] # ne prendre que la partie TLD donc tout avant / ou ?
    return (data[:14], tld, data[-3:]) # 14 premiers chars c'est le timestamp, 3 derniers c'est le code http

# remplacer nom-du-fichier-index par le nom d'un fichier (cdx-00000, cdx-00001 etc)
input_data = ""
with open('index-snippet.txt') as fi:
    input_data = fi.read()

# prendre tout ce qui est entre timestamp et status http, par exemple :
# 20180219115239 {"url": "http://example.com/", "mime": "text/html", "mime-detected": "text/html", "status": "301"
data = re.findall('\d{14} {"url": "(?:(?:https?://)|(?:www\.))(?:(?:\w*[a-zA-Z]\w*)[^?/ ])+.*status": "\d{3}', input_data) # prendre les donnees en format "timestamp
data_separated = list(map(lambda x : separate(x), data)) # appliquer la fonction du haut aux donnees

with open('infos-TLD.csv', 'w') as fo:
    for i in range(0, len(data_separated)):
        fo.write("{}, {}, {}\n".format(data_separated[i][0], data_separated[i][1], data_separated[i][2]))
    fo.close()