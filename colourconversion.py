binary_to_hex = {
0b0000 : 0,
0b0001 : 1,
0b0010 : 2,
0b0011 : 3,
0b0100 : 4,
0b0101 : 5,
0b0110 : 6,
0b0111 : 7,
0b1000 : 8,
0b1001 : 9,
0b1010 : "A",
0b1011 : "B",
0b1100 : "C",
0b1101 : "D",
0b1110 : "E",
0b1111 : "F"
}

binaries = [1, 2, 4, 8, 16, 32, 64, 128, 256]

RGB = [244, 55, 1]
RGB_binary = []

for value in RGB:
	RGB_binary.append(bin(value))

print RGB_binary

for binary in RGB_binary:
	print len(binary[2::])
	
