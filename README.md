# BigDataCommonCrawl

*1. Travail sur un  seul fragment (1Go) de l'index de l'index.*
- récupérer l'archive compressée

- extraire des infos relatives TLD (lemonde.fr, lequipe.fr etc, pas foot.lequipe.fr) sous ce format: (csv: timestamp, url_original, http_header_response, url_target)

        extract-URL.py

- estimer le taux de répétition des TLD sur un fragment et le nombre de TLD uniques

        stats-URL.py

- donner la répartition par suffix (.fr .com .net etc)

        ExtractSuffixes

- donner la répartition des codes http générale, puis par suffix

        stats-codes-http.py

*2. Travail sur différent fragments (aléatoire svp, par le 001 puis 002, 003)*
- répeter point 1.
- estimer le taux de nouveaux TLD ajouté par chaque fragment, par rapport à l'ensemble des TLD déjà récupérées.

        stats-added-URL.py

- à partir de combien de fragments est-on raisonnablement serein de couvrir à peu pres l'ensemble des TLD accédés sur le mois ?
- quelle homogénéité de la répartition des suffixes ?

*3. Passage sur le cloud*
_(au besoin pour les TLD, tres probablement indispensable pour la récup des données de scraping)_
- mettre au point l'archive locale WARC et les outils d'acces
(se réferrer au doc écrit par Eric sur D)

*0. Points divers*
(cartographie)
- y a-t-il des redirections massives ?
- qqs stats sur le nombres de pages/img/.../? par site
