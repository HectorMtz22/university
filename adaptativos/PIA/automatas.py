
def convertir(d):
    r = 1
    if d == '000' or d == '100' or d == '111':
        r = 0
    
    return r

cad = input("input = ")
ran = input("range = ")

t = len(cad)
index = t - 1
print("Longitud: ", t)
r = ""

for i in range(int(ran)):
    aux1 = index
    aux2 = index - index
    aux3 = index - (index - 1)
    cnt = 1
    r = ""

    for j in range(t):
        if aux3 == t:
            aux3 = 0

        l = cad[aux1]
        m = cad[aux2]
        n = cad[aux3]

        n1 = l + m + n
        if cnt == 1:
            aux1 = 0
            aux2 = 1
            aux3 = 2

        else:
            aux1 += 1 
            aux2 += 1
            aux3 += 1
        
        cnt += 1
        r += str(convertir(n1)) 
    
    cad = r
    print(r)

