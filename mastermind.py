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
out = ""

guess = raw_input()
guess = [guess]

if ((nums == guess).all()):
	print("****")
#if (guess[0][0] in nums):
#	out = out + "*"
#elif (guess[0][1] in nums):
#	out = out + "*"
#elif (guess[0][2] in nums):
#	out = out + "*"
#elif (guess[0][3] in nums):
#	out = out + "*"
#else:
#	print "none"
#print out

#if ((guess[0][0] in nums) and (guess[0][1] in nums) and (guess[0][2] in nums) and (guess[0][3] in nums)):
#	print("****")
#else:
#	print("none")

#for char in guess:
#	if ((nums[0][0] in guess) and (nums[0][1] in guess) and (nums[0][2] in guess) and (nums[0][3] in guess)):
#		print("****")
