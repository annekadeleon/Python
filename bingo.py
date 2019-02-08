from random import randint

chosen = []

while len(chosen) != 10:
	new = randint(1, 100)
	if new not in chosen:
		chosen.append(new)

print chosen

draft = []


for i in range(1, 100):
	draft.append("_")

for num in chosen:
	draft.insert(num-1, num)

def print_board(board):
	for i in range(100):
			print board[i],
		else:
			print("\n")

print_board(draft)
