#declare and make the grid that were gonna beat the shit out of, and a bool to see if it is player 1's turn
#turn number isn't really used in this version but that may change probbaly not though
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


def togglePlayerTurn():
    #wish i knew why this didn't work isP1Turn = not isP1Turn
    global isP1Turn
    if isP1Turn:
        isP1Turn = False
    else:
        isP1Turn = True


#a gift form our savior stack overflow
def printGrid():
    for row in grid:
        print('  '.join([str(elem) for elem in row]))
    return


def placeToken(): #ask player for column input (0-6)
    global turnNumber
    global isP1Turn
    turnNumber += 1
    
    if not isP1Turn:
        #player 2 is anything even, so 2nd turn, 4th, 6th etc
        currentToken = 'Y'
        togglePlayerTurn()
    else:
        #player 1 all other cases
        currentToken = 'R'
        togglePlayerTurn()
    
    print('Turn Number', turnNumber)

    dontBreakWhile = False
    hasntPicked = True
    while hasntPicked:
        try: #get input
           playerChoice = int(input('Pick Column (0-6): '))
        except ValueError: #when there is an error
            print("That's not even number you idiot")
        else:   #if it is an integer continue
            if ( 0 <= playerChoice <=6):
                for i in range(5, -1, -1):
                    if grid[i][playerChoice]==0:
                        grid[i][playerChoice] = currentToken
                        hasntPicked = False #they have picked and the procedure is done
                        break #breaks from for loop once token is placed
                    else:
                        if not grid[0][playerChoice]==0:
                            print("That Row is Full!")
                            break   #breaks from for loop when row is full
            else:
                print("that number is out of range")
            

def isGameWon():
    x = 0
    y = 0 
    #~~~~~~~~~~~~~~~~~DIAGONAL TESTING~~~~~~~~~~~~~~~~~
    #this is where it would go...IF I HAD ANY
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