def P(n, x):


    if n == 0:
        return 1
    if n == 1:
        return x

    return ((2 * n - 1)  * P(n - 1, x) - (n - 1) * P(n - 2, x)) / n


def main():
    n = int(input("Введите порядок полинома n: "))
    x = float(input("Введите значение x: "))

    print(P(n, x))



def other_main():
    n = int(input("Введите порядок полинома n: "))
    x = float(input("Введите значение x: "))
    P_0 = 1
    P_1 = x
    P_n = 0
    for n in range(2, n + 1):
        P_n = ((2 * n - 1) * P_1 - (n - 1) * P_0) / n
        P_0 = P_1
        P_1 = P_n
    print(P_n)

main()
other_main()