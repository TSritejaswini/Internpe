import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]

rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🟡" or gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
    # Check horizontal spaces
    for x in range(rows):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x][y + 1] == chip and gameBoard[x][y + 2] == chip and gameBoard[x][y + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check vertical spaces
    for y in range(cols):
        for x in range(rows - 3):
            if gameBoard[x][y] == chip and gameBoard[x + 1][y] == chip and gameBoard[x + 2][y] == chip and gameBoard[x + 3][y] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check upper right to bottom left diagonal spaces
    for x in range(rows - 3):
        for y in range(3, cols):
            if gameBoard[x][y] == chip and gameBoard[x + 1][y - 1] == chip and gameBoard[x + 2][y - 2] == chip and gameBoard[x + 3][y - 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check upper left to bottom right diagonal spaces
    for x in range(rows - 3):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x + 1][y + 1] == chip and gameBoard[x + 2][y + 2] == chip and gameBoard[x + 3][y + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    return False

def coordinateParser(inputString):
    coordinate = [None] * 2
    if inputString[0] == "A":
        coordinate[1] = 0
    elif inputString[0] == "B":
        coordinate[1] = 1
    elif inputString[0] == "C":
        coordinate[1] = 2
    elif inputString[0] == "D":
        coordinate[1] = 3
    elif inputString[0] == "E":
        coordinate[1] = 4
    elif inputString[0] == "F":
        coordinate[1] = 5
    elif inputString[0] == "G":
        coordinate[1] = 6
    else:
        print("Invalid column. Please choose a letter from A to G.")
        return None

    try:
        coordinate[0] = int(inputString[1])
        if coordinate[0] < 0 or coordinate[0] >= rows:
            print("Invalid row. Please choose a number from 0 to 5.")
            return None
    except ValueError:
        print("Invalid row. Please choose a number from 0 to 5.")
        return None

    return coordinate

def isSpaceAvailable(intendedCoordinate):
    if gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔴' or gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🟡':
        return False
    return True

def gravityChecker(intendedCoordinate):
    spaceBelow = [intendedCoordinate[0] + 1, intendedCoordinate[1]]
    if spaceBelow[0] == rows:
        return True
    if not isSpaceAvailable(spaceBelow):
        return True
    return False

leaveLoop = False
turnCounter = 0
while not leaveLoop:
    if turnCounter % 2 == 0:
        printGameBoard()
        while True:
            spacePicked = input("\nChoose a space (e.g., A0): ").strip().upper()
            coordinate = coordinateParser(spacePicked)
            if coordinate and isSpaceAvailable(coordinate) and gravityChecker(coordinate):
                modifyArray(coordinate, '🟡')
                break
            else:
                print("Not a valid coordinate. Try again.")
        winner = checkForWinner('🟡')
        turnCounter += 1
    else:
        while True:
            cpuLetter = random.choice(possibleLetters)
            cpuRow = random.randint(0, rows - 1)
            cpuChoice = f"{cpuLetter}{cpuRow}"
            cpuCoordinate = coordinateParser(cpuChoice)
            if cpuCoordinate and isSpaceAvailable(cpuCoordinate) and gravityChecker(cpuCoordinate):
                modifyArray(cpuCoordinate, '🔴')
                break
        winner = checkForWinner('🔴')
        turnCounter += 1

    if winner:
        printGameBoard()
        break
