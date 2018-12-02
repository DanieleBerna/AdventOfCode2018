import collections

inputStringList = open('input_d02.txt').readlines()

def ChecksumId(boxIdList):
    occurTwoCount=0
    occurThreeCount=0

    for boxID in boxIdList:

        occurences = set()
        for r in (collections.Counter(boxID).most_common(len(boxID))):
            occurences.add(r[1])
        if 2 in occurences:
            occurTwoCount+=1
        if 3 in occurences:
            occurThreeCount+=1

    print "Checksum: "+ str(occurTwoCount*occurThreeCount)

def FindCommonCharacters(boxIdList):
    oneDifferenceStrings = []

    for s1 in boxIdList:
        for s2 in boxIdList:
            numberOfDifferences = sum(1 for s1, s2 in zip(s1, s2) if s1 != s2)
            if numberOfDifferences == 1:
                oneDifferenceStrings.append((s1.rstrip("\n"), s2.rstrip("\n")))

    commonCharacters = ""
    for z in zip(oneDifferenceStrings[0][0], oneDifferenceStrings[0][1]):
        if z[0] == z[1]:
            commonCharacters += z[0]

    print "Common characters: " + commonCharacters


ChecksumId(inputStringList)
FindCommonCharacters(inputStringList)

#print inputStringList
#print collections.Counter(inputStringList)


