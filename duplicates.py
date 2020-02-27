a = [1, 1, 1, 2, 3, 3, 4, 4, 5, 9, 11, 20]
b = []

for x in a:
	if x not in b:
		b.append(x)

print(b)
