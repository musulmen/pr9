import numpy as np

while True:
    try:
        a = input("Введите число a: ").replace(',', '.')
        b = input("Введите число b: ").replace(',', '.')
        a = float(a)
        b = float(b)
        if a > b:
            a, b = b, a
        start = int(np.ceil(a))
        end = int(np.floor(b))
        c = [i**2 for i in range(start, end + 1)]
        print(c)
        break
    except ValueError:
        print("Ошибка: введите корректные числа.")
