# TEXT WIDGET
#AIDES: http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel
#AIDES: http://www.jchr.be/python/tkinter.htm#scrollbar

try :
    from Tkinter import * #Python Version 2
    pass
except:
    from tkinter import * #Python Version 3

fenetre = Tk()    

scrollbar = Scrollbar(fenetre)                                #Création/Déclaration d'une variable Scrollbar(dans la fenêtre MASTER)
scrollbar.pack(side=RIGHT, fill=Y)                          #Placement de la Scollbar dans la fenêtre

texte0=Text(fenetre, yscrollcommand=scrollbar.set)
texte0.insert(END, "bla bla bla "*3)
texte0.insert(END, "\n"+"BOUHHHHHHHHHH"*2 + "\n")
texte0.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=texte0.yview)

fenetre.mainloop()
