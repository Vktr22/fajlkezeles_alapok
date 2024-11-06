import fajlkezeles
import feladatok

lista = fajlkezeles.lista_letrehozasa()

szoveg = fajlkezeles.szovegge_alakit(lista)
#fajlkezeles.fajlba_mentes(szoveg)
fajlkezeles.fajlbol_olvas(szoveg, lista)


"""
1, hány negatív szám van a listában?
2, melyik a legnagyobb szám?
3, készíts új listát paros_lista néven és legyenek benne a páros számok
4, mennyi az öttel osztható számok összege
5, hányadik helyen áll a legkisebb szám első előfordulása"""
print("1. hány negatív szám van?")
negativDb=feladatok.negativ_db(lista)
print(negativDb)
print()

print("2. Melyik a legnagyobb szám?")
legnagyobbSzam=feladatok.legnagyobbSzam(lista)
print(legnagyobbSzam)
print()

print("3. páros lista:")
parosLista = feladatok.parosSzamokLista(lista)
print(parosLista)
print()

print("4. 5-el osztható számok összege:")
ottelSzum=feladatok.ottelOszthatokOsszege(lista)
print(ottelSzum)
print()

print("5. a legkisebb szám első előfordulási helye:")
minErtek = feladatok.minErtek(lista)
minhely = feladatok.minErtekElsoEloford(lista, minErtek)
print(minhely)
print()
