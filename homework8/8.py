import random

t = [
    [5, 12, 19, 26, 33],
    [7, 14, 21, 28, 35],
    [9, 16, 23, 30, 37],
    [11, 18, 25, 32, 39],
    [13, 20, 27, 34, 41],
]

u = []

for r in t:
    while True:
        try:
            n = int(input(f"Выберите число из {r}: "))
            if n in r:
                u.append(n)
                break
            else:
                print("Неверный ввод. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число.")

s = [random.choice(r) for r in t]

print("\nВаши числа:", u)
print("Случайно выбранные числа:", s)

m = set(u) & set(s)

if m:
    print("Совпадения:", m)
else:
    print("Совпадения: нет совпадений")

print("Количество совпадений:", len(m))
