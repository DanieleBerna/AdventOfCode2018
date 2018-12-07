import numpy as np
import re

def TaxicabDistance(p,q):
    return sum([abs(sum(y)) for y in(zip(p,(-x for x in q)))])

# Get list of points' coordinates
inputFile = open('input_d06.txt').readlines()
locationsList=[]
for i in inputFile:
    parsedInput = re.split(',| |\n',i)
    locationsList.append((int(parsedInput[0]),int(parsedInput[2])))

# Get some info about the "city map"
mapMin = (min(locationsList,key=lambda item:item[0])[0],min(locationsList,key=lambda item:item[1])[1])
mapMax = (max(locationsList,key=lambda item:item[0])[0],max(locationsList,key=lambda item:item[1])[1])
mapSize = (mapMax[0]-mapMin[0],mapMax[1]-mapMin[1])

for i in range(len(locationsList)):
    locationsList[i] = (locationsList[i][0]-mapMin[0],locationsList[i][1]-mapMin[1])

areaMap = np.zeros((mapSize[0]+1, mapSize[1]+1))

locationsList= zip(locationsList,range(len(locationsList)))

for i in range(mapSize[0]+1):
    for j in range(mapSize[1]+1):
        distances = []
        for p in locationsList:
            d = TaxicabDistance((j,i),p[0])
            distances.append(d)
        minDist = min(distances)
        if distances.count(minDist)>1:
            areaMap[i][j]=None
        else:
            areaMap[i][j]=locationsList[distances.index(minDist)][1]

regionSize =max([np.count_nonzero(areaMap == p[1]) for p in locationsList])
print "Size of closed region of short distances: " + str(regionSize)


regionSize=0
for i in range(mapSize[0]+1):
    for j in range(mapSize[1]+1):
        tempDist=0
        for p in locationsList:
            tempDist += TaxicabDistance((j,i),p[0])
        if tempDist<10000:
            regionSize += 1

print "Size of region with sum of distances < 10000: " + str(regionSize)