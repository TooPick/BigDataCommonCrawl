import csv
import re
from itertools import groupby

# remplacer nom-du-fichier-index par le nom d'un fichier (cdx-00000, cdx-00001 etc)

input_data = list()
urls_list = list()
urls_list_sorted = list()
urls_list_sorted2 = list()
"""
with open('cdx-00000-mini.txt') as fi:
    input_data = fi.read()

data = re.findall('"url": "(?:(?:https?://)|(?:www\.))(?:(?:\w*[a-zA-Z]\w*)[^?/ ])+', input_data)
urls_list = map(lambda x : x[8:], data) # extraire les codes sans le prefix ["url": "] 
urls_list_sorted = sorted(urls_list) # trier
"""
with open('infos-TLD.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		input_data.append(row[1])

urls_list_sorted2 = sorted(input_data)
for i in range(0, len(urls_list_sorted2)):
	matab = urls_list_sorted2[i].split('.')
	if(len(matab) == 3):
		urls_list_sorted.append(matab[1]+'.'+matab[2])
	else:
		if(len(matab) == 2):
			temp = matab[0].split('//')
			urls_list_sorted.append(temp[1]+'.'+matab[1])

"""
for i in range(0, len(urls_list_sorted)):
	index1 = urls_list_sorted[i].find('https://www.') # 12 caracteres à couper
	index2 = urls_list_sorted[i].find('http://www.') # 11 caractere à couper
	index3 = urls_list_sorted[i].find('http://') # 4
	index4 = urls_list_sorted[i].find('https://') # 5 

	if index1 != -1:
		#print("couper la chaine 12 caracteres")
		urls_list.append(urls_list_sorted[i])
		
	else:
		if index2 != -1:
			print("couper la chaine 11 caracteres")
		else:
			if index3 != -1:
				print("couper la chaine 4 caracteres")
			else:
				print("couper la chaine 5 caracteres")

urls_list2 = list(map(lambda x : x[12:], urls_list))
print(urls_list2)
#print(urls_list_sorted)
"""


counts = [len(list(group)) for key, group in groupby(urls_list_sorted)] # compter les repetitions
total_count = sum(counts) # compter la somme totale des codes

urls_list_set = set(urls_list_sorted) # enlever les repetitions
urls_list_set_list = list(urls_list_set) # convertir set en list pour pouvoir le trier
urls_list_set_sorted = sorted(urls_list_set_list) # trier la liste

nb_tld_unique = len(urls_list_set_list)

#print(counts)
#print(urls_list_set_sorted)

percentages = []
with open('TLD_stats.txt', 'w') as fo:
    print ("nombre de TLD : {}".format(total_count))
    print ("TLD uniques : {}".format(nb_tld_unique))
    fo.write("TLD uniques : {} \n".format(nb_tld_unique))
    fo.write("URL | Nombre absolu | Pourcentage \n")
    for i in range(0, len(counts)-1):
        percentages.append(counts[i] / total_count * 100) # compter les pourcentages de chaque code
        fo.write("{} % : {} ({})\n".format(percentages[i], counts[i], urls_list_set_sorted[i])) # ecrire dans le fichier
    fo.close()