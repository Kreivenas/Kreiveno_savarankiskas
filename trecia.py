# Sukurti programą, kuri saugotų duomenis apie darbuotojus Pickle faile bei atliktų su duomenimis įvairius veiksmus:
# Sukurti funkciją, kuri sukuria darbuotoją (vardas, amžius, darbo pozicija) ir jį grąžina
# Sukurti funkciją, kuri išsaugo darbuotojus į failą (pickle)
# Sukurti funkciją, kuri užkrauna darbuotojus iš failo ir juos grąžina (pickle)
# Panaudoti sukūrimo funkciją kelis kartus su kokiomis norite reikšmėmis
# Panaudoti išsaugojimą į failą funkciją
# Panaudoti užkrovimo iš failo funkciją
# Atspausdinkite užkrautus iš failo duomenis
import pickle

def sukurti_darbuotoja(vardas, amzius, pozicija):
    darbuotojas = {"vardas": vardas, "amzius": amzius, "pozicija": pozicija}
    return darbuotojas

def issaugoti_darbuotojus(Darbuotojai, failo_pavadinimas):
    with open(failo_pavadinimas, 'wb') as f:
        pickle.dump(Darbuotojai, f)

def uzkrauti_darbuotojus(failo_pavadinimas):
    with open(failo_pavadinimas, 'rb') as f:
        Darbuotojai = pickle.load(f)
    return Darbuotojai

darbuotojas1 = sukurti_darbuotoja("Jonas", 30, "Vadybininkas")
darbuotojas2 = sukurti_darbuotoja("Petras", 35, "Programuotojas")
darbuotojas3 = sukurti_darbuotoja("Linas", 28, "Dizaineris")

Darbuotojai = [darbuotojas1, darbuotojas2, darbuotojas3]

issaugoti_darbuotojus(Darbuotojai, "Darbuotojai.pickle")

uzkrauti_darbuotojus = uzkrauti_darbuotojus("Darbuotojai.pickle")

for darbuotojas in uzkrauti_darbuotojus:
    print(darbuotojas["vardas"], darbuotojas["amzius"], darbuotojas["pozicija"])
