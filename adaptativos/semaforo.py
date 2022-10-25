import time
import os
from random import randrange 

# define an alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
CRUCES = 8

next_move = 2
cruces = [] 

carriles_en_verde = [
    [0,0,1,0,0,0,1,0], 
    [1,0,1,0,0,0,0,0], 
    [1,0,0,0,1,0,0,0], 
    [0,1,0,0,0,1,0,0],
    [0,1,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,1]
]

def iniciar():
    cruces.clear()
    for i in range(CRUCES):
        cruces.append(randrange(0, 15))
        print("Cruce", ALPHABET[i], "tiene:", cruces[i], "carros.")

    print("\n")

        
def semaforo():
    for i, data in enumerate(carriles_en_verde):
        next_move = adjustTime(data, cruces)
        print("Iteración", i)
        for index, value in enumerate(data):
            if value == 1:
                print("Cruce", ALPHABET[index], "tiene luz verde.")
            else:
                print("Cruce", ALPHABET[index], "tiene luz roja.")
            #print("Cruce", ALPHABET[index], "tiene:", cruces[index], "carros.")
        
        print("tiempo (en minutos):", next_move)
        time.sleep(next_move)
        os.system('cls' if os.name == 'nt' else 'clear')

def adjustTime(data, cruces):
    for index, value in enumerate(data):
        if value == 1:
            if cruces[index] > 5:
                return next_move + 1
            else:
                return next_move - 1
        

    return 2
        

while True:
    iniciar()
    semaforo()
