ns = [1, 5, 2, 7, 3, 8, 4, 10]

result = [ns[i] for i in range(1, len(ns)) if ns[i] > ns[i - 1]]
print("Элементы больше предыдущего:", result)
