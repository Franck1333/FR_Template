#Aides: http://effbot.org/tkinterbook/scrollbar.htm


try :
    from Tkinter import * #Python Version 2
    pass
except:
    from tkinter import * #Python Version 3
 
def version1():
    
    master = Tk()                                               #Création de la Fenêtre MASTER

    scrollbar = Scrollbar(master)                               #Création/Déclaration d'une variable Scrollbar(dans la fenêtre MASTER)
    scrollbar.pack(side=RIGHT, fill=Y)                          #Placement de la Scollbar dans la fenêtre 

    listbox = Listbox(master, yscrollcommand=scrollbar.set)     #Liaison de la ScrollBar à son objet relié à la fenêtre MASTER
    for i in range(1000):
        listbox.insert(END, str(i))
    listbox.pack(side=LEFT, fill=BOTH)

    scrollbar.config(command=listbox.yview)                     #Configuration de la Scrollbar par rapport a son objet et de son orientation

    mainloop()


def version2():

    root = Tk()

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(root)
    listbox.pack()

    for i in range(100):
        listbox.insert(END, i)

    # attach listbox to scrollbar
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    mainloop()


if __name__ == "__main__":
    #version1()
    version2()
