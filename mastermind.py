print ("---MASTERMIND---")

import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
num4 = random.randint(0, 9)

nums = str(num1) + str(num2) + str(num3) + str(num4)
stars = ""
guess = ""
count = 0

print nums

print("Guess the 4 numbers in as few tries possible")

guess = raw_input()

while count < 4:
	if guess[0] == nums[count]:
		stars = stars + "*"
		count += 1

count = 0
while count < 4:
	if guess[1] == nums[count]:
		stars = stars + "*"
		count += 1

count = 0
while count < 4:
	if guess[2] == nums[count]:
		stars = stars + "*"
		count += 1

count = 0
while count < 4:
	if guess[3] == nums[count]:
		stars = stars + "*"
		count += 1

print stars
