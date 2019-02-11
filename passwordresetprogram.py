print("Change password")
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase_pass = 0
lowercase_pass = 0
new_password = ""
while True:
	new_pass1 = raw_input("Enter password twice.\n>")
	new_pass2 = raw_input(">")
	if new_pass1 == new_pass2:
		if len(new_pass1) >= 8:
			for i in range(len(new_pass1)):
				if new_pass1[i] in uppercase:
					uppercase_pass += 1
				elif new_pass1[i] in lowercase:
					lowercase_pass += 1
			if (uppercase_pass < 1) or (lowercase_pass < 1):
				print("Your new password must have at least one uppercase letter and one lowercase letter.")
			else:
				new_passsword = new_pass1
				print("Password succesfully changed.")
				break
		else:
			print("Your new password must be at least 8 characters long.")
	else:
		print("You must enter your new password twice.")
