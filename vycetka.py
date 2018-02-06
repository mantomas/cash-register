# import zapsani_trzby
import soucet_penez
from fileinput import close

myfile = open('odlozene_drobne.txt', 'r') # otevření souboru se stavem odložených drobných
odlozene_drobne = int(myfile.read()) # přečtení hodnoty a vrácení stavu jako integer
myfile = close()

# výpočet stavu kasy - volá součtový modul a připočítá odložené drobné a stav druhé kasy
stav_kasy = soucet_penez.soucet() + odlozene_drobne + soucet_penez.ostatni()
rozdil_trzby = stav_kasy - soucet_penez.spravny_stav()
print('V kase je: ', str(stav_kasy) + ',-Kč')
print('Rozdíl tržby je: ', str(rozdil_trzby) + ',-Kč')
# zapsani_trzby.zapsani_trzby_do_souboru(stav_kasy, rozdil_trzby)