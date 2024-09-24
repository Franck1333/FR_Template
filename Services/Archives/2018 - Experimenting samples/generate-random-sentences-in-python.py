import random

#Aides : https://stackoverflow.com/questions/29938804/generate-random-sentences-in-python

#Génération aléatoire d'une Phrase en Anglais --DEBUT--
nouns = ("puppy", "car", "rabbit", "girl", "monkey")                            #Liste de Noms utilisables
verbs = ("runs", "hits", "jumps", "drives", "barfs")                            #Liste de Verbes utilisables
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")     #Liste d'adverbes utilisables 
adj = ("adorable", "clueless", "dirty", "odd", "stupid")                        #Liste d'adjectifs utilisables
num = random.randrange(0,5)                                                     #Méthode permettant la génération de la phrase aléatoirement et la stock dans une variable 'num'
print (nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num])         #Affichage de la Phrase générer aléatoirement
#Génération aléatoire d'une Phrase en Anglais --FIN--
