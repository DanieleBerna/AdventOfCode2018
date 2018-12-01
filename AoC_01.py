import itertools

def CalibrateFrequency (frequency, driftList):
    for f in driftList:
        frequency += int(f)
    return frequency

def FindFirstTwiceFrequency (frequency, driftList):
    frequenciesAlreadyFound=set([]) #Changed from list to set
    twiceFound = False
    twiceFrequency=0

    while not twiceFound:
        for f in driftList:
            frequency += int(f)
            if frequency in frequenciesAlreadyFound:
                twiceFrequency = frequency
                twiceFound=True
                break
            else:
                frequenciesAlreadyFound.add(frequency) #Changed from "append item to a list" to "add item to a set"
    return twiceFrequency

inputStringList = open('D:/input_d01.txt').readlines()
inputList = ([int(i) for i in inputStringList])

print "Frequency: " + str(CalibrateFrequency(0, inputList))
print "First Twice: " + str(FindFirstTwiceFrequency(0, inputList))
