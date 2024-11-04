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

even_count = sum(1 for n in ns if n % 2 == 0)
odd_count = sum(1 for n in ns if n % 2 != 0)

print("Четных элементов:", even_count)
print("Нечетных элементов:", odd_count)
