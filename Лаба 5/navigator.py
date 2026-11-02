inf = float('inf')
start = 0


def djkstra(G, s):
    n = len(G)
    Q = [(0, s)]
    d = [inf for i in range(n)]
    d[s] = 0
    while len(Q) != 0:
        (cost, u) = Q.pop(0)

        for v in range(n):
            if d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                Q.append((d[v], v))
    return d


def getPath(f, G):

    global d
    n = len(G)
    path = [f]
    while f != start:
        for v in range(n):
            if d[v] == d[f] - G[f][v]:
                path.append(v)
                f = v
    return path[::-1]

