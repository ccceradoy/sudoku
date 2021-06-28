'''
Terminal-based sudoku. A functional programming approach.
Has the following features:
    - Self-generating board
    - Can save the current state of the game
    - Can load the last saved state of the game from the .txt file

@author: Cid Ceradoy
'''

import random
import os
import copy

def generateBoard():
    # A 2-d array that will store an arrays of rows
    grid = []

    # Generate an array with unique elements ranging from 1-9
    # Serves as the basis for generating a valid sudoku board through shifting
    # elements by 3's
    initialArr = random.sample(range(1, 10), 9)
    
    firstRow = initialArr[3::] + initialArr[:3:]
    grid.append(firstRow)

    secondRow = firstRow[3::] + firstRow[:3:]
    grid.append(secondRow)

    thirdRow = secondRow[3::] + secondRow[:3:]
    grid.append(thirdRow)

    fourthRow = thirdRow[1::] + thirdRow[:1:]
    grid.append(fourthRow)

    fifthRow = fourthRow[3::] + fourthRow[:3:]
    grid.append(fifthRow)

    sixthRow = fifthRow[3::] + fifthRow[:3:]
    grid.append(sixthRow)

    seventhRow = sixthRow[1::] + sixthRow[:1:]
    grid.append(seventhRow)

    eigthRow = seventhRow[3::] + seventhRow[:3:]
    grid.append(eigthRow)

    ninthRow = eigthRow[3::] + eigthRow[:3:]
    grid.append(ninthRow)

    return grid


def displayBoard(board):
    print("0 1 2   3 4 5   6 7 8 |   ")
    print("- - - - - - - - - - - - -")
    print(board[0][0], board[0][1], board[0][2], '|', board[0][3], board[0][4], board[0][5], '|', board[0][6], board[0][7], board[0][8], '|', 0)
    print(board[1][0], board[1][1], board[1][2], '|', board[1][3], board[1][4], board[1][5], '|', board[1][6], board[1][7], board[1][8], '|', 1)
    print(board[2][0], board[2][1], board[2][2], '|', board[2][3], board[2][4], board[2][5], '|', board[2][6], board[2][7], board[2][8], '|', 2)
    print("- - - - - - - - - - - - -")
    print(board[3][0], board[3][1], board[3][2], '|', board[3][3], board[3][4], board[3][5], '|', board[3][6], board[3][7], board[3][8], '|', 3)
    print(board[4][0], board[4][1], board[4][2], '|', board[4][3], board[4][4], board[4][5], '|', board[4][6], board[4][7], board[4][8], '|', 4)
    print(board[5][0], board[5][1], board[5][2], '|', board[5][3], board[5][4], board[5][5], '|', board[5][6], board[5][7], board[5][8], '|', 5)
    print("- - - - - - - - - - - - -")
    print(board[6][0], board[6][1], board[6][2], '|', board[6][3], board[6][4], board[6][5], '|', board[6][6], board[6][7], board[6][8], '|', 6)
    print(board[7][0], board[7][1], board[7][2], '|', board[7][3], board[7][4], board[7][5], '|', board[7][6], board[7][7], board[7][8], '|', 7)
    print(board[8][0], board[8][1], board[8][2], '|', board[8][3], board[8][4], board[8][5], '|', board[8][6], board[8][7], board[8][8], '|', 8)
    print("\n")

# Will cover 50 randomly selected cell by replacing it with "*"
# Each points (row, col) will be stored in an array for checking purposes
def coverBoard(board):
    blank = 0
    while blank < 50:
        board[random.randint(0, 8)][random.randint(0, 8)] = "*"
        blank += 1

# Get the available row-col to be filled
def getArrOfChoice(board):
    arrOfChoices = []

    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == "*":
                arrOfChoices.append((i, j))
    return arrOfChoices

# Check if the cell is already occupied.
# To be used in inputRowCol()
def checkIfOccupied(board, row, col):
    if (board[row][col] == "*"):
        return False
    return True

# Prompt for user input row and col
def inputRowCol(board, arrOfChoices):
    row = 9
    col = 9
    while row and col not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        
        # Check if the (row, col) is from the array of choices or board[row][col] is 
        if (row, col) not in arrOfChoices or board[row][col] != "*":
            print("Invalid row and/or col, choose again")
            row = 9
            col = 9

    return (row, col)

# Prompt for user input and put it in the (row, col) cell.
# Will only be prompted given the row and col is valid
def inputAnswer(board, row, col):
    answer = 0
    while answer not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        answer = int(input("Enter answer: "))
        board[row][col] = answer
    print("\n")

# Delete the content of a cell given that (row, col) is not
# from the given cells.
def deleteAnswer(board, arrOfChoices):
    row = 9
    col = 9
    while row and col not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))

        if (row, col) in arrOfChoices:
            board[row][col] = "*"
            print(f"Row {row}, Col {col} is now back to *")
        
        else:
            print("Invalid row and/or col, choose again.")

