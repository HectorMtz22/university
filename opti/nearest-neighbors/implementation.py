import numpy as np
import fileinput

# Colores ANSI
COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_BLUE = '\033[94m'
COLOR_RESET = '\033[0m'

def printTSP(names, nodes, cost):
    for node in nodes[:-1]:
        name = names[node]
        print(name, end=" -> ")

    print(names[nodes[-1]])


    print(COLOR_RED + "Costo total:", COLOR_RESET, cost)


# loop through all lines
lines = []
isThereNodes = False
num_nodes = 0
for line in fileinput.input():
    if (isThereNodes):
        lines.append(line)
    else:
        if line.startswith("NODE_COORD_SECTION"):
            isThereNodes = True
        
        if line.startswith("DIMENSION"):
            num_nodes = int(line.split(',')[1])

# Lectura de datos de entrada desde el archivo
# num_nodes = int(lines[0].split(',')[1])
node_coords = np.zeros((num_nodes, 2))
node_names = []
for i in range(num_nodes):
    node_info = lines[i].split(',')
    node_names.append(node_info[0])
    node_coords[i] = [float(node_info[1]), float(node_info[2])]

# Cálculo de la matriz de distancias entre todos los nodos
dist_matrix = np.zeros((num_nodes, num_nodes))
for i in range(num_nodes):
    for j in range(i+1, num_nodes):
        dist_matrix[i][j] = np.linalg.norm(node_coords[i] - node_coords[j])
        dist_matrix[j][i] = dist_matrix[i][j]

# Algoritmo del vecino más cercano
print(COLOR_GREEN + "Algoritmo vecino mas cercano" + COLOR_RESET)
visited = [np.random.randint(num_nodes)]
print("El primer nodo es: ", node_names[visited[0]])
while len(visited) < num_nodes:
    last_node = visited[-1]
    min_dist = float("inf")
    for i in range(num_nodes):
        if i not in visited and dist_matrix[last_node][i] < min_dist:
            min_dist = dist_matrix[last_node][i]
            next_node = i
    visited.append(next_node)
    print("El nodo", node_names[next_node], "es el mas cercano. Lo agregamos")

tour = visited + [visited[0]]

# Cálculo del costo total del recorrido
cost = 0
for i in range(num_nodes):
    cost += dist_matrix[tour[i]][tour[i+1]]

print(COLOR_BLUE + "Ruta con algoritmo mas cercano" + COLOR_RESET)
printTSP(node_names, tour, cost)


print("\n Mejora 2-opt")
# Aplicación de la mejora 2-opt
improved = True
while improved:
    improved = False
    for i in range(1, num_nodes-1):
        for j in range(i+1, num_nodes):
            new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
            new_cost = 0
            for k in range(num_nodes):
                new_cost += dist_matrix[new_tour[k]][new_tour[k+1]]
            if new_cost < cost:
                print("Mejora intercambiando", node_names[tour[i]], node_names[tour[j]])
                tour = new_tour
                cost = new_cost
                improved = True
                printTSP(node_names, tour, cost)
                break
        if improved:
            break

# Impresión del tour y su costo
# print("Tour TSP:", tour)

print(COLOR_BLUE + "\nRuta final encontrada por el algoritmo" + COLOR_RESET)
printTSP(node_names, tour, cost)