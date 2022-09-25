import networkx as nx
import numpy as np

N, X, Y = map(int, input().split())

G = nx.Graph()
G.add_edges_from([tuple(map(int, input().split())) for _ in range(N-1)])

print(*nx.shortest_path(G, source=X, target=Y))
