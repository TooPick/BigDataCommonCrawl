import re
from itertools import groupby

# remplacer nom-du-fichier-index par le nom d'un fichier (cdx-00000, cdx-00001 etc)

input_data = ""
with open('index-snippet.txt') as fi:
    input_data = fi.read()

data = re.findall('"url": "(?:(?:https?://)|(?:www\.))(?:(?:\w*[a-zA-Z]\w*)[^?/ ])+', input_data)
urls_list = map(lambda x : x[8:], data) # extraire les codes sans le prefix ["url": "] 
urls_list_sorted = sorted(urls_list) # trier

counts = [len(list(group)) for key, group in groupby(urls_list_sorted)] # compter les repetitions
total_count = sum(counts) # compter la somme totale des codes

urls_list_set = set(urls_list_sorted) # enlever les repetitions
urls_list_set_list = list(urls_list_set) # convertir set en list pour pouvoir le trier
urls_list_set_sorted = sorted(urls_list_set_list) # trier la liste

percentages = []
with open('TLD_stats.txt', 'w') as fo:
    print ("TLD uniques : {}".format(total_count))
    fo.write("TLD uniques : {}".format(total_count))
    fo.write("URL | Nombre absolu | Pourcentage".format(total_count))
    for i in range(0, len(counts)):
        percentages.append(counts[i] / total_count * 100) # compter les pourcentages de chaque code
        # print("{} : {} ({}%)".format(urls_list_set_sorted[i], counts[i], percentages[i])) # imprimer
        fo.write("{} : {} ({}%)\n".format(percentages[i], counts[i], urls_list_set_sorted[i])) # ecrire dans le fichier
    fo.close()