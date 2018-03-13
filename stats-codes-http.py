import re
from itertools import groupby

# remplacer nom-du-fichier-index par le nom d'un fichier (cdx-00000, cdx-00001 etc)

input_data = ""
with open('nom-du-fichier-index') as fi:
    input_data = fi.read()

data = re.findall('"status": "\d\d\d', input_data) # chercher tous les codes
status_code_list = map(lambda x : x[11:], data) # extraire les codes sans le prefix ["status:" "] 
status_code_list_sorted = sorted(status_code_list) # trier

counts = [len(list(group)) for key, group in groupby(status_code_list_sorted)] # compter les repetitions
total_count = sum(counts) # compter la somme totale des codes

status_code_set = set(status_code_list_sorted) # enlever les repetitions
status_code_set_list = list(status_code_set) # convertir set en list pour pouvoir le trier
status_code_set_sorted = sorted(status_code_set_list) # trier la liste

percentages = []
with open('codes_stats.txt', 'w') as fo:
    for i in range(0, len(counts)):
        percentages.append(round(counts[i] / total_count * 100, 2)) # compter les pourcentages de chaque code
        print("{} : {} ({}%)".format(status_code_set_sorted[i], counts[i], percentages[i])) # imprimer
        fo.write("{} : {} ({}%)\n".format(status_code_set_sorted[i], counts[i], percentages[i])) # ecrire dans le fichier
    fo.close()