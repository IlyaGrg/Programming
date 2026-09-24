def New_string(s, a):
    S = ''
    for i in range(0, len(a) - 1):
        if i == 0:
            S += s[0:a[i + 1]]
        else:
            S += s[a[i] + 1:a[i + 1]]
    new_string = ''
    for i in S:
        new_string += i * 2
    return new_string

s = input("Введите строку, которая заканчивается точкой: ")
print(f'Длина строки: {len(s)}')
print(f'Кол-во слов в строке: {len(s[:-1].split())}')
print(f'Длина самого длинного слова: {max([len(x) for x in s[:-1].split()])}')
print(f'Длина самого короткого слова: {min([len(x) for x in s[:-1].split()])}')
a = [i for i in range(len(s)) if s[i] == '*']
a.insert(0,0)
a.append(len(s))
print(f'Новая строка: {New_string(s,a)}')