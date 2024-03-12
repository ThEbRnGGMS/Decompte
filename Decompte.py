import time
import os
from datetime import datetime

mode = int(input("Veux tu l'heure (1) ou un decompte (2) ? "))

if mode == 1:
    heure_actuelle = datetime.now().strftime("%H:%M:%S")
    print("L'heure actuelle est :", heure_actuelle)

if mode == 2:
    
    tmp_sec = int(input("Entre le temps en sec : "))

    while tmp_sec != 0:
        tmp_sec -= 1
        time.sleep(1)
        os.system('cls')
        print(tmp_sec)

    os.system('cls')
    print("temps écouler !!!")
