import csv
import os
import time
import datetime

# le fichier 'URL_stats.csv' est genere par 'stats-URL.py' et a le format [Pourcentage, Nombre absolu, URL] + 2 en-tetes
# le fichier 'all_URL.txt' est genere par ce script et n'est pris en compte que s'il existe deja

all_urls = [] # l'ensemble des URLs deja recuperes

if os.path.exists('./all_URL.txt'): # s'il y a deja des URLs, on les lit
    with open('all_URL.txt') as fi:
        all_urls = fi.read().split('\n')
all_urls = list(filter(None, all_urls)) # supprimer des eventuels elements vides

next_data = [] # nouveaux URLs
with open('URL_stats4.csv') as fi: # lire un fichier des stats sur les URLs
    csv_data = csv.reader(fi)
    next_data = list(csv_data)

next_data = next_data[2:] # supprimer les en-tetes (URL uniques; Pourcentage, Nb absolu, URL)
next_urls = list(map(lambda x : x[2], next_data)) # prendre que les URLs (sans Nb et Pourcents)
new_urls = [item for item in next_urls if item not in all_urls] # prendre les URLs qui sont dans la deuxieme liste mais pas dans la premiere

all_urls += new_urls # ajouter les nouveaux URLs
added_proportion = len(new_urls) / len(all_urls) * 100 # calculer le taux des URLs ajoutes

stats_filename = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S') # un nom de fichier unique pour les stats
stats = "URLs ajoutees : {} ({}%)".format(len(new_urls), round(added_proportion, 5)) # les stats
print (stats)

with open(stats_filename + '_added_URL_stats.txt', 'w') as fo: # ecrire les stats
    fo.write(stats)
with open('all_URL.txt', 'w') as fo: # ecrire l'ensemble des URLs
    fo.write('\n'.join(all_urls))