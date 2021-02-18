#declare and make the grid that will be used to represent the game board, and a boolean to see if it is player 1's turn
turnNumber = 0
isP1Turn = True
gameState = 0

#remember 0, 0 is top left corner, and 6, 7  is bottom right
#coords would be (Y,X)

grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]


def returnIsP1Turn():
    global isP1Turn
    return isP1Turn


def togglePlayerTurn():
    global isP1Turn
    if isP1Turn:
        isP1Turn = False
    else:
        isP1Turn = True


def printGrid():
    for row in grid:
        print('  '.join([str(elem) for elem in row]))
    return


def placeToken(): #ask player for column input (0-6)
    global turnNumber
    turnNumber += 1
    
    if not returnIsP1Turn():
        #player 2 is anything even, so 2nd turn, 4th, 6th etc
        currentToken = 'Y'
        togglePlayerTurn()
    else:
        #player 1 all other cases
        currentToken = 'R'
        togglePlayerTurn()
    
    print('Turn Number', turnNumber)

    hasntPicked = True
    while hasntPicked:
        try: #get input
           playerChoice = int(input('Pick Column (1-7): '))
        except ValueError: #when there is an error
            print("That's not even number you idiot")
        else:   #if it is an integer continue
            if (1 <= playerChoice <= 7):
                playerChoice -= 1 #this is to make the user input make more sense
                for i in range(5, -1, -1):
                    if grid[i][playerChoice]==0:
                        grid[i][playerChoice] = currentToken
                        hasntPicked = False #they have picked and the procedure is done
                        break #breaks from for loop once token is placed
                    else:
                        if not grid[0][playerChoice]==0:
                            print("That Row is Full!")
                            break   #breaks from for loop when row is full, to request new value
            else:
                print("that number is out of range")
            

def isGameWon():
    x = 0
    y = 0 
    #A gift from our savior kris
    #~~~~~~~~~~~~~~~~~DIAGONAL-UP TESTING~~~~~~~~~~~~~~~~~
    for x in range(4):
        for y in range(5,2,-1):
            redTally = 0
            yellowTally = 0
            for i in range(4):

                if grid[y-i][x+i] == 'R':
                    redTally += 1       #start counting when a R is detected
                    if redTally == 4:   #once the limit is reached return 2 and stop
                        return 1
                else:
                    redTally = 0        #once stream broken, reset counter
                if grid[y-i][x+i] == 'Y':
                    yellowTally += 1    #start counting when a R is detected
                    if yellowTally == 4:#once the limit is reached return 2 and stop
                        return 2
                else:
                    yellowTally = 0     #once stream broken, reset counter
    #~~~~~~~~~~~~~~~~~DIAGONAL-DOWN TESTING~~~~~~~~~~~~~~~~~
    for x in range(4):
        for y in range(3):
            redTally = 0
            yellowTally = 0
            for i in range(4):

                if grid[y+i][x+i] == 'R':
                    redTally += 1       #start counting when a R is detected
                    if redTally == 4:   #once the limit is reached return 2 and stop
                        return 1
                else:
                    redTally = 0        #once stream broken, reset counter
                if grid[y+i][x+i] == 'Y':
                    yellowTally += 1    #start counting when a R is detected
                    if yellowTally == 4:#once the limit is reached return 2 and stop
                        return 2
                else:
                    yellowTally = 0     #once stream broken, reset counter
    #~~~~~~~~~~~~~~~~~VERTICAL TESTING~~~~~~~~~~~~~~~~~
    redTally = 0
    yellowTally = 0
    for x in range(7):
        for y in range(6):
            if grid[y][x] == 'R':
                redTally += 1       #start counting when a R is detected
                if redTally == 4:   #once the limit is reached return 2 and stop
                    return 1
            else:
                redTally = 0        #once stream broken, reset counter
            if grid[y][x] == 'Y':
                yellowTally += 1    #start counting when a R is detected
                if yellowTally == 4:#once the limit is reached return 2 and stop
                    return 2
            else:
                    yellowTally = 0 #once stream broken, reset counter
        redTally = 0                #reset after checking a column
        yellowTally = 0 
    #~~~~~~~~~~~~~~~~HORIZONTAL TESTING~~~~~~~~~~~~~~~~
    for y in range(6):
        for x in range(7):
            if grid[y][x] == 'R':
                redTally += 1
                if redTally == 4:
                    return 1
            else:
                redTally = 0
        
            if grid[y][x] == 'Y':
                yellowTally += 1
                if yellowTally == 4:
                    return 2
            else:
                yellowTally = 0 
        yellowTally = 0
        redTally = 0 
    return 0 #if nobody won just return 0


while gameState == 0:
    printGrid()
    placeToken()
    gameState = isGameWon()
    if gameState == 1:
        printGrid()
        print('Good Job Player 1!')
        break
    elif gameState == 2:
        printGrid()
        print('Good Job Player 2!')
        break
quit
