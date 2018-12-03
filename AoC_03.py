import re

def SplitClaim(claimID):
    # Parse the claimID returning a dictionary
    parsedClaim = re.split('#|,| |@|:|x',claimID)
    return {'id':int(parsedClaim[1]),'x':int(parsedClaim[4]),'y':int(parsedClaim[5]),'sizeX':int(parsedClaim[7]),'sizeY':int(parsedClaim[8])}


def CheckForFabricConflicts(claimIDs):
    # Cycles all claims setting values for the fabricTable
    fabricTable = [[0 for y in range(1000)] for x in range(1000)]
    totalConflicts = 0
    for claimID in claimIDs:
        claim = SplitClaim(claimID)
        for i in range(claim['x'], claim['x'] + claim['sizeX']):
            for j in range(claim['y'], claim['y'] + claim['sizeY']):
                fabricTable[i][j] += 1
                if fabricTable[i][j] == 2:
                    totalConflicts += 1
    return (fabricTable, totalConflicts)


def FindNonOverlappingClaimID(fabricTable, claimIDs):
    # Tests each claim with the previously generated fabric table
    for claimID in claimIDs:
        conflictFound = False
        claim = SplitClaim(claimID)
        for i in range(claim['x'], claim['x'] + claim['sizeX']):
            for j in range(claim['y'], claim['y'] + claim['sizeY']):
                if fabricTable[i][j] >1:
                    conflictFound=True
                    break
        if not conflictFound:
            return claim['id']


inputStringList = open('input_d03.txt').readlines()
checkResult = CheckForFabricConflicts(inputStringList)

print "Claim conflicts: "+ str(checkResult[1])
print "Non overlapping claimID: " + str( FindNonOverlappingClaimID(checkResult[0], inputStringList) )

