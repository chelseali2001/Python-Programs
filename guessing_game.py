import random

answer = random.randint(1, 9)

right = False

while right == False:
	val = int(input("Guess a number between 1 and 9: "))

	if val == answer:
		print("Yup you got it")
		right = True
	elif val > answer:
			print("Too high")
	elif val < answer:
			print("Too low")
