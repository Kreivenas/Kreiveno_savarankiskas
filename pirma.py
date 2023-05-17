def gauti_pirmas_raides(sarasas):
    pirmos_raides = []
    for vardas in sarasas:
        pirmos_raides.append(vardas[0])
    return pirmos_raides

vardai = ['Tomas', 'Kamile', 'Kajus', 'Ligita', 'Dovydas']

rezultatas = gauti_pirmas_raides(vardai)
print(rezultatas)
