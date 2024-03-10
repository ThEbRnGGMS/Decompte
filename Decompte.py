import time
import os

tmp_sec = int(input("Entre le temps en sec : "))

while tmp_sec != 0:
    tmp_sec -= 1
    time.sleep(1)
    os.system('cls')
    print(tmp_sec)

os.system('cls')
print("temps écouler !!!")