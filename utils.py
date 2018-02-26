import os.path
import datetime

def read_backup():
    if os.path.isfile("odlozene_drobne.txt"):
        myfile = open('odlozene_drobne.txt', 'r')
        part = myfile.read()
        myfile.close
    else:
        myfile = open('odlozene_drobne.txt', 'w+')
        part = myfile.read()
        myfile.close    
        
    if part == '':
        backup_coins = 0
    else:
        backup_coins = int(part)
    return backup_coins

def write_backup(self):
    myfile = open('odlozene_drobne.txt', 'w+')
    myfile.write(self.e13.get())
    myfile.close
    
def save_result(stav_kasy, rozdil_trzby):
    now = datetime.datetime.now()
    datum = now.strftime("%d.%m.%Y %H:%M")
    myfile = open('trzba.dat', 'a')
    myfile.write("%-19s%-11s%-7s%-14s%-7s%-1s" % (datum, 'Stav kasy: ', str(stav_kasy), 'Rozdíl tržby: ', str(rozdil_trzby), '\n'))
    myfile.close