res = []
n = int(input("Ingresa la cantidad de números: "))

for i in range(0, n):
    res.append(int(input(f"Ingresa el número {i}: ")))

print('\nEl arreglo total es:\n' + str(res))