from datetime import date

annee = input('Quelle année ? ')

if not annee or annee == "":  #verifica se o input esta vazio, se sim pega o ano atual
    annee = int(date.today().year)
else:
    annee = int(annee)
if annee %4 == 0 and annee %100 !=0 or annee %400 == 0:
    print(f'Le {annee} est bissextile')
else:
    print(f' Le {annee} n est pas bissexile')