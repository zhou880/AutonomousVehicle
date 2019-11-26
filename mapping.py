# Create blank array
# https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python/6667361
# Add column to blank array
# https://stackoverflow.com/questions/2002415/how-can-i-add-an-additional-row-and-column-to-an-array
import csv

def getSensor(mapArray):
    #Reads ultrasonic data
    front = int(input('Enter front sensor value: '))
    left = int(input('Enter left sensor value: '))
    right = int(input('Enter right sensor value: '))
    return front, left, right

def generateMap(mapArray):
    #Generates map
    with open("output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(mapArray)
    
def startingLoc(x, y):
    #Calculates starting location and prints out starting array
    mapArray = [[0 for i in range(x + 1)] for j in range(y + 1)] 
    mapArray[y][x] = 5
    print(np.matrix(mapArray[::-1]))
    return mapArray

def newLoc(mapArray, direction, x, y):
    #Uses current direction to choose where to add the next traveled point
    #IN "if direction == value, value is the direction value that will occur
    # after the execution of either addRow, moveRightCol, goUnder, 
    # or moveLeftCol
    frontMax = 20
    sideMax = 15
    if front > frontMax and left < sideMax and right < sideMax:
        if direction == 1:
            mapArray, x, y = moveRightCol(mapArray, x, y)
        elif direction == 2:
           mapArray, x, y = goUnder(mapArray, x, y)
        elif direction == 3:
            mapArray, x, y = moveLeftCol(mapArray, x, y)
        elif direction == 0:
            mapArray, x, y = addRow(mapArray, x, y)
        else:
            print('Invalid direction value')
        #move forward
        
    elif front < frontMax and left < sideMax and right > sideMax:
        print(direction)
        if direction == 1: #The new position will be 1 after turning right
            mapArray, x, y = moveRightCol(mapArray, x, y)
        elif direction == 2:
            mapArray, x, y = goUnder(mapArray, x, y)
        elif direction == 3:
             mapArray, x, y = moveLeftCol(mapArray, x, y)
        elif direction == 0:
            mapArray, x, y = addRow(mapArray, x, y)
        else:
            print('Invalid direction value')
        #turn right
    
    elif front < frontMax and left < sideMax and right < sideMax:
        if direction == 1:
            mapArray, x, y = moveRightCol(mapArray, x, y)
        elif direction == 2:
            mapArray, x, y = goUnder(mapArray, x, y)
        elif direction == 3:
            mapArray, x, y = moveLeftCol(mapArray, x, y)
        elif direction == 0:
            mapArray, x, y = addRow(mapArray, x, y)
        else:
                print('Invalid direction value')
        #turn around 360
        
    elif front < frontMax and left > sideMax and right > sideMax:
        if direction == 1: #The new position will be 1 after turning right
            mapArray, x, y = moveRightCol(mapArray, x, y)
        elif direction == 2:
            mapArray, x, y = goUnder(mapArray, x, y)
        elif direction == 3:
             mapArray, x, y = moveLeftCol(mapArray, x, y)
        elif direction == 0:
            mapArray, x, y = addRow(mapArray, x, y)
        else:
            print('Invalid direction value')
        
    elif front < frontMax and left > sideMax and right < sideMax:
        if direction == 1:
            mapArray, x, y = moveRightCol(mapArray, x, y)
        elif direction == 2:
            mapArray, x, y = goUnder(mapArray, x, y)
        elif direction == 3:
            mapArray, x, y = moveLeftCol(mapArray, x, y)
        elif direction == 0:
            mapArray, x, y = addRow(mapArray, x, y)
        else:
            print('Invalid direction value')
        #turn left
        
    elif front > frontMax and left < sideMax and right > sideMax:
        if direction == 1: #The new position will be 1 after turning right
            mapArray, x, y = moveRightCol(mapArray, x, y)
        elif direction == 2:
            mapArray, x, y = goUnder(mapArray, x, y)
        elif direction == 3:
             mapArray, x, y = moveLeftCol(mapArray, x, y)
        elif direction == 0:
            mapArray, x, y = addRow(mapArray, x, y)
        else:
            print('Invalid direction value')
        #turn right
    elif front > frontMax and left > sideMax and right < sideMax:
        if direction == 1:
            mapArray, x, y = moveRightCol(mapArray, x, y)
        elif direction == 2:
           mapArray, x, y = goUnder(mapArray, x, y)
        elif direction == 3:
            mapArray, x, y = moveLeftCol(mapArray, x, y)
        elif direction == 0:
            mapArray, x, y = addRow(mapArray, x, y)
        else:
            print('Invalid direction value')
        #move forward
    elif front > frontMax and left > sideMax and right > sideMax:
        if direction == 1: #The new position will be 1 after turning right
            mapArray, x, y = moveRightCol(mapArray, x, y)
        elif direction == 2:
            mapArray, x, y = goUnder(mapArray, x, y)
        elif direction == 3:
             mapArray, x, y = moveLeftCol(mapArray, x, y)
        elif direction == 0:
            mapArray, x, y = addRow(mapArray, x, y)
        else:
            print('Invalid direction value')
        #turn right
    return mapArray, x, y

#NEED TO PUT IF STATEMENTS FOR IF THERE"S ALREADY A SPOT
def moveRightCol(mapArray, x, y):
    #adds value to right of the current position
    mapArray = [x + [0] for x in mapArray] #adds new column
    mapArray[y][x+1] = 1
    print(np.matrix(mapArray[::-1]))
    return mapArray, x+1, y
    #What if column is already created?
    
def moveLeftCol(mapArray, x, y):
    mapArray[y][x-1] = 1
    print(np.matrix(mapArray[::-1]))
    return mapArray, x - 1, y 

def goUnder(mapArray, x, y):
    mapArray[y-1][x] = 1
    print(np.matrix(mapArray[::-1]))
    return mapArray, x, y - 1

def addRow(mapArray, x, y):
    added = [0] * (len(mapArray[y-1]))
    added[x] = 1
    mapArray.append(added)
    print(np.matrix(mapArray[::-1]))
    return mapArray, x, y + 1
    

def getDirection(direction, front, left, right):
    #This function finds out what direction the robot will orient itself
    # after reading the ultrasonic values in the conditionals
    frontMax = 20
    sideMax = 15
    '''Directions
        front = 0
        right = 1
        back = 2
        left = 3 '''
    current = direction
    directionOpt = [0 ,1 ,2 ,3] #all possible directions
    if front > frontMax and left < sideMax and right < sideMax:
        direction = directionOpt[current]
        #face forward
    elif front < frontMax and left < sideMax and right > sideMax:
        if direction >= 3:
            direction = directionOpt[current -3]
        else:
            direction = directionOpt[current + 1]
           #face right
    elif front < frontMax and left > sideMax and right > sideMax:
        if direction >= 3:
            direction = directionOpt[current -3]
        else:
            direction = directionOpt[current + 1]
            #face right
    elif front < frontMax and left < sideMax and right < sideMax:
        if direction >= 2:
            direction = directionOpt[current - 2]
        else:
            direction = directionOpt[current + 2]
        #face backwards
    elif front < frontMax and left > sideMax and right < sideMax:
        if direction >= 1:
            direction = directionOpt[current - 1]
        else:
            direction = directionOpt[current + 3]
        #face left
    elif front > frontMax and left < sideMax and right > sideMax:
        if direction >= 3:
            direction = directionOpt[current -3]
        else:
            direction = directionOpt[current + 1]
        #face right
    elif front > frontMax and left > sideMax and right < sideMax:
        direction = directionOpt[current]
        #face forward
    elif front > frontMax and left > sideMax and right > sideMax:
        if direction >= 3:
            direction = directionOpt[current -3]
        else:
            direction = directionOpt[current + 1]
        #face right
    return direction #direction is passed so that the action associated 
                    # with the direction can be executed later
    
def printCurrentDirection(cD):
    print()
    if cD == 0:
        print('Robot is facing fowards')
    elif cD == 1:
        print('Robot is facing right')
    elif cD == 2:
        print('Robot is facing downwards')
    elif cD == 3:
        print('Robot is facing left')
    print()

class currentPosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.direction = direction
        

#main
import numpy as np

currentDirection = 0
xStarting = int(input('Enter starting x-coordinate location: '))
yStarting = int(input('Enter starting y-coordinate location: '))

location = currentPosition(xStarting, yStarting)
mapArray = startingLoc(xStarting, yStarting)
try:
    while True:
        front, left, right = getSensor(mapArray)
        #find new orientation of robot
        currentDirection = getDirection(currentDirection, front, left, right)
        printCurrentDirection(currentDirection)
        #generate new array after corresponding action
        mapArray, x, y = newLoc(mapArray, currentDirection, location.x, location.y)
        #redefines location of the robot
        location = currentPosition(x, y)
        
except KeyboardInterrupt: #generates map upon keyboard interrupt
    generateMap(mapArray[::-1])