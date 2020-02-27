def findMax(val, maxVal):
	for x in val:
		if x > maxVal:
			return findMax(val, x)

	return maxVal

val = [0, 0, 0]

val[0] = int(input("Enter the 1st number: "))
val[1] = int(input("Enter the 2nd number: "))
val[2] = int(input("Enter the 3rd number: "))

maxVal = val[0]

print("Max value is " + str(findMax(val, maxVal)))
