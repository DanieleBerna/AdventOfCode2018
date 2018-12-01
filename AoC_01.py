def CalibrateFrequency (frequency, driftList):
    for f in driftList:
        frequency += int(f)
    return frequency

def FindFirstTwiceFrequency (frequency, driftList):
    frequenciesAlreadyFound=[]
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
                frequenciesAlreadyFound = frequenciesAlreadyFound+[frequency]
    return twiceFrequency

input = [int(x) for x in open('D:/input_d01.txt').readlines()]
print "Frequency: " + str(CalibrateFrequency(0,input))
print  "First Twice: " + str(FindFirstTwiceFrequency(0,parsedFrequency))