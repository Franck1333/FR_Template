
try :
    from Tkinter import * # type: ignore #Python Version 2
    pass
except:
    from tkinter import * #Python Version 3

fenetre0= Tk()

ascenseur0=Scrollbar(fenetre0)
ascenseur0.pack(side= RIGHT, fill=Y)

texte0=Text(fenetre0, yscrollcommand=ascenseur0.set)
texte0.insert(END, "bla bla bla "*443)
texte0.pack(side=LEFT, fill=BOTH)

ascenseur0.config(command=texte0.yview)

fenetre0.mainloop()
