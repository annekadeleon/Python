print("Reset password")
#list of uppercase letters
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#list of lowercase letters
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#initialisation
uppercase_pass = 0
lowercase_pass = 0
new_password = ""

#loops until condition is changed to False
while True:
	#requires two inputs from user
	new_pass1 = raw_input("Enter password twice.\n>")
	new_pass2 = raw_input(">")
	#checks if both inputs are equal
	if new_pass1 == new_pass2:
		#checks if input is at least 8 characters long
		if len(new_pass1) >= 8:
			#iterates as many times as the length of new_pass1
			for i in range(len(new_pass1)):
				#checks if each letter is in uppercase
				if new_pass1[i] in uppercase:
					#adds one if letter is uppercase
					uppercase_pass += 1
				#checks if each letter is in lowercase
				elif new_pass1[i] in lowercase:
					#adds one if letter is lowercase
					lowercase_pass += 1
			#checks if password has at least 1 uppercase and 1 lowercase letter
			if (uppercase_pass < 1) or (lowercase_pass < 1):
				print("Your new password must have at least one uppercase letter and one lowercase letter.")
			else:
				new_passsword = new_pass1
				print("Password succesfully changed.")
				#stops loop
				break
		#if user's input is less than 8 characters long, loop starts again
		else:
			print("Your new password must be at least 8 characters long.")
	#if user's two inputs are not equal, loop starts again
	else:
		print("You must enter your new password twice.")
