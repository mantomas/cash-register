"""
Utilities to keep main app small
and easier to develop.
Contain functions to read and write files
and will be extended.
"""
import os.path # used to check if file exist
import datetime # give access to actual date and time functions

def read_backup(): 
    """
    read backup_money value from a file
    and if there is none it is created
    """
    if os.path.isfile("backup_money.txt"): # check if file exist
        myfile = open('backup_money.txt', 'r') # open to read
        backup_money = myfile.read() # takes the value of backup
        myfile.close
    else: # if file don't exist backup = 0
        backup_money = 0
        
    backup_coins = int(backup_money) # make sure backup_couns value is integer
    return backup_coins

def write_backup(self):
    """
    rewrites value of backup_money
    """
    myfile = open('backup_money.txt', 'w+')
    myfile.write(self.e13.get())
    myfile.close
    
def save_result(stav_kasy, rozdil_trzby):
    """
    takes the result from calculation,
    creates new file with actual date and time
    or append existing one with line
    containing date, time, reference value and difference
    """
    now = datetime.datetime.now()
    datum = now.strftime("%d.%m.%Y %H:%M")
    myfile = open('archive.txt', 'a')
    myfile.write("%-19s%-11s%-7s%-14s%-7s%-1s" % (datum, 'Stav kasy: ', str(stav_kasy), 'Rozdíl tržby: ', str(rozdil_trzby), '\n'))
    myfile.close