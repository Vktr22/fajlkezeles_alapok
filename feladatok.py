"""
1, hány negatív szám van a listában?
2, melyik a legnagyobb szám?
3, készíts új listát paros_lista néven és legyenek benne a páros számok
4, mennyi az öttel osztható számok összege
5, hányadik helyen áll a legkisebb szám első előfordilása"""

def negativ_db(lista):
    db:int=0
    for i in range (0, len(lista), 1):
        if (lista[i]<0):
            db+=1
    return db
def legnagyobbSzam(lista):
    legnagyobb:int=0
    i:int=0
    while (i<len(lista)):
        if (lista[i]>legnagyobb):
            legnagyobb=lista[i]
        i+=1
    return legnagyobb

def parosSzamokLista(lista):
    parosLista=[]
    for i in range(0, len(lista), 1):
        if (lista[i]%2==0):
            parosLista.append(lista[i])
    return parosLista

def ottelOszthatokOsszege(lista):
    osszeg:int=0
    for i in range(0, len(lista), 1):
        if(lista[i]%5==0):
            osszeg+=lista[i]
    return osszeg

def minErtek(lista):
    min:int=0
    for i in range (0, len(lista), 1):
        if (lista[i]<min):
            min=lista[i]
    return min

def minErtekElsoEloford(lista, min):
    i=0
    while(lista[i]!=min):
        i+=1
    return i

