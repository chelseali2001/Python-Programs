def check(a, val):
	if val in a:
		return True
	else:
		return False

val = int(input("Enter a number: "))

a = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 16, 18, 21, 25, 30]

if (check(a, val)):
	print(str(val) + " is in list a")
else:
	print(str(val) + " is not in list a")
