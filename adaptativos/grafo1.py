import sys

m = 0
grados = []

try:
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    f.close()
except IOError:
    print("No se pudo leer el archivo correctamente")
    sys.exit(1)

n = len(lines)

for line in lines:
    line = line.strip()
    cells = line.split()
    grado = 0
    for cell in cells:
        m += int(cell)
        grado = grado + int(cell)
        grados.append(grado)


# Formula
m = m / 2

# Formula de densidad
density = 2 * m / (n * (n - 1))

print('# de Vertices - Personas (n):', n)
print('# de Aristas - Amistades (n)', m)
print('Densidad:', density)

for i in range(len(grados)):
    centralidad = grados[i] / (n - 1)
    print(f'Grado v {i} = {grados[i]}: Centralidad: {centralidad}')
