from random import randint
n = int(input('Введите длину массива: '))
a = [randint(-10, 10) for i in range(n)]

index = 0
k = 0
print(a)
maximum = -1
for i in range(0, len(a)):
    if a[i] > 0:
        k += 1
        if k > maximum:
            maximum = k
            index = i
    else:
        k = 0
result = a[index - maximum + 1: index + 1]
del a[index - maximum + 1: index + 1]
print(f'Наибольшая группа: {result}')
print(f'Итоговый массив {a + result}')