# Check if the board is now full.
# One of the determinant in loop
def checkBoardFull(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == "*":
                return False
    return True

# Will just print the original board
def revealSolution(originalBoard):
    displayBoard(originalBoard)

# Save the current state of the game
# Without the [] for easy conversion to array later on
def saveGame(dupBoard, origBoard):
    # Save the duplicate board with "*"'s
    f = open("sudoku.txt", "w+")
    for i in range(0, 9):
        for j in range(0, 9):
            f.write(str(dupBoard[i][j]))
            if (j != 8):
                f.write(",")
        if (i != 8):
            f.write("\n")
    f.close()
    print("Game is saved.")

    # Also save the solution to avoid bug later on
    f = open("solution.txt", "w+")
    for i in range(0, len(origBoard)):
        for j in range(0, len(origBoard)):
            f.write(str(origBoard[i][j]))
            if (j != 8):
                f.write(",")
        if (i != 8):
            f.write("\n")


# Load the game from the .txt file
def loadGame():
    # Will produce an array with rows as elements, presented as strings
    with open("sudoku.txt") as f:
        contents = f.read()
    arr = (contents.split("\n"))

    # Will make the array a 2-d array, elements still a string
    for i in range(0, len(arr)):
        arr[i] = arr[i].split(",")

    # Convert all string to int except the "*"
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if (arr[i][j]) != "*":
                arr[i][j] = int(arr[i][j])
    print("Game is loaded.")

    # Will load the solution
    with open("solution.txt") as f:
        contents = f.read()
    orig = (contents.split("\n"))

    for i in range(0, len(orig)):
        orig[i] = orig[i].split(",")

    for i in range(0, len(orig)):
        for j in range(0, len(orig)):
            orig[i][j] = int(orig[i][j])

    return (arr, orig)
    
# Check if the file exists. If so, then check if it is empty
def checkFile(filePath):
    # Check if it exists, return False if not.
    if not(os.path.exists(filePath)):
        return False

    # Check if it is empty, return False if not.
    if (os.stat(filePath).st_size == 0):
        return False

    return True

# Will prompt when not playing
def pregameChoice():
    print("===== MENU =====")
    print("1. New Game     ")
    print("2. Load Game    ")
    print("3. Exit         ")
    print("================")
    choice = int(input("Choice: "))
    print("\n")

    return choice

# Will prompt when playing
def ingameChoice():
    print("===== MENU =====")
    print("1. Make a move  ")
    print("2. Save Game    ")
    print("3. Show solution")
    print("4. Go to Main Menu")
    print("================")
    choice = int(input("Choice: "))
    print("\n")

    return choice

# Asks for player's move while playing
def moveChoice():
    print("===== MENU =====")
    print("1. Fill Cell    ")
    print("2. Delete Cell  ")
    print("================")
    choice = int(input("Choice: "))
    print("\n")

    return choice

def main():
    print("Welcome to sudoku!")

    while True:
        # Prompt right on
        pregame = pregameChoice()

        # If new game, set up the new duplicate board through deep copy of originalBoard
        if (pregame == 1):
            # Should not be touched except when loading
            originalBoard = generateBoard()

            # Deep copy
            dupBoard = copy.deepcopy(originalBoard)
            coverBoard(dupBoard)
        
        # If load game, set up the dupBoard through the load game
        elif (pregame == 2):
            makeSure = input("Are you sure you want to load game? Y/N: ")

            if (makeSure == "Y"):
                # Check first if the file exists
                if checkFile("sudoku.txt") == False:
                    print("File is either empty or doesn't exists. Create a new game instead\n")
                    continue
                dupBoard, originalBoard = loadGame()

        # Exit
        else:
            return

        # Return an array of possible (row, col) to be used for verification of
        # validity of moves
        arrOfChoices = getArrOfChoice(dupBoard)

        # Game proper
        ingame = -1
        while (ingame != 4 and ingame != 3 and checkBoardFull(dupBoard) == False):
            displayBoard(dupBoard)
            ingame = ingameChoice()

            # If making a move
            if (ingame == 1):
                move = moveChoice()

                # If move is fill
                if (move == 1):
                    row, col = inputRowCol(dupBoard, arrOfChoices)
                    inputAnswer(dupBoard, row, col)

                # If move is delete
                elif (move == 2):
                    deleteAnswer(dupBoard, arrOfChoices)

            # Save the current state of the game
            elif (ingame == 2):
                saveGame(dupBoard, originalBoard)

            # Reveal the solution then go back to the main menu
            elif (ingame == 3):
                print("The solution to the sudoku board is: ")
                revealSolution(originalBoard)

        # Check if the answer is correct
        if dupBoard == originalBoard:
            print("Congrats you solved the sudoku!")

            playAgain = input("Play again? Y/N: ")

            if (playAgain == "N"):
                break
            
if __name__ == "__main__":
    main()