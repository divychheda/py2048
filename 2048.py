import random 
import copy
import math
#i had to install getch with #pip install getch (so that user doesnt have to press enter for every input)
import getch
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--n")
parser.add_argument("--w")

args = parser.parse_args()

if args.w == None:
	w = 2048
else :
	x = int(args.w)
	next1 = int(math.pow(2,math.ceil(math.log(x,2))))
	pre = int(math.pow(2,math.floor(math.log(x,2))))
	if (x - pre) > (next1 - x) :
		w = next1
	
	else :
		w = pre 
		

if args.n == None :
	board_size = 4
else:
	board_size = int(args.n)

#building the game board
board = [[0 for i in range(board_size)]for i in range(board_size)]


import os
def clear():
	if os.name == 'posix':
		_ = os.system('clear')

def disp():
	print(f"You need {w} to win")
	largest = board[0][0]
	for row in board:
		for i in row:
			if i > largest:
				largest=i

	max_space = len(str(largest))

	for row in board:
		curr=""
		for i in row:
			#checking the distribution of spaces so that the game-board is not spoiled 
			curr+=(" "*(max_space-len(str(i))+1))+str(i)
		print(curr)

def shiftOneRowLeft(row):

	for k in range(board_size-1):
		for i in range(board_size-1,0,-1):
			if row[i-1] == 0:
				row[i-1] = row[i]
				row[i] = 0

	for i in range(board_size-1):
		if row[i+1] == row[i]:
			row[i] *= 2
			row[i+1] = 0

	for k in range(board_size-1):
		for i in range(board_size-1,0,-1):
			if row[i-1] == 0:
				row[i-1] = row[i]
				row[i] = 0

	return row 

def reverse_order(row):
	revList = []
	for i in range(board_size-1, -1, -1):
		revList.append(row[i])
	return revList

def transpose(curr_board):
	for i in range(board_size):
		for j in range(i, board_size):
			if i != j:
				tmp = curr_board[i][j]
				curr_board[i][j] = curr_board[j][i]
				curr_board[j][i] = tmp
	return curr_board

#shifting all elements for rows left on clicking a
def shift_left(curr_board):
	for i in range(board_size):
		curr_board[i] = shiftOneRowLeft(curr_board[i])
	return curr_board


#shifting left in reverse so - right XD on clicking d 
def shift_right(curr_board):
	for i in range(board_size):
		curr_board[i] = reverse_order(curr_board[i])
		curr_board[i] = shiftOneRowLeft(curr_board[i])
		curr_board[i] = reverse_order(curr_board[i])
	return curr_board

#shifting all elements up on the click of w
def shift_up(curr_board):
	curr_board = transpose(curr_board)
	curr_board = shift_left(curr_board)
	curr_board = transpose(curr_board)
	return curr_board

#shifting all elements down on the click of s
def shift_down(curr_board):
	curr_board = transpose(curr_board)
	curr_board = shift_right(curr_board)
	curr_board = transpose(curr_board)
	return curr_board

played = True

def random2(curr_board):
	row1 = random.randint(0, board_size-1)
	col1 = random.randint(0, board_size-1)

	while not curr_board[row1][col1] == 0:
		row1 = random.randint(0, board_size-1)
		col1 = random.randint(0, board_size-1)

	curr_board[row1][col1] = 2 

def win():
	for row in board:
		if w in row:
			return True
	return False 

def lost():
	tempBoard1 = copy.deepcopy(board)
	tempBoard2 = copy.deepcopy(board)
	tempBoard1 = shift_right(tempBoard1)
	if tempBoard1 == tempBoard2:
		tempBoard1 = shift_up(tempBoard1)
		if tempBoard1 == tempBoard2:
			tempBoard1 = shift_left(tempBoard1)
			if tempBoard1 == tempBoard2:
				tempBoard1 = shift_down(tempBoard1)
				if tempBoard1 == tempBoard2:
					return True
	return False 

clear()
random2(board)
disp()				
while played:
	validn = True

	tempBoard = copy.deepcopy(board)
	if win():
			clear()
			disp()
			print("You've won")
			played = False 
			exit()

	
	n = getch.getch()
	
	if n.lower() == 'w':
		board = shift_up(board)
	
	elif n.lower() == 'a':
		board = shift_left(board)
		
	elif n.lower() == 's':
		board = shift_down(board)	

	elif n.lower() == 'd':
		board = shift_right(board)

	else : 
		validn = False
		
	if not validn :
		clear()
		disp()

	else:
		if tempBoard == board :
			if not win():
				clear()
				disp()
				if lost():
					print("No more possible moves, you've lost")
					played = False 

				else:
					print("Try another move")
			else : 
				clear()
				disp()
				print("You've won")
				played = False 
			

		else :
			clear()
			if win():
				disp()
				print("You've won")
				played = False 


			else:
				random2(board)
				disp()

				if lost():
					print("No more possible moves, you've lost")
					played = False 



