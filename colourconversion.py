#not done
binary_to_hex = {
0000 : 0,
0001 : 1,
0010 : 2,
0011 : 3,
0100 : 4,
0101 : 5,
0110 : 6,
0111 : 7,
1000 : 8,
1001 : 9,
1010 : "A",
1011 : "B",
1100 : "C",
1101 : "D",
1110 : "E",
1111 : "F"
}

#binaries = [1, 2, 4, 8, 16, 32, 64, 128, 256]

RGB = [255, 100, 1]
RGB_binary = []
full_binary = []
RGB_hex = []

for value in RGB:
	RGB_binary.append(bin(value)[2::])

print RGB_binary

for binary_number in RGB_binary:
	while len(binary_number) != 8:
		binary_number = "0" + binary_number
	full_binary.append(binary_number)

print full_binary

for binary_number in full_binary:
		print binary_to_hex[int(binary_number[:4:])], binary_to_hex[int(binary_number[4::])]
