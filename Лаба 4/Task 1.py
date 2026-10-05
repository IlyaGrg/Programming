


def graph(n):
    arr = []
    print('Введите связи: ',end ='')
    x, y = map(int, input().split())
    arr.append([x, y])
    while True:
        try:
            print("Введите связи:", end = ' ')
            x, y = map(int, input().split())
            arr.append([x, y])
        except ValueError:
            break
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i, j in arr:
        matrix[i][j] = 1
        matrix[j][i] = 1
    for i in matrix:
        print(i, sep=' ')
    return matrix


def check_pitiels(arr, n):
    summ = 0
    for i in range(n):
        for j in range(n):
            summ += arr[i][i]
    if summ > 0:
        print("В графе есть петли")
    else:
        print("В графе нет петель")



def check_smez(arr, n):
    for i in range(n):
        flag = False
        summ = 0
        for j in range(n):
            summ += arr[i][j]
        if summ == 0:
            print("В графе есть вершины, не смежные с другими")
            flag = True
            break
        if flag == True:
            break
    else:
        print('В графе нет врешин, не смежных с другими')



def print_v(arr, n):
    a = []
    for i in range(n):
        print(f'Для вершины {i} смежные вершины: ')
        k = 0
        for j in range(n):
            if arr[i][j] == 1:
                print(f'{j} ', end=' ')
                k += 1
        if k == 0:
            print('Отсутствуют')

        print(f'\n')



def check_max(arr, n):
    flag = False
    for i in range(n):
        summ = 0
        for j in range(n):
            summ += arr[i][j]
        if summ == n or (summ == n - 1 and arr[i][i] == 0):
            print('В графе есть вершина, смежная со всеми')
            flag = True
            break
        if flag == True:
            break
    else:
        print('В графе нет вершин, смежных со всеми')

def print_s(arr, n):
    a = []
    for i in range(n):
        k = 0
        for j in range(n):
            if arr[i][j] == 1:
                k += 1
        print(f'Степень вершины {i} равна {k}')
        if k == 1:
            a.append(i)
    print(f'Вершины со степенью 1: {a}')



def sm_maximum(arr, n):
    maximum = -1
    for i in range(n):
        k = 0
        for j in range(n):
            if arr[i][j] == 1:
                k += 1
        maximum = max(maximum, k)
    print(f"Степень графа равна {maximum} ")

def main():
    n = int(input("Введите количество вершин: "))
    matrix = graph(n)
    check_pitiels(matrix, n)
    check_smez(matrix, n)
    print_v(matrix, n)
    check_max(matrix, n)
    print_s(matrix, n)
    sm_maximum(matrix, n)





main()