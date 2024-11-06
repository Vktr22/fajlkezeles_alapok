import math
import random


def lista_letrehozasa():
    #generálj 100 véletlen egész számot [-50;150]
    #a fgv térjen vissza a listával
    lista=[]
    i:int=0
    while(i<100):
        szam:int=int(random.random()*(151+50)-50)
        lista.append(szam)
        i+=1
    return lista

#a listában lévő számokat fűzd össze string-é, az elválaztó jel ';' legyen
#az utolsó után ne legyen
def szovegge_alakit(lista):
    i:int=0
    szoveg: str=""
    while(i<len(lista)-1):
        szoveg+=str(lista[i])
        szoveg+=";"
        # szoveg+=f"{lista[i]};"    -> zárójel nélkül, ha string értéknek adom!!!
        i+=1
    szoveg+=str(lista[i])
    return szoveg

"""def fajlba_mentes(szoveg):           -> ahányszor futtatom, annyiszor generálódik le (ugyan abba a file-ba
    fajlom = open("adatok.txt", "w", encoding='utf-8')
    fajlom.write(szoveg)
    fajlom.close()"""

"""adatok beolvasása fájlból"""

def fajlbol_olvas(szoveg, list):
    fajlom = open("adatok.txt", "r", encoding='utf-8')
    szoveg_fajlbol:str=fajlom.read()
    list = szoveg_fajlbol.split(";")
    """végigmegyek a szöveglistán, és minden elemét számmá alakítom
    és eltávolítom belőle a felesleges szóközöket"""
    lista=[]
    for i in range(0, len(list), 1):
        szam:int=int(list[i].strip())
        lista.append(szam)
    '''print(szoveg_fajlbol)
    print(lista)'''
    fajlom.close()
    return lista
