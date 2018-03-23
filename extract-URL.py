import re
from itertools import groupby

# separer une ligne de donnees en trois parties : timestamp, url et code http
def separate(data):
    url_raw = data.split(')')[0]
    url_raw = url_raw.split(',')
    url_raw.reverse()
    url = ".".join(url_raw)
    timestamp = re.findall(' \d{14} {', data)[0] # ne prendre que la partie URL donc tout avant / ou ?
    timestamp = timestamp[1:-2]
    return (timestamp, url, data[-3:]) # 14 premiers chars c'est le timestamp, 3 derniers c'est le code http

# remplacer nom-du-fichier-index par le nom d'un fichier (cdx-00000, cdx-00001 etc)
input_data = ""
with open('nom-du-fichier-index') as fi:
    input_data = fi.read()

# prendre tout ce qui est entre timestamp et status http, par exemple :
# 20180219115239 {"url": "http://example.com/", "mime": "text/html", "mime-detected": "text/html", "status": "301"
data = re.findall('(?:[a-z])+(?:,[a-z]+)+\)/.+\d{14}.+status": "\d{3}', input_data) # prendre les donnees en format "timestamp
data_separated = list(map(lambda x : separate(x), data)) # appliquer la fonction du haut aux donnees
code = ''
with open('infos-URL.csv', 'w') as fo:
    for i in range(0, len(data_separated)):
        if(int(data_separated[i][2]) >= 200 and int(data_separated[i][2]) < 300):
            code = 'OK'
        else:
            if(int(data_separated[i][2]) >= 300 and int(data_separated[i][2]) < 400):
                code = 'Redirection'
            else:
                if(int(data_separated[i][2]) >= 400):
                    code = 'Erreur'
        fo.write("{},{},{}\n".format(data_separated[i][0], data_separated[i][1], code))
    fo.close()