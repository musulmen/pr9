ns = [3, 8, 1, 6, 4, 9, 2]

print("Исходный список:", ns)

i_min = ns.index(min(ns))
i_max = ns.index(max(ns))

ns[i_min], ns[i_max] = ns[i_max], ns[i_min]

print("Список после замены:", ns)
