from functools import reduce
import sys

def skaiciu_vidurkis(failo_pavadinimas):
    with open(failo_pavadinimas, 'r', encoding='utf-8') as failas:
        eilutes = failas.readlines()

    skaiciai = []
    for eilute in eilutes:
        skaiciai += [int(skaicius) for skaicius in eilute.strip().replace(',', ' ').split()]

    vidurkis = reduce(lambda x, y: x + y, skaiciai) / len(skaiciai)

    with open('rezultatas.txt', 'r+', encoding='utf-8') as rez_failas:
        rez_failas.write(str(vidurkis))

    return vidurkis

failo_pavadinimas = 'duomenys.txt'
vidurkis = skaiciu_vidurkis(failo_pavadinimas)
sys.stdout.reconfigure(encoding='utf-8')
print("skaiciu vidurkis", vidurkis,)

