def fib(num):
	if num == 1:
		return [1]
	elif num == 2:
		return [1, 1]
	else:
		fib = [1, 1]

		for x in range(1, num - 1):
			fib.append(fib[x] + fib[x - 1])

		return fib

num = int(input("How many Fibonacci numbers do you want: "))

print(fib(num))
