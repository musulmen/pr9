ns = []

while True:
    b = input("Введите число (или 'end' для завершения): ")
    if b.lower() == 'end':
        break
    b = b.replace(',', '.')  
    try:
        c = float(b)
        if not c.is_integer():
            print("Ошибка: вещественное число не может быть четным или нечетным.")
            continue
        ns.append(int(c))
    except ValueError:
        print("Ошибка: введите корректное число.")

d = [n for n in ns if n % 2 != 0]
print("Нечетные элементы списка:", d)
