from itertools import groupby
import csv

# le fichier 'infos-TLD.csv' est genere par 'extract-TLD.py' et a le format [timestamp, url, code_http]

input_data = []
with open('infos-TLD.csv') as fi:
    csv_data = csv.reader(fi)
    input_data = list(csv_data)

status_code_list = map(lambda x : x[2], input_data) # extraire les codes 
status_code_list_sorted = sorted(status_code_list) # trier

counts = [len(list(group)) for key, group in groupby(status_code_list_sorted)] # compter les repetitions
total_count = sum(counts) # compter la somme totale des codes

status_code_set = set(status_code_list_sorted) # enlever les repetitions
status_code_set_list = list(status_code_set) # convertir set en list pour pouvoir le trier
status_code_set_sorted = sorted(status_code_set_list) # trier la liste

percentages = []
with open('codes_stats.csv', 'w') as fo:
    print("Code HTTP : Nombre absolu (Pourcentage)")
    fo.write("Code HTTP, Nombre absolu, Pourcentage \n")
    for i in range(0, len(counts)):
        percentages.append(round(counts[i] / total_count * 100, 2)) # compter les pourcentages de chaque code
        print("{} : {} ({}%)".format(status_code_set_sorted[i], counts[i], percentages[i])) # imprimer
        fo.write("{}, {}, {}%\n".format(status_code_set_sorted[i], counts[i], percentages[i])) # ecrire dans le fichier
    fo.close()