# -*- coding: utf-8 -*-
#https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/2235545-faites-de-la-programmation-parallele-avec-threading

import random
import sys
from threading import Thread
import time

class Afficheur(Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 20:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            i += 1

# Création des threads
thread_1 = Afficheur("1")
thread_2 = Afficheur("2")
thread_7 = Afficheur("7")

# Lancement des threads
thread_1.start()
thread_2.start()
thread_7.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()
thread_7.join()
