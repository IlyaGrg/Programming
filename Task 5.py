from random import randint
n = int(input("Введите количество строк в матрице: "))
m = int(input("Введите количество столбцов в матрице: "))
N = int(input("Введите число, для которого будем искать кратные числа в матрице: "))

M = [[randint(-10,10) for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        print(f'{M[i][j]}', end=' ')
    print(f'\n')
flag = True
for i in range(n):
    for j in range(m):
        if M[i][j] % N == 0:
            print(f'Элемент равен: {M[i][j]}\n')
            print(f'Индексы элемента равны: {i, j}\n')
            print(f'Степень кратности равна: {M[i][j] // N}\n')
            flag = False
            break
    if flag == False:
        break


