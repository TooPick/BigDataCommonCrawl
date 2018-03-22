Pour utiliser le map sur un fichier "in.txt" :
	cat in.txt | ./map.py > out-map.txt

Pour utiliser le reduce sur un fichier "out-map.txt" :
	cat out-map.txt | ./reduce.py > out-reduce.txt

Pour exécuter le programme "Suffix" qui récupère les indexs et analyse leurs suffixes:
	python ./suffix.py

Pour utiliser le programme "stats" qui calcule les poucentages sur un fichier "in.txt":
	cat in.txt | ./stats.py > out-stats.txt
