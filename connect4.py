#declare and make the grid that were gonna beat the shit out of, and a bool to see if it is player 1's turn
turnNumber = 0
isP1Turn = True

grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

def printGrid():
    for row in grid:
        print('  '.join([str(elem) for elem in row]))
    return

def placeToken(): #ask player for column input (0-6)
    global turnNumber
    global isP1Turn
    turnNumber += 1
    #player 1 is red, player one goes on odd rounds
    if(turnNumber%2 == 0):
        currentToken = 'Y'
        isP1Turn = False
    else:
        currentToken = 'R'
        isP1Turn = True
    
    print('Turn Number', turnNumber)
    while True:
        try: #get input
           playerChoice = int(input('Pick Column (0-6): '))
        except ValueError:
            print("That's not even number you idiot")
        else:
            #If the current column has something at the bottom, go up one and check, if its open place it
            if (0 <= playerChoice <=6): 
                if not grid[5][playerChoice]==0:
                    if not grid[4][playerChoice]==0:
                        if not grid[3][playerChoice]==0:
                            if not grid[2][playerChoice]==0:
                                if not grid[1][playerChoice]==0:
                                    if not grid[0][playerChoice]==0:
                                            print("That Row is Full!")
                                    else:
                                        grid[0][playerChoice] = currentToken
                                        break
                                else:
                                    grid[1][playerChoice] = currentToken
                                    break
                            else:
                                grid[2][playerChoice] = currentToken
                                break
                        else:
                            grid[3][playerChoice] = currentToken    
                            break
                    else:
                        grid[4][playerChoice] = currentToken
                        break                                     
                else:
                    grid[5][playerChoice] = currentToken
                    break         
            #a few easter eggs for if you input funny numbers
            elif playerChoice == 69:
                print("nice but please input a number in the range 0-6: ")
            elif playerChoice == 7355608:
                print('Bomb has been planted')
            else:
               print('Out of range. Try again')

def isGameWon():
    x = 0
    y = 0 
    #~~~~~~~~~~~~~~~~~VERTICAL TESTING~~~~~~~~~~~~~~~~~
    for x in range(7):
        for y in range(6):
            if grid[y][x] == 'R':
                redTally += 1 #start counting when a R is detected
                if redTally == 4: #once the limit is reached return 2 and stop
                    return 1
            else:
                redTally = 0 #once stream broken, reset counter
            redTally = 0 #reset after checking a column
            if grid[y][x] == 'Y':
                yellowTally += 1 #start counting when a R is detected
                if yellowTally == 4: #once the limit is reached return 2 and stop
                    return 2
            else:
                    yellowTally = 0 #once stream broken, reset counter
        yellowTally = 0 #reset after checking a column
    #~~~~~~~~~~~~~~~~HORIZONTAL TESTING~~~~~~~~~~~~~~~~
    for y in range(6):
        for x in range(7):
            if grid[y][x] == 'R':
                redTally += 1
                if redTally == 4:
                    return 1
            else:
                redTally = 0
        redTally = 0 
        if grid[y][x] == 'Y':
                yellowTally += 1
                if yellowTally == 4:
                    return 2
        else:
            yellowTally = 0 
        yellowTally = 0
    
    return 0 #if nobody won just return 0



gameState = 0
while gameState == 0:
    printGrid()
    placeToken()
    gameState = isGameWon()


if gameState == 1:
    printGrid()
    print('Good Job Player 1!')
elif gameState == 2:
    printGrid()
    print('Good Job Player 2!')

