state = False
while state == False:
	email_address = raw_input("Enter your email address: ")
	if " " in email_address:
		print "Invalid email address"
	elif ".com" not in email_address:
		print "Invalid email address"
	elif "@" not in email_address:
		print "Invalid email address"
	else:
		print "Email address is valid"
		state = True
