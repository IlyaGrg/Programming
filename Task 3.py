from random import randint
n = int(input("Введите длину массива: "))
a = [randint(-20, 20) for i in range(n)]
print(f'Исходный список: {a}')

A = min([i for i in a if i > 0])
B = max([i for i in a if i < 0])
print(f'Наименьший положительный элемент: {A}')
print(f'Наибольший отрицательный элемент: {B}')
index_A = 0
index_B = 0
for i in range(n):
    if a[i] == A:
        index_A = i
    if a[i] == B:
        index_B = i

if index_A < index_B:
    del a[index_A + 1: index_B]
else:
    del a[index_B + 1: index_A]
print(f'Результирующий список: {a}')

