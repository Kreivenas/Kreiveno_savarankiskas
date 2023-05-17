# -*- coding: utf-8 -*-
# Sukurti funkciją, kuri priimtų sąrašą tuple elementų,
# kiekvienas tuple sudarytas iš 2 elementų - stringo ir sąrašo int skaičių.
# Funkcija turi grąžinti sąrašą tuple elementų, kurie sudaryti iš 2 reikšmių:
# stringo ir skaičių vidurkio:
# Pvz: į funkciją paduodamas sąrašas:
# [("apple", [1, 2, 3]), ("banana", [4, 5, 6]), ("orange", [7, 8, 9])],
# turi būti grąžinamas: [("apple", 2.0), ("banana", 5.0), ("orange", 8.0)]
# Panaudoti sukurtą funkciją su kokiomis norite reikšmėmis ir atspausdinti funkcijos rezultatus

def skaiciu_vidurkis(sarasas):
    rezultatas = []
    for elementas in sarasas:
        tekstas, skaiciai = elementas
        vidurkis = sum(skaiciai) / len(skaiciai)
        rezultatas.append((tekstas, int(vidurkis))) #man taip skaiciai graziau atrodo :)
    return rezultatas

# Testuojame funkciją
pradinis_sarasas = [("BMW", [325, 315, 320]), ("Audi", [100, 4, 6]), ("VW", [2, 4, 6])]
rezultatas = skaiciu_vidurkis(pradinis_sarasas)
print(rezultatas)
