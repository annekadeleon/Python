import sys
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

#shows values in chosen
print(chosen)

draft_board = []

#creates 100 values in draft_board
for i in range(1,101):
	#puts chosen numbers in respective index
	if i-1 in chosen:
		draft_board.append(i)
	else:
		draft_board.append(" _")

#function print_board accepts one argument, board, a list
def print_board(board):
	print("Bingo!\nHere's your board:\n")
	#iterates 100 times
	for i in range(100):
		#every 10th number
		if i in [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]:
			#prints value of board at index i
			print(board[i]),
			#prints new line
			print("\n")
		else:
			#prints value of board at index i
			print(board[i]),
	#asks user
	user_input = raw_input("Enter the called number 'q' to quit\n>")
	while user_input.lower() != "q":
		user_input = raw_input("Try again.\n>")
	else:
		print("See you next time.")
		#terminates code
		sys.exit()

#uses draft_board as input into print_board function
print_board(draft_board)
