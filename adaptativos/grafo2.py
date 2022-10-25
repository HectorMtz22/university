import networkx as nx

DG = nx.DiGraph()
DG.add_edge('a', 'b', weight=2)
DG.add_edge('a', 'c', weight=1)
DG.add_edge('a', 'd', weight=1)
DG.add_edge('c', 'b', weight=1)
DG.add_edge('c', 'd', weight=2)
DG.add_edge('d', 'c', weight=2)

print("Nodos de la red:", list(DG.nodes()))

pesos = nx.pagerank(DG, alpha = 0.85)
print("Peso del vertice a:", pesos['a'])
print("Peso del vertice b:", pesos['b'])
print("Peso del vertice c:", pesos['c'])
print("Peso del vertice d:", pesos['d'])
