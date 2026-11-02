import csv
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


with open("graph_matrix.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=";")
    graph = []
    for row in rows:
        new_row = []
        for x in row:
            if x == 'inf':
                new_row.append(inf)
            else:
                new_row.append(int(x))
        graph.append(new_row)


start = int(input("Введите начальную точку: ")) - 1
end = int(input("Введите пункт назначения: ")) - 1
d = djkstra(graph, start)
print(d)
getPath(end, graph)
print(getPath(end, graph))
