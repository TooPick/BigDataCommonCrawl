import csv
import os
import time
import datetime

# le fichier 'TLD_stats.csv' est genere par 'stats-TLD.py' et a le format [Pourcentage, Nombre absolu, URL] + 2 en-tetes
# le fichier 'all_TLD.txt' est genere par ce script et n'est pris en compte que s'il existe deja

all_tlds = [] # l'ensemble des TLDs deja recuperes

if os.path.exists('./all_TLD.txt'): # s'il y a deja des TLDs, on les lit
    with open('all_TLD.txt') as fi:
        all_tlds = fi.read().split('\n')
all_tlds = list(filter(None, all_tlds)) # supprimer des eventuels elements vides

next_data = [] # nouveaux TLDs
with open('TLD_stats4.csv') as fi: # lire un fichier des stats sur les TLDs
    csv_data = csv.reader(fi)
    next_data = list(csv_data)

next_data = next_data[2:] # supprimer les en-tetes (TLD uniques; Pourcentage, Nb absolu, TLD)
next_tlds = list(map(lambda x : x[2], next_data)) # prendre que les TLDs (sans Nb et Pourcents)
new_tlds = [item for item in next_tlds if item not in all_tlds] # prendre les TLDs qui sont dans la deuxieme liste mais pas dans la premiere

all_tlds += new_tlds # ajouter les nouveaux TLDs
added_proportion = len(new_tlds) / len(all_tlds) * 100 # calculer le taux des TLDs ajoutes

stats_filename = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S') # un nom de fichier unique pour les stats
stats = "TLDs ajoutees : {} ({}%)".format(len(new_tlds), round(added_proportion, 5)) # les stats
print (stats)

with open(stats_filename + '_added_TLD_stats.txt', 'w') as fo: # ecrire les stats
    fo.write(stats)
with open('all_TLD.txt', 'w') as fo: # ecrire l'ensemble des TLDs
    fo.write('\n'.join(all_tlds))