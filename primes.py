def Prime(num, counter):
	if num == 1:
		return False
	elif num == 2:
		return True
	elif num == counter:
		return True
	else:
		if num % counter == 0:
			return False
		else:
			return Prime(num, counter + 1)


num = int(input("Enter a number: "))

if (Prime(num, 2)):
	print(str(num) + " is a prime number")
else:
	print(str(num) + " is not a prime number")
