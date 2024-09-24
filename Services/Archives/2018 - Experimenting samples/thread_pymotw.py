import time
import threading

def chocolat():
    print('Chocolat')

def vanille():
    print('Vanille')

choco_thread = threading.Thread(target=chocolat)
vanille_thread = threading.Thread(target=chocolat)



if __name__ == "__main__":
    choco_thread = threading.Thread(target=chocolat)
    vanille_thread = threading.Thread(target=chocolat)

    choco_thread.start()
    vanille_thread.start()
