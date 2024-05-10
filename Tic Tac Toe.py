import os
import time

# Initialize the board and player
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

# Define game status flags
Win = 1
Draw = -1
Running = 0
Stop = 1

Game = Running
Mark = 'X'

# Function to draw the Tic-Tac-Toe board
def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print(" | | ")

# Function to check if a position on the board is empty
def CheckPosition(x):
    if board[x] == ' ':
        return True
    else:
        return False

# Function to check if there's a winner or if the game is a draw
def CheckWin():
    global Game

    # Check rows, columns, and diagonals for a win
    if board[1] == board[2] == board[3] != ' ' or \
       board[4] == board[5] == board[6] != ' ' or \
       board[7] == board[8] == board[9] != ' ' or \
       board[1] == board[4] == board[7] != ' ' or \
       board[2] == board[5] == board[8] != ' ' or \
       board[3] == board[6] == board[9] != ' ' or \
       board[1] == board[5] == board[9] != ' ' or \
       board[3] == board[5] == board[7] != ' ':
        Game = Win
    # Check for a draw
    elif all(board[i] != ' ' for i in range(1, 10)):
        Game = Draw
    else:
        Game = Running

print("Tic-Tac-Toe Game")
print("Player 1 [X] --- Player 2 [O]\n")
print("Please Wait...")
time.sleep(3)

# Main game loop
while Game == Running:
    os.system('cls')  # Clear the console
    DrawBoard()

    # Determine current player and mark
    if player % 2 != 0:
        print("Player 1's turn")
        Mark = 'X'
    else:
        print("Player 2's turn")
        Mark = 'O'

    # Get player input for the position to mark
    choice = int(input("Enter the position [1-9] to mark: "))
    if 1 <= choice <= 9 and CheckPosition(choice):
        board[choice] = Mark
        player += 1
        CheckWin()

    os.system('cls')  # Clear the console
    DrawBoard()

    # Display game result
    if Game == Draw:
        print("Game Draw")
    elif Game == Win:
        player -= 1
        if player % 2 != 0:
            print("Player 1 Wins")
        else:
            print("Player 2 Wins")
