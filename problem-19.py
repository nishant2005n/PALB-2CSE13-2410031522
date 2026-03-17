a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 7]

set_a = set(a)
is_subset = all(x in set_a for x in b)

print("Is subset:", is_subset)