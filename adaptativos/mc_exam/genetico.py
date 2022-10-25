from math import floor
import random
p1 = []
p2 = []

def generar():
    p1.clear()
    p2.clear()
    for i in range(0, 5):
        p1.append(random.randint(0, 1))
        p2.append(random.randint(0, 1))


generar()
pc = floor(len(p1) / 2) 
h1 = []
h2 = []
n_iterations = 0

while True:
    n_iterations += 1
    h1 = p1[:pc] + p2[pc :]
    h2 = p2[:pc] + p1[pc :]
    # Imprime los hijos
    print("Número de iteraciones =", n_iterations)
    print(h1)
    print(h2)
    print()
    # Verifica si se cumple
    if h1[0] == 1 and h2[0] == 1 and h1[1] == 0 and h2[1] == 0:
        break
    
    if n_iterations % 200 == 0:
        generar()

