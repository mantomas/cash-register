import datetime

def zapsani_trzby_do_souboru(stav_kasy, rozdil_trzby):
    now = datetime.datetime.now()
    datum = now.strftime("%d.%m.%Y %H:%M")
    myfile = open('trzba.dat', 'a')
    myfile.write(datum + '\tStav kasy: ' + str(stav_kasy) + '\tRozdíl tržby: ' + str(rozdil_trzby) + '\n')
    myfile.close