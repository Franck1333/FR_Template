# CANVAS
#AIDES: http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel

try :
    from Tkinter import * # type: ignore #Python Version 2
    pass
except:
    from tkinter import * #Python Version 3

fenetre = Tk()    

# canvas

scrollbar = Scrollbar(fenetre)                               #Création/Déclaration d'une variable Scrollbar(dans la fenêtre MASTER)
scrollbar.pack(side=RIGHT, fill=Y)                          #Placement de la Scollbar dans la fenêtre 

canvas = Canvas(fenetre, width=150, height=120, background='yellow',yscrollcommand=scrollbar.set)
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
canvas.pack()

scrollbar.config(command=canvas.yview)                     #Configuration de la Scrollbar par rapport a son objet et de son orientation
