sum = 0
n = int(input("Ingresa la cantidad de números: "))

for _ in range(0, n):
    temp = input("Ingresa el número: ")
    sum += int(temp)

print(sum)