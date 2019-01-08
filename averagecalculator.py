nums = []

print("What unit will the average be, and in what rate? \nE.g.\nUnit: Celsius\nRate: 1 week\n")
unit,rate = raw_input("Unit: "), raw_input("Rate: ")

print("Enter a number on a new line to calculate their averages. When done, type 'x'.")

while True:
	num = raw_input(">")
	try:
		if "." in num:
			num = float(num)
		else:
			num = int(num)
		nums.append(num)
	except ValueError:
		if num == "x":
			break
		else:
			print("You must enter a valid number (integer or decimal).")

length = len(nums)
total = 0

for num in nums:
	total += num

print("Total in " + rate + ": " + str(total) + " " + unit)

avg = total / length

print("The average " + unit + " in " + rate + " is " + str(avg) + " " + unit)
