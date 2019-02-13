binary_to_hex = {
"0000" : 0,
"0001" : 1,
"0010" : 2,
"0011" : 3,
"0100" : 4,
"0101" : 5,
"0110" : 6,
"0111" : 7,
"1000" : 8,
"1001" : 9,
"1010" : "A",
"1011" : "B",
"1100" : "C",
"1101" : "D",
"1110" : "E",
"1111" : "F"
}

#binaries = [1, 2, 4, 8, 16, 32, 64, 128, 256]

RGB = []
while len(RGB) != 3:
	for letter in "RGB":
		user_input = raw_input("Enter value for " + letter + ":")
		if (int(user_input) > 255) or (int(user_input) < 0):
			print("RGB values must be between 0 and 255")
			del RGB[:]
			break
		else:
			RGB.append(int(user_input))

for value in RGB:
	if (value > 255) or (value < 0):
		print("RGB values must be between 0 and 255")
		break

RGB_binary = []
full_binary = []
RGB_hex = []
hex_num = "#"

for value in RGB:
	RGB_binary.append(bin(value)[2::])

for binary_number in RGB_binary:
	while len(binary_number) != 8:
		binary_number = "0" + binary_number
	full_binary.append(binary_number)

for binary_number in full_binary:
	hex_num += str(binary_to_hex[binary_number[:4:]])
	hex_num += str(binary_to_hex[binary_number[4::]])

print hex_num
