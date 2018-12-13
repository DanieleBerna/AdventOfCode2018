import re
import itertools

def DrawTable(table):
    for row in table:
        print " ".join(map(str, row))

def GetPointsArea(points):

    xList = [ x for x, y in points ]

    xMin= min(xList)
    xMax= max(xList)

    yList = [ y for x, y in points ]
    yMin = min(yList)
    yMax = max(yList)


    sizeX = xMax-xMin
    sizeY = yMax-yMin

    return (sizeX*sizeY,sizeX,sizeY,xMin,yMax)


def GetMessageFromTheSky(points):
    updatedPoints=[ [x,y] for x, y, _, _ in points ]
    oldArea = GetPointsArea(updatedPoints)[0] # Stores the area of the starting configuration of points

    messageTime=0
    for t in itertools.count():
        updatedPoints=[ (x+xv*t,y+yv*t) for x,y,xv,yv in points ] # Now moves all points according to their velocities
        currentArea = GetPointsArea(updatedPoints)[0] # Get the area of the new configuration

        if currentArea>oldArea: # if current area is bigger than old one, it means that the configuration started to get sparse again...
            updatedPoints=[ (x+xv*(t-1),y+yv*(t-1)) for x,y,xv,yv in points ] # So, roll back to the previous position (the message)
            messageTime = t-1
            break
        else:
            oldArea=currentArea

    finalSize = GetPointsArea(updatedPoints)
    message = [[' ' for i in range(finalSize[1]+1)]for j in range(finalSize[2]+1)]

    for pos in updatedPoints:
        message[pos[1]-finalSize[4]-1][pos[0]-finalSize[3]]='#'

    return (message, messageTime)


inputStrings = open('input_d10.txt').readlines()
points = []
for inString in inputStrings:
    points.append( map(int,(re.split('position=<|> velocity=<|,|>',inString)[1:-1])))

message, messageTime = GetMessageFromTheSky(points)
DrawTable(message)
print "Message time: " + str(messageTime)



