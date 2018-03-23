import csv
import re
from itertools import groupby

# le fichier 'infos-URL.csv' est genere par 'extract-URL.py' et a le format [timestamp, url, code_http]

input_data = list()
urls_list = list()
urls_list_sorted = list()

with open('infos-URL.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		input_data.append(row[1])

urls_list_sorted = sorted(input_data)

counts = [len(list(group)) for key, group in groupby(urls_list_sorted)] # compter les repetitions
total_count = sum(counts) # compter la somme totale des codes

urls_list_set = set(urls_list_sorted) # enlever les repetitions
urls_list_set_list = list(urls_list_set) # convertir set en list pour pouvoir le trier
urls_list_set_sorted = sorted(urls_list_set_list) # trier la liste

nb_url_unique = len(urls_list_set_list)

percentages = []
with open('URL_stats.csv', 'w') as fo:
    print ("nombre de URL : {}".format(total_count))
    print ("URL uniques : {}".format(nb_url_unique))
    fo.write("URL uniques : {} \n".format(nb_url_unique))
    fo.write("Pourcentage, Nombre absolu, URL \n")
    for i in range(0, len(counts)):
        percentages.append(counts[i] / total_count * 100) # compter les pourcentages de chaque code
        fo.write("{}%,{},{}\n".format(percentages[i], counts[i], urls_list_set_sorted[i])) # ecrire dans le fichier
    fo.close()