import datetime


def ParseInput(inputStringList):

    sortedInputStringList = sorted(inputStringList, key=lambda x: datetime.datetime.strptime(x.split(']')[0][1:], '%Y-%m-%d %H:%M'))

    parsedInput=[]
    guardsSet = set()

    for s in sortedInputStringList:
        stringParts = s.split(" ")
        asleep = False
        guardID = -1
        sleepDuration = 0.0

        timestamp = stringParts[0]+' '+stringParts[1]
        sleepMinutesInterval = (-1,-1)

        if stringParts[2]=='falls':
            asleep = True
        elif stringParts[2]=='wakes':
            startSleepTime = datetime.datetime.strptime(parsedInput[-1]['timestamp'], '[%Y-%m-%d %H:%M]')
            endSleepTime = datetime.datetime.strptime(timestamp, '[%Y-%m-%d %H:%M]')
            sleepDuration = ( endSleepTime-startSleepTime).total_seconds() / 60
            sleepMinutesInterval =(startSleepTime.minute,endSleepTime.minute)

        if '#' in stringParts[3]:
            guardID = int(stringParts[3][1:])
            guardsSet.add(guardID)
        else:
            guardID = parsedInput[-1]['guardID']

        parsedInput.append( {'timestamp':timestamp,'guardID':guardID,'asleep': asleep, 'sleepDuration':sleepDuration, 'sleepMinutesInterval':sleepMinutesInterval } )

    return (parsedInput,guardsSet)


def FindMinuteAndGuard(parsedList, guardsSet):
    lista = []
    for g in guardsSet:
        sleepData = {}
        sleepData['guardID'] = g
        sleepData['sleepTotal'] = 0
        sleepData['minutes'] = [0 for m in range(60)]

        for i in parsedList:
            if g == i['guardID'] and i['sleepDuration'] > 0:
                sleepData['sleepTotal'] += i['sleepDuration']
                if i['sleepMinutesInterval'][0] != -1:
                    startMinute = i['sleepMinutesInterval'][0]
                    endMinute = i['sleepMinutesInterval'][1]
                    temp = [0 for m in range(60)]
                    temp[startMinute:endMinute] = [1 for x in range(endMinute - startMinute)]

                    sleepData['minutes'] = [sum(x) for x in zip(sleepData['minutes'], temp)]

        lista.append(sleepData)

    sortedList = sorted(lista, key=lambda d: d['sleepTotal'], reverse=True)

    return (sortedList[0]['guardID'], sortedList[0]['minutes'].index(max(sortedList[0]['minutes'])),sortedList)

def FindMostFrequentlyMinute (sortedList):
    currentGuard = 0
    currentMinute = 0
    currentMax = 0
    for s in sortedList:
        if max(s['minutes'])>currentMax:
            currentMax = max(s['minutes'])
            currentMinute = s['minutes'].index(max(s['minutes']))
            currentGuard = s['guardID']
    return (currentGuard,currentMinute)


inputStringList = open('input_d04.txt').readlines()
parsedInput , guardsSet = ParseInput(inputStringList)

guard,minute, sortedList = FindMinuteAndGuard(parsedInput, guardsSet)
print "ID of the guard that has the most minutes asleep multiplied by the minute: " + str(guard*minute)

currentGuard,currentMinute = FindMostFrequentlyMinute (sortedList)
print "ID of the guard most frequently asleep on the same minute multiplied by the minute: " + str(currentGuard*currentMinute)




