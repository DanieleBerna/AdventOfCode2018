import string


def ReactPolymer(polymerString):
    reactionPatterns = [(x[0]+x[1]) for x in (zip(string.ascii_lowercase,string.ascii_uppercase))]
    reactionPatterns.extend(p[::-1] for p in reactionPatterns[:])

    while any(pattern in polymerString for pattern in reactionPatterns):
        for pattern in reactionPatterns:
            polymerString=polymerString.replace(pattern,'')

    return polymerString


def FindShortestPolymer(polymerString):
    reactedPolymersList = []
    letters = string.ascii_lowercase
    for l in letters:
        checkString = polymerString.replace(l,'')
        checkString = checkString.replace(l.upper(), '')
        lung = len(ReactPolymer(checkString))
        reactedPolymersList.append((l,lung))
    reactedPolymersList = sorted(reactedPolymersList, key=lambda d: d[1])
    return reactedPolymersList[0][1]


inputStringList = (open('input_d05.txt').readline())[:-1]

print "Length of reacted polymer: " + str(len( ReactPolymer(inputStringList) ))

print "Length of shortest polymer without a letter: " + str(FindShortestPolymer(inputStringList))

