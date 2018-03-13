Pour utiliser le map sur un fichier "in.txt" :
	cat in.txt | ./map.py > out-map.txt

Pour utiliser le reduce sur un fichier "out-map.txt" :
	cat out-map.txt | ./reduce.py > out-reduce.txt
