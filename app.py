# -*- coding: utf-8 -*-
import tkinter as tk
import utils
import os

class hlavni_okno:
    def __init__(self, master):   
        self.panel2 = tk.Frame(master)
        self.panel2.grid()
        obr5000 = os.path.join(os.path.dirname(__file__), 'img/5000.gif')
        obr2000 = os.path.join(os.path.dirname(__file__), 'img/2000.gif')
        obr1000 = os.path.join(os.path.dirname(__file__), 'img/1000.gif')
        obr500 = os.path.join(os.path.dirname(__file__), 'img/500.gif')
        obr200 = os.path.join(os.path.dirname(__file__), 'img/200.gif')
        obr100 = os.path.join(os.path.dirname(__file__), 'img/100.gif')
        obr50 = os.path.join(os.path.dirname(__file__), 'img/50.gif')
        obr20 = os.path.join(os.path.dirname(__file__), 'img/20.gif')
        obr10 = os.path.join(os.path.dirname(__file__), 'img/10.gif')
        obr5 = os.path.join(os.path.dirname(__file__), 'img/5.gif')
        obr2 = os.path.join(os.path.dirname(__file__), 'img/2.gif')
        obr1 = os.path.join(os.path.dirname(__file__), 'img/1.gif')
        obrdrobne = os.path.join(os.path.dirname(__file__), 'img/drobne.gif')
        obrdruha = os.path.join(os.path.dirname(__file__), 'img/druha.gif')
        obrdoklady = os.path.join(os.path.dirname(__file__), 'img/doklady.gif')
        obrzasilkovna = os.path.join(os.path.dirname(__file__), 'img/zasilkovna.gif')
        obrok = os.path.join(os.path.dirname(__file__), 'img/ok.gif')
        ic5000 = tk.PhotoImage(file=obr5000)  
        tk.Label.ic5000 = ic5000 # avoid garbage collector    
        ic2000 = tk.PhotoImage(file=obr2000)  
        tk.Label.ic2000 = ic2000
        ic1000 = tk.PhotoImage(file=obr1000)  
        tk.Label.ic1000 = ic1000
        ic500 = tk.PhotoImage(file=obr500)  
        tk.Label.ic500 = ic500
        ic200 = tk.PhotoImage(file=obr200)  
        tk.Label.ic200 = ic200
        ic100 = tk.PhotoImage(file=obr100)  
        tk.Label.ic100 = ic100
        ic50 = tk.PhotoImage(file=obr50)  
        tk.Label.ic50 = ic50
        ic20 = tk.PhotoImage(file=obr20)  
        tk.Label.ic20 = ic20
        ic10 = tk.PhotoImage(file=obr10)  
        tk.Label.ic10 = ic10
        ic5 = tk.PhotoImage(file=obr5)  
        tk.Label.ic5 = ic5
        ic2 = tk.PhotoImage(file=obr2)  
        tk.Label.ic2 = ic2
        ic1 = tk.PhotoImage(file=obr1)  
        tk.Label.ic1 = ic1
        icdrobne = tk.PhotoImage(file=obrdrobne)  
        tk.Label.icdrobne = icdrobne
        icdruha = tk.PhotoImage(file=obrdruha)  
        tk.Label.icdruha = icdruha
        icdoklady = tk.PhotoImage(file=obrdoklady)  
        tk.Label.icdoklady = icdoklady
        iczasilkovna = tk.PhotoImage(file=obrzasilkovna)  
        tk.Label.iczasilkovna = iczasilkovna
        icok = tk.PhotoImage(file=obrok)  
        tk.Label.icok = icok
    # validating command
        vcmd = (master.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')    
    # label for value input      

        
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="5000").grid(row=0)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="2000").grid(row=1)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="1000").grid(row=2)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="500").grid(row=3)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="200").grid(row=4)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="100").grid(row=5)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="50").grid(row=6)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="20").grid(row=7)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="10").grid(row=8)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="5").grid(row=9)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="2").grid(row=10)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="1").grid(row=11)
    # label for special value input   
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="Odložené drobné").grid(row=12)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="Druhá kasa").grid(row=13)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="Neuhrazené doklady").grid(row=14)
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="Zásilkovna").grid(row=15)
    # label for the correct state of the cash register
        tk.Label(self.panel2, width=20, font = "Helvetica 12", anchor="e", text="V kase má být...", bg="light green").grid(row=16)
    # label images
        tk.Label(self.panel2, image = ic5000).grid(row=0, column=1)     
        tk.Label(self.panel2, image = ic2000).grid(row=1, column=1)  
        tk.Label(self.panel2, image = ic1000).grid(row=2, column=1)
        tk.Label(self.panel2, image = ic500).grid(row=3, column=1)
        tk.Label(self.panel2, image = ic200).grid(row=4, column=1)
        tk.Label(self.panel2, image = ic100).grid(row=5, column=1)
        tk.Label(self.panel2, image = ic50).grid(row=6, column=1)
        tk.Label(self.panel2, image = ic20).grid(row=7, column=1)
        tk.Label(self.panel2, image = ic10).grid(row=8, column=1)
        tk.Label(self.panel2, image = ic5).grid(row=9, column=1)
        tk.Label(self.panel2, image = ic2).grid(row=10, column=1)
        tk.Label(self.panel2, image = ic1).grid(row=11, column=1)  
        tk.Label(self.panel2, image = icdrobne).grid(row=12, column=1)
        tk.Label(self.panel2, image = icdruha).grid(row=13, column=1)
        tk.Label(self.panel2, image = icdoklady).grid(row=14, column=1)
        tk.Label(self.panel2, image = iczasilkovna).grid(row=15, column=1)
        tk.Label(self.panel2, image = icok).grid(row=16, column=1)     
    # entry field for value input 
        self.e1 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e1.focus() # focus on the first entry
        self.e2 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e3 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e4 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e5 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e6 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e7 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e8 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e9 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e10 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e11 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e12 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
    # entry field for special value input    
        self.e13 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e14 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e15 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
        self.e16 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
    # entry field for the correct state of the cash register   
        self.e17 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8)
    # entry for actual_result to place its value
        self.e18 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd, width=8, font = "Helvetica 26")
        
    # placing entry fields in a grid   
        self.e1.grid(row=0, column=2, padx=2, pady=2)
        self.e2.grid(row=1, column=2, padx=2, pady=2)
        self.e3.grid(row=2, column=2, padx=2, pady=2)
        self.e4.grid(row=3, column=2, padx=2, pady=2)
        self.e5.grid(row=4, column=2, padx=2, pady=2)
        self.e6.grid(row=5, column=2, padx=2, pady=2)
        self.e7.grid(row=6, column=2, padx=2, pady=2)
        self.e8.grid(row=7, column=2, padx=2, pady=2)
        self.e9.grid(row=8, column=2, padx=2, pady=2)
        self.e10.grid(row=9, column=2, padx=2, pady=2)
        self.e11.grid(row=10, column=2, padx=2, pady=2)
        self.e12.grid(row=11, column=2, padx=2, pady=2)
        self.e13.grid(row=12, column=2, padx=2, pady=2) # odlozene drobne
        self.e13.insert(0, backup_coins)
        self.e14.grid(row=13, column=2, padx=2, pady=2)
        self.e15.grid(row=14, column=2, padx=2, pady=2)
        self.e16.grid(row=15, column=2, padx=2, pady=2)
        self.e17.grid(row=16, column=2, padx=2, pady=2) # reference value
    # actual result    
        self.e18.grid(row=17, column=3, padx=10, pady=2) 
    # button area
        self.button3 = tk.Button(self.panel2, text = "Přepiš drobné", width=20, command = self.write_backup)
        self.button3.grid(row=12, column=3) # write backup_coins
        self.button2 = tk.Button(self.panel2, text = "Mezisoučet", width=20, command = self.show_me)
        self.button2.grid(row=16, column=3) # calculation
        self.button1 = tk.Button(self.panel2, text = "Zavřít", command = self.panel2.quit)
        self.button1.grid(row=19, column=0) # close without save
        self.button4 = tk.Button(self.panel2, text = "Uložit a zavřít", width=20, command = self.save_and_quit)
        self.button4.grid(row=19, column=3) # save result into file and close
    # calculating function = returning actual_result
    def secti_penize(self):
        jednotlive_stavy = [
            self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(),
            self.e5.get(), self.e6.get(), self.e7.get(), self.e8.get(),
            self.e9.get(), self.e10.get(), self.e11.get(), self.e12.get(),
            ]
        drobne = self.e13.get()
        if drobne == '':
            drobne = 0
        else:
            drobne = int(drobne)
        druhakasa = self.e14.get()
        if druhakasa == '':
            druhakasa = 0
        else:
            druhakasa = int(druhakasa)
        neuhrazeno = self.e15.get()
        if neuhrazeno == '':
            neuhrazeno = 0
        else:
            neuhrazeno = int(neuhrazeno)
        zasilkovna = self.e16.get()
        if zasilkovna == '':
            zasilkovna = 0
        else:
            zasilkovna = int(zasilkovna)
            
        reference = self.e17.get()
        if reference == '':
            reference = 0
        else:
            reference = int(reference)
            
        for index in range(len(jednotlive_stavy)):
            if jednotlive_stavy[index] == '':
                jednotlive_stavy[index] = 0
            else:
                jednotlive_stavy[index] = int(jednotlive_stavy[index])
                
        hodnoty = [
            5000, 2000, 1000, 500, 200, 100, 50,
            20, 10, 5, 2, 1
            ] 
            
        stav_kasy = 0
        i = 0
        while i < len(jednotlive_stavy):
            stav_kasy = stav_kasy + (jednotlive_stavy[i] * hodnoty[i])
            i = i + 1
           
        actual_result = (stav_kasy + neuhrazeno + druhakasa + drobne) - (reference + zasilkovna) 
        return actual_result
    # 
    def show_me(self):
        actual_result = self.secti_penize()
        self.e18.delete(0, 20)
        self.e18.insert(0, actual_result)
    def write_backup(self):
        utils.write_backup(self)
    # validation        
    def validate(self, action, index, value_if_allowed,
        prior_value, text, validation_type, trigger_type, widget_name):
        if(action=='1'):
            try:
                int(value_if_allowed) # input must be integer
                return True
            except ValueError: # no allowed input, no entry
                return False
        else:
            return True
    def save_and_quit(self): # save result and difference and then quit
        money = self.secti_penize()
        utils.save_result(self.e17.get(), money)
        master.destroy()
        
   
backup_coins = utils.read_backup()
if __name__ == "__main__":
    master = tk.Tk()
    master.title("Výčetka 1.2")
    hlavni_okno(master)
    master.mainloop()

