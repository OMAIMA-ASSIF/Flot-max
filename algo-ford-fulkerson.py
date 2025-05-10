from collections import defaultdict, deque

def ford_fulkerson(graph, source, sink):
    # Initialisation du graphe résiduel
    residual = defaultdict(dict)
    for u in graph:
        for v, cap in graph[u].items():
            residual[u][v] = cap
            residual[v][u] = 0  # Arête inverse

    total_flow = 0

    while True:
        # BFS pour trouver un chemin augmentant
        parent = {}
        queue = deque([source])
        found = False
        
        while queue and not found:
            u = queue.popleft()
            for v, cap in residual[u].items():
                if cap > 0 and v not in parent:
                    parent[v] = u
                    if v == sink:
                        found = True
                        break
                    queue.append(v)
        
        if not found:
            break  # Plus de chemin

        # Calcul du flot minimal
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u

        # Mise à jour des capacités
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u

        total_flow += path_flow

    return total_flow

# Exemple 1 (ex1 td flot max)
graph1 = {
    's': {'a': 3, 'b': 5 ,'c': 2},
    'a': {'d': 2, 'e': 2, 'b': 2},
    'b': {'d': 3, 'e': 1},
    'c': {'b': 3, 'd': 1, 'e': 1, 'f':2},
    'd': {'p': 3, 'e': 4 },
    'e': {'p': 3, 'f': 1},
    'f': {'p': 4},
    'p': {}
}
print("Flot max exemple 1:", ford_fulkerson(graph1, 's', 'p'))

# Exemple 2
graph2 = {
    's': {'1': 16, '2': 13},
    '1': {'2': 10, '3': 12},
    '2': {'4': 14},
    '3': {'t': 20},
    '4': {'t': 4},
    't': {}
}
print("Flot max exemple 2:", ford_fulkerson(graph2, 's', 't'))