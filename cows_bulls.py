import random

answer = str(random.randint(1000, 9999))
right = False
count = 0
print(answer)

while right == False:
	val = raw_input("Guess a 4-digit number: ")
	count = count + 1
	cows = 0
	bulls = 0

	if val == answer:
		print("You go it after " + str(count) + " guess(es)")
	else:
		for x in range(4):
			if val[x] == answer[x]:
				cows += 1
			elif val[x] in answer:
				bulls += 1

		print (str(cows) + " cows " + str(bulls) + " bulls")
