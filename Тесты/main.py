import csv
import time

inf = float('inf')
start = 0

def dijkstra(G, s):
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

def getPath(f, G): ####в аргументе G добавил

    global d
    n = len(G)
    path = [f]
    while f!=start:
        for v in range(n):
            if d[v] == d[f] - G[f][v]:
                path.append(v)
                f = v
    return path[::-1]

places = ['Яр', 'Глазов', 'Балезино', 'Кез', 'Юкаменское', 'Дебёсы', 'Игра', 'Селты', 'Сюмси', 'Якшур-Бодья', 'Воткинск', 'Ува', 'Вавож', 'Ижевск', 'Завьялово', 'Малая Пурга', 'Можга', 'Сарапул', 'Камбарка', 'Алнаши', 'Грахово', 'Каракулино']
places_dict = {places[i]: i for i in range(len(places))}

with open('graph.csv', encoding='utf-8') as file:
    rows = csv.reader(file)
    graph = []
    for row in rows:
        norm_row = []
        for x in row:
            if x == 'inf':
                norm_row.append(inf)
            else:
                norm_row.append(int(x))
        graph.append(norm_row)


    time.sleep(1)
    print('Яндекс карты по Удмуртии на коленке')
    time.sleep(1)
    print('Доступные места:')
    print(*places, )
    time.sleep(1)
    p_in = input('Выберите пункт отправления: ')
    p_out = input('Выберите пункт назначения: ')
    start = places_dict[p_in]
    end = places_dict[p_out]
    time.sleep(1)
    d = dijkstra(graph, start)
    print(d)
    spis = getPath(end, graph)
    road = [places[x] for x in spis]
    print(f'Маршрут построен: {[places[x] for x in spis]}')