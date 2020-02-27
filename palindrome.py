val = raw_input("Enter a string: ")

rvs = val[::-1]

if val == rvs:
	print(val + " is a palindrome")
else:
	print(val + " is not a palindrome") 
