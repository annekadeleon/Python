print ("---MASTERMIND---")

import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
num4 = random.randint(0, 9)

nums = [num1, num2, num3, num4]
print nums

print("Guess the 4 numbers in as few tries as possible")

count = 0

while count <= 4:
	guess = raw_input()
	for char in guess:
		if int(char) == nums[count]:
			print("*")
	count += 1

#if difficulty.lower() = "a" or "easy":
#	print("Guess the number in as few tries as possible")
#	num = randint(0, 9)
#	guess = raw_input()
#	if int(guess) == num:
#		score += 1
#		print("Well done!")
#	elif int(guess) != num:
#		print("Sorry!")
#	else:
#		print("Wrong input!")
