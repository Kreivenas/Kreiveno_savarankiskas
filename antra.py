# -*- coding: utf-8 -*-
# Sukurti funkciją, kuri priimtų tuple ir grązintų kitą tuple,
# tik su pasalintais dublikatais. Eiliskumas elementų turi išlikti toks pats:
# Pvz: jeigu funkcija priima (1, 2, 3, 4, 3, 2, 1) tuple,
# tai turėtų grąžinti (1, 2, 3, 4)
# Pvz: jeigu funkcija priima (‘a’, ‘d’, ‘g’, ‘h’, ‘i’, ‘q’, ‘q’, ‘h’, ‘d’) tuple,
# tai turėtų grąžinti (‘a’, ‘d’, ‘g’, ‘h’, ‘i’, ‘q’)
# Paduoti tuple į funkciją (reikšmes sugalvokite patys)
# ir išspausdinti funkcijos rezultatą
def pasalinti_dublikatus(tup):
    unikalios_reiksmes = []
    for elementas in tup:
        if elementas not in unikalios_reiksmes:
            unikalios_reiksmes.append(elementas)
    return tuple(unikalios_reiksmes)

pradinis_tuple = (1, 2, 5, 19, 3, 19, 1, 22, 2, 2, 1)
result = pasalinti_dublikatus(pradinis_tuple)
print(result)

pradinis_tuple = ('l', 'b', 'r', 'h', 'l', 'b', 'a', 'i', 's', 'k', 'j', 'k')
result = pasalinti_dublikatus(pradinis_tuple)
print(result)
