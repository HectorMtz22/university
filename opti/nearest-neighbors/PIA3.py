import csv
import math
import sys

def distancia(coord1, coord2):
    """
    Calcula la distancia euclidiana entre dos coordenadas.
    """
    return math.sqrt((coord2['x'] - coord1['x'])**2 + (coord2['y'] - coord1['y'])**2)

def encontrar_ruta_corta(clientes, punto_partida):
    """
    Encuentra la ruta óptima utilizando el algoritmo del Vecino más Cercano.
    """
    ruta = [punto_partida] 
    clientes_restantes = clientes.copy()

    while clientes_restantes:
        cliente_actual = ruta[-1]
        distancia_minima = sys.maxsize
        cliente_mas_cercano = None

        for cliente in clientes_restantes:
            d = distancia(cliente_actual, cliente)
            if d < distancia_minima:
                distancia_minima = d
                cliente_mas_cercano = cliente

        ruta.append(cliente_mas_cercano)
        clientes_restantes.remove(cliente_mas_cercano)

    return ruta


clientes = []
punto_partida = None

with open('pia_problema.csv', 'r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)

    try:
        for fila in lector_csv:
            try:
                coord_x = int(float(fila['x']))
                coord_y = int(float(fila['y']))
                nombre_cliente = fila['nombre']
                clientes.append({'x': coord_x, 'y': coord_y, 'nombre': nombre_cliente})
            except ValueError:
                print(f"Error al leer las coordenadas en la fila: {fila}. Saltando fila...")

        punto_partida = clientes[0] 

    except StopIteration:
        print("El archivo CSV está vacío.")

ruta_optima = encontrar_ruta_corta(clientes, punto_partida)
ruta_optima.append(punto_partida) 
ruta_optima.pop(0)  

print("Ruta óptima:")
for cliente in ruta_optima:
    print(f"Cliente: {cliente['nombre']} - ({cliente['x']},{cliente['y']})")

