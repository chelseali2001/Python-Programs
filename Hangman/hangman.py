import random

with open('sowpods.txt') as f:
	words = list(f)

answer = random.choice(words).strip()
win = False
letters = []
errors = 0
an = []

for x in range(len(answer)):
	an.append("")

while win == False:
	val = raw_input("Enter a letter: ")

	if val == answer: 
		print("You got it, after " + str(errors) + " error(s)")
		win = True
	elif "" not in an:
		print("You got it, after " + str(errors) + " error(s)")
		win = True
	else:
		if val not in answer:
			errors += 1
			print(str(errors) + " error(s)")
			letters.append(val)
		elif val in answer:
			if val not in an:
				letters.append(val)
				
			for x in range(len(answer)):
				if val == answer[x]:
					an[x] = val

		print(an)
