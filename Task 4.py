n = int(input('Введите число n, до которого будут искаться простые числа: '))
a = [i for i in range(2, n)]
p = 2
a7 = [x for x in a if x % 7 == 0]
prime = []
while len(a) > 0:
    p = a[0]
    a = [x for x in a if x % p != 0]
    prime.append(p)
print(f'Все числа от 2 до n, кратные 7: {a7}')
print(f'Все простые числа от 2 до n: {prime}')
