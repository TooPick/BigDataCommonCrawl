import urllib.request
import argparse
import json

# parsing des arguments de ligne de commande
parser = argparse.ArgumentParser()
parser.add_argument("search_page", help="Monthly Search page (ex. CC-MAIN-2018-09)")
parser.add_argument("url", help="Root URL of a website (ex. commoncrawl.org)")
args = parser.parse_args()

# transformer le prefix du format <fr,nom2,nom1)> en format <nom1.nom2.fr>
def reverse_prefix(url):
    url_splitted = url.split(')') # diviser sur la parenthese
    prefix = url_splitted[0].split(',') # diviser sur les virgules
    prefix.reverse()
    return "{}{}".format(".".join(prefix), url_splitted[1]) # joindre le prefixe inverse avec le reste

# convertir en tableau d'objets JSON propre
# le format initial : <{objet}\n{objet}...>
# le format cible :   <[{objet},{objet}...]>
def convertToJson(data):
    data = str(data, "utf-8") # co  nvertir en string
    data = ",".join(data.split("\n")) # remplacer les sauts de ligne par des virgules
    data = data[:-1] # supprimer la virgule a la fin
    return "[{}]".format(data) # mettre en format de tableau

# construire la requete pour l'Index de commoncrawl
request = 'http://index.commoncrawl.org/{}-index?url={}%2F*&output=json'.format(args.search_page, args.url)

try:
    # telecharger toutes les donnees concernant l'url
    raw_data = urllib.request.urlopen(request).read()
except (http.client.IncompleteRead) as e:
    raw_data = e.partial

data = convertToJson(raw_data)
data_json = json.loads(data)
urls = list(map(lambda x : x["urlkey"], data_json)) # extraire seulement les URLs
urls = list(map(lambda x : reverse_prefix(x), urls)) # inverser les prefixes
urls = sorted(list(set(urls))) # supprimer les doublons et trier

# ecrire en sortie d'ecran et dans le fichier
with open("{}-pages.txt".format(args.url), 'w') as fo:
    for i in range(0, len(urls)):
        fo.write(urls[i] + '\n')
        print (urls[i])