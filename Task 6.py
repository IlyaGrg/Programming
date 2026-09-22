from random import randint
n = int(input("Введите количество строк в матрице: "))
m = int(input("Введите количество столбцов в матрице: "))
z = int(input("Введите кол-во матриц: "))
T = [[[randint(-10,10) for i in range(z)] for j in range(n)]for k in range(m)]
for i in range(n):
    for j in range(m):
        for k in range(z):
            print(f'{T[i][j][k]}', end=' ')
        print(f'\n')
    print(f'\n')
maximum = -1e9
indexes = []
for i in range(n):
    for j in range(m):
        for k in range(z):
            if T[i][j][k] > maximum:
                maximum = T[i][j][k]
                indexes = [i,j,k]
print(f'Максимальный элемент равен: {maximum}, Индексы равны: {indexes}')