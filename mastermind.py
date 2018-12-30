print ("---MASTERMIND---")

import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
num4 = random.randint(0, 9)

nums = str(num1) + str(num2) + str(num3) + str(num4)
stars = ""
guess = ""

print nums

print("Guess the 4 numbers in as few tries possible")

guess = raw_input(">")

while stars != "****":
	for num in guess:
		if num == guess[0]:
			stars = stars + "*"
		elif num == guess[1]:
			stars = stars + "*"
		elif num == guess[2]:
			stars = stars + "*"
		elif num == guess[3]:
			stars = stars + "*"
		else:
			print("wrong")
	print stars


#while stars != "****":
#	guess = raw_input(">")
#	if (nums[0]in guess)
#	elif nums[0] in guess:
#		stars = stars + "*"
#		print "stars: " + stars
#	elif nums[1] in guess:
#		stars = stars + "*"
#		print "stars: " + stars
#		print stars
#	elif nums[2] in guess:
#		stars = stars + "*"
#		print "stars: " + stars
#	elif nums[3] in guess:
#		stars = stars + "*"
#		print "stars: " + stars
#	else:
#		print "try again"#
