from pulp import *
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#Muesta el conjunto minimo de vertices
def minVertex(vertex):
    print("Minimum vertex cover: \n{",end="")
    for v in V:
        if x[v].varValue > 0:
            print(v,end=",")
    print(end="\b}")

# Conjunto de vértices
V = [1, 2, 3, 4, 5]

# Conjunto de aristas
E = [(1,2), (2,4), (3,4), (5,1), (5,3), (5,4)]

# Crear el problema de minimización
prob = LpProblem("VertexCover", LpMinimize)

# Variables binarias para indicar si un vértice está en la cobertura
x = LpVariable.dicts("x", V, 0, 1, LpBinary)

# Función objetivo: minimizar el tamaño de la cobertura
prob += lpSum([x[i] for i in V])

# Restricciones: cada arista debe ser cubierta por al menos un vértice
for (i,j) in E:
    prob += x[i] + x[j] >= 1

# Resolver el problema
prob.solve()

# Crear un grafo con NetworkX
G = nx.Graph()
G.add_nodes_from(V)
G.add_edges_from(E)


node_colors = ['gray' if value(x[i]) > 0 else 'lightgray' for i in V]
nx.draw(G, with_labels=True, node_color=node_colors)

gray_patch = mpatches.Patch(color='gray', label='En la cobertura')
lightGray_patch = mpatches.Patch(color='lightgray', label='No en la cobertura')

plt.legend(handles=[lightGray_patch, gray_patch])

plt.show()
minVertex(V)

