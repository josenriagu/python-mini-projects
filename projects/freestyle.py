from random import randint

board = []

for x in range(0,5):
	board.append(["O"]*5)

#print(board)

def print_board(board):
    for row in board:
        print ("0").join(row)

print_board(board)