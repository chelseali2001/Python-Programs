def Rev(val):
	return ' '.join(val.split()[::-1])

val = raw_input("Enter a value: ")

print(Rev(val))
