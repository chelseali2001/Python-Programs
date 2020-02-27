import random

a = ["r", "p", "s"]

done = False

while (done == False):
	val = raw_input("Enter 'r' for rock, 'p' for paper' or 's' for scissors: ")
	opp = random.choice(a)

	print("Your opponent chose " + opp)

	if opp == val:
		print("It's a tie")
	else:
		if opp == "r":
			if val == "p":
				print("You win")
			elif val == "s":
				print("You lose")
		elif opp == "p":
			if val == "r":
				print("You lose")
			elif val == "s":
				print("You win")
		elif opp == "s":
			if val == "r":
				print("You win")
			elif val == "p":
				print("You lose")

	newVal = int(input("Enter 1 if you want to play again, 2 if you want to quit: "))

	if newVal == 2:
		done = True
