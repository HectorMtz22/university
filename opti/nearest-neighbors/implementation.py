import numpy as np

# Lectura de datos de entrada desde el archivo
with open("input.txt", "r") as f:
    lines = f.readlines()
    num_nodes = int(lines[0].split()[1])
    node_coords = np.zeros((num_nodes, 2))
    for i in range(num_nodes):
        node_info = lines[i+3].split()
        node_coords[i] = [float(node_info[1]), float(node_info[2])]

# Cálculo de la matriz de distancias entre todos los nodos
dist_matrix = np.zeros((num_nodes, num_nodes))
for i in range(num_nodes):
    for j in range(i+1, num_nodes):
        dist_matrix[i][j] = np.linalg.norm(node_coords[i] - node_coords[j])
        dist_matrix[j][i] = dist_matrix[i][j]

# Algoritmo del vecino más cercano
visited = [np.random.randint(num_nodes)]
while len(visited) < num_nodes:
    last_node = visited[-1]
    min_dist = float("inf")
    for i in range(num_nodes):
        if i not in visited and dist_matrix[last_node][i] < min_dist:
            min_dist = dist_matrix[last_node][i]
            next_node = i
    visited.append(next_node)
tour = visited + [visited[0]]

# Cálculo del costo total del recorrido
cost = 0
for i in range(num_nodes):
    cost += dist_matrix[tour[i]][tour[i+1]]

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
                tour = new_tour
                cost = new_cost
                improved = True
                break
        if improved:
            break

# Impresión del tour y su costo
print("Tour TSP:", tour)
print("Costo total:", cost)
