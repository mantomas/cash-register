def soucet():
    while True:
        try:
            koruny = int(input('Počet korunových mincí: '))
        except ValueError:
            print('To nebylo celé číslo!')
        else:
            if koruny < 0:
                print('Záporné množství nedává smysl!')
            else:
                break
    while True:
        try:
            dvoukoruny = int(input('Počet dvoukorunových mincí: '))
        except ValueError:
            print('To nebylo celé číslo!')
        else:
            if dvoukoruny < 0:
                print('Záporné množství nedává smysl!')
            else:
                break
    soucet  = koruny + dvoukoruny*2
    return soucet

def ostatni():
    while True:
        try:
            druha_kasa = int(input('Stav druhé kasy: '))
        except ValueError:
            print('To nebylo celé číslo!')
        else:
            if druha_kasa < 0:
                print('Záporné množství nedává smysl!')
            else:
                break
    return druha_kasa

def spravny_stav():
    while True:
        try:
            spravny_stav = int(input('Jaký stav kasy hlásí pokladna: '))
        except ValueError:
            print('To nebylo celé číslo!')
        else:
            if spravny_stav < 0:
                print('Záporné množství nedává smysl!')
            else:
                break
    return spravny_stav
