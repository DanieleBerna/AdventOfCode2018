import numpy as np


def GetPowerLevel(x,y,serialNumber):
    # Returns the power level of a cell
    return (((((x+10)*y)+serialNumber)*(x+10))// 10**2 % 10)-5


def FillEnergyGrid(gridSize,serialNumber):
    # Build the power grid as a 2D numpy array where each cell contains its own power level
    grid = np.zeros([gridSize,gridSize])

    for x in range(gridSize):
        for y in range(gridSize):
            grid[x][y]= GetPowerLevel(x+1,y+1,serialNumber)
    return grid


def FindMaxSquare(grid,gridSize,maxSquareSize,fixedSquareSize=True):
    maxEnergy=-99999999999
    maxCell=()
    size=1
    startingSquareSize=1

    if fixedSquareSize:
        startingSquareSize=maxSquareSize

    for squareSize in range(startingSquareSize,maxSquareSize+1):
        for x in range((squareSize-1),gridSize):
            for y in range(gridSize-squareSize+1):
                squareEnergy = np.sum(grid[x:squareSize - gridSize + x, y:squareSize - gridSize + y])
                if squareEnergy>maxEnergy:
                    maxEnergy=squareEnergy
                    maxCell=(x+1,y+1)
                    size=squareSize
    return (maxCell,maxEnergy,size)



gridSize=300
serialNumber = 3031 #my input

# PART 1
cellCoords, maxEnergy, _ = FindMaxSquare( FillEnergyGrid(gridSize,serialNumber),gridSize, 3 )
print "Coordinates of top-left fuel cell: " + str(cellCoords)
print "Total energy of the 3x3 square: " + str(maxEnergy)
print "RESULT: " + str(cellCoords[0]) + ',' + str(cellCoords[1])

# PART 2
cellCoords, maxEnergy, maxSize =FindMaxSquare( FillEnergyGrid(gridSize,serialNumber),gridSize, 300, fixedSquareSize=False )
print "Coordinates of top-left fuel cell: " + str(cellCoords)
print "Total energy of the square: " + str(maxEnergy)
print "Size of the square: " + str(maxSize)
print "RESULT: " + str(cellCoords[0])+ ',' + str(cellCoords[1]) + ',' + str(maxSize)
