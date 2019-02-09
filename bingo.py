from random import randint

#empty list
chosen = []

#loops until chosen has 10 values
while len(chosen) < 10:
	#puts random number from 1-100 into variable new
	new = randint(1, 100)
	#makes sure number is not repeated
	if new not in chosen:
		chosen.append(new)

print(chosen)

draft_board = []

#creates 100 values in draft_board
for i in range(1,101):
	#puts chosen numbers in respective index
	if i-1 in chosen:
		draft_board.append([i])
	else:
		draft_board.append(["_"])

print(len(draft_board))

#print draft_board

def print_board(board):
	for i in range(100):
		if i in [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]:
			print(board[i]),
			print("\n")
		else:
			print(board[i]),

print_board(draft_board)
